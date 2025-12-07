from ..Argument import Argument
from typing import Any
from pydantic import Field, computed_field

class Orig(Argument):
    '''
    JSON into pydantic model. The class passed in "orig"
    If input is already an instance of "orig", it just returns it
    '''
    orig: Any = Field(default = None)

    def implementation(self, original_value: str):
        if self.orig == None:
            return original_value

        if isinstance(original_value, self.orig):
            return original_value

        _item = self.orig
        _item.model_validate(original_value)

        return _item(**original_value)
