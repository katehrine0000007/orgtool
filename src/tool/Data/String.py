from App.Objects.Object import Object
from pydantic import Field

class String(Object):
    value: str = Field()

    @classmethod
    def asArgument(cls, val):
        if val == None:
            return None

        return str(val)
