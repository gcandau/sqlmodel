from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query

from sqlmodel_v2_beta import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/", response_model=HeroRead)
def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        db_hero = Hero.model_validate(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


@app.get("/heroes/", response_model=List[HeroRead])
def read_heroes(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with Session(engine) as session:
        heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
        return heroes


@app.get("/heroes/{hero_id}", response_model=HeroRead)
def read_hero(hero_id: int):
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero
