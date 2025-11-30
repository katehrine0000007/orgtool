from .Response import Response
from typing import Any
from pydantic import Field

class AnyResponse(Response):
    data: Any = Field(default = None)

    @staticmethod
    def fromItems(items):
        resp = AnyResponse()
        resp.data = items

        return resp
