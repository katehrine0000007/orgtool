from App.Objects.Mixins.BaseModel import BaseModel
from .Condition import Condition
from pydantic import Field

class Sort(BaseModel):
    condition: Condition = Field()
    descend: bool = Field(default = False)
