from App.Objects.Act import Act
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Objects.List import List
from App.Arguments.Objects.Orig import Orig
from App.Objects.Misc.DictList import DictList
from .Item import Item
from .OutputItem import OutputItem
from .Queue import Queue
from App.Responses.Response import Response

class Run(Act):
    '''
    Queue's entrypoint
    '''

    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items=[
            List(
                name = 'prestart',
                orig = Orig(
                    name = 'prestart_item',
                    orig = Item
                )
            ),
            List(
                name = 'items',
                orig = Orig(
                    name = 'items_item',
                    orig = Item
                )
            ),
            List(
                name = 'output',
                orig = Orig(
                    name = 'output_item',
                    orig = OutputItem
                )
            )
        ])

    async def implementation(self, i):
        queue = Queue()
        queue.output = i.get('output')

        await queue.run(i.get('prestart'), i.get('items'))

        return queue.getOutput()
