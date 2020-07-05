from typing import Any
from typeguard import typechecked

from frame.settings import DEBUG


def typechecking(func: Any = None) -> Any:
    if DEBUG is True:
        return typechecked(func=func)
    return func
