from App.Objects.Act import Act
from App.Arguments.ArgumentDict import ArgumentDict

class Search(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [])

    async def implementation(self, i):
        pass
