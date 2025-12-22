from App.Objects.Act import Act
from App.Objects.Misc.DictList import DictList
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Objects.Same import Same

class Equate(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items=[
            Same(
                name = 'equate_this'
            ),
            Same(
                name = 'to'
            )
        ])

    async def implementation(self, i) -> None:
        i.values['equate_this'].current = i.get('to')
