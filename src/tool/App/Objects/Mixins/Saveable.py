from ..Misc.ObjectMeta import ObjectMeta
from ..Misc.SavedVia import SavedVia
from typing import ClassVar
from pydantic import Field, model_validator

class Saveable():
    self_name: ClassVar[str] = 'Saveable'

    obj: ObjectMeta = Field(default = ObjectMeta())

    @model_validator(mode='after')
    def _saved_via(self):
        self.obj.saved_via = SavedVia()
        self.obj.saved_via.object_name = self.getClassNameJoined()

        return self
