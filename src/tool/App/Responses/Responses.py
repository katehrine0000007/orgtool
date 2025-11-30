from App.Responses.Response import Response
from pydantic import Field

class Responses(Response):
    responses: list = Field(repr=True, default = [])

    def append(self, item):
        self.responses.append(item)

    def toData(self):
        items = []
        for item in self.responses:
            items.append(item.toData())

        return items
