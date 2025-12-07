from .Response import Response
from pydantic import Field

class ModelsResponse(Response):
    models: list = Field(repr=True, default = [])

    def toDict(self) -> list:
        out = []

        for item in self.models:
            if hasattr(item, 'toJson') == False:
                out.append(None)
            else:
                out.append(item.toJson())

        return out

    @staticmethod
    def fromItems(items):
        print(items)
        new = ModelsResponse(models = items)

        return new
