from unittest.mock import patch

from sqlmodel_v2_beta import create_engine

from ...conftest import get_testing_print_function


def test_tutorial(clear_sqlmodel):
    from docs_src.tutorial.where import tutorial002 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    assert calls == [
        [
            {
                "name": "Spider-Boy",
                "secret_name": "Pedro Parqueador",
                "age": None,
                "id": 2,
            }
        ],
        [{"name": "Rusty-Man", "secret_name": "Tommy Sharp", "age": 48, "id": 3}],
    ]
