from typing import Optional

import pytest
from pydantic import field_validator
from pydantic.error_wrappers import ValidationError

from sqlmodel_v2_beta import SQLModel


def test_validation(clear_sqlmodel):
    """Test validation of implicit and explict None values.

    # For consistency with pydantic, validators are not to be called on
    # arguments that are not explicitly provided.

    https://github.com/tiangolo/sqlmodel/issues/230
    https://github.com/samuelcolvin/pydantic/issues/1223

    """

    class Hero(SQLModel):
        name: Optional[str] = None
        secret_name: Optional[str] = None
        age: Optional[int] = None

        @field_validator("name", "secret_name", "age")
        def reject_none(cls, v):
            assert v is not None
            return v

    Hero.model_validate({"age": 25})

    with pytest.raises(ValidationError):
        Hero.model_validate({"name": None, "age": 25})
