from typing import Any, Dict, List, Union
from unittest.mock import patch

from sqlmodel_v2_beta import create_engine

from ...conftest import get_testing_print_function


def check_calls(calls: List[List[Union[str, Dict[str, Any]]]]):
    assert calls[0][0] == [
        {
            "name": "Deadpond",
            "secret_name": "Dive Wilson",
            "age": None,
            "id": 1,
        },
        {
            "name": "Spider-Boy",
            "secret_name": "Pedro Parqueador",
            "age": None,
            "id": 2,
        },
        {
            "name": "Rusty-Man",
            "secret_name": "Tommy Sharp",
            "age": 48,
            "id": 3,
        },
    ]


def test_tutorial_003(clear_sqlmodel):
    from docs_src.tutorial.select import tutorial003 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    check_calls(calls)


def test_tutorial_002(clear_sqlmodel):
    from docs_src.tutorial.select import tutorial004 as mod

    mod.sqlite_url = "sqlite://"
    mod.engine = create_engine(mod.sqlite_url)
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        mod.main()
    check_calls(calls)
