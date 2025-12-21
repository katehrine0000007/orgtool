from App.Objects.BaseModel import BaseModel
from typing import Any
from pydantic import Field

class Condition(BaseModel):
    val1: Any = Field()
    operator: str | Any = Field()
    val2: Any = Field()

    def getFirst(self, model):
        return getattr(model, self.val1)

    def getLast(self):
        return self.val2
