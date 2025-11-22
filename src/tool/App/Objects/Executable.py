from .Object import Object
from App.Arguments.ArgumentsDict import ArgumentsDict
from App.Responses.Response import Response

class Executable(Object):
    def getArguments(self) -> ArgumentsDict:
        pass

    async def implementation(self, i: ArgumentsDict) -> Response:
        '''
        Entry point, must be redefined in your class
        '''
        pass

    async def implementation_wrap(self, i: ArgumentsDict) -> Response:
        return await self.implementation(i)

    async def before(self, i: ArgumentsDict) -> None:
        pass

    async def after(self, i: ArgumentsDict) -> None:
        pass

    async def execute(self, 
                      i: ArgumentsDict, 
                      check_arguments: bool = True, 
                      raise_on_assertions: bool = True) -> Response:
        '''
        Internal method. Calls module-defined implementation() and returns what it returns
        (No, it calls implementation_wrap())
        '''

        passing = self.getArguments().get(
            check_arguments = check_arguments,
            i = i,
            raise_on_assertions = raise_on_assertions,
        )

        await self.await_trigger('before_execute')

        response = await self.implementation_wrap(i = passing)

        await self.await_trigger('after_execute')

        return response
