from App.Responses.Response import Response

class Updateable():
    async def update(self, response: Response) -> Response:
        return response
