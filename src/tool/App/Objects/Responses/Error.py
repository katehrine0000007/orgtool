from App.Objects.Responses.Response import Response
from pydantic import Field

class Error(Response):
    name: str = Field()
    message: str = Field()
