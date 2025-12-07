from App.Objects.Object import Object
from pydantic import Field

class XML(Object):
    xml: str = Field()

    @classmethod
    def getConverters(cls) -> list:
        from Data.XMLToJson import XMLToJson

        return [XMLToJson]
