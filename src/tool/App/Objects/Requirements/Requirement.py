from App.Objects.Object import Object
from pydantic import Field

class Requirement(Object):
    name: str = Field()
    version: str = Field(default = None)

    def getName(self) -> str:
        if self.version == None:
            return f"{self.name}=={self.version}"

        return self.name
