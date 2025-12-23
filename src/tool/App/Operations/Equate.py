from App.Objects.Act import Act
from App.Objects.Misc.DictList import DictList
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Argument import Argument

class Equate(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items=[
            Argument(
                name = 'equate_this'
            ),
            Argument(
                name = 'to'
            )
        ])

    async def implementation(self, i) -> None:
        i.values['equate_this'].current = i.get('to')
