from App.Objects.Act import Act
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Responses.
from Data.Checkmarks.Checkmark import Checkmark
from Data.Checkmarks.List import List
from Data.String import String

class AddCheckmark(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'list',
                id_allow = True,
                orig = List
            ),
            Argument(
                name = 'label',
                default = False,
                orig = String
            )
        ])

    def implementation(self, i):
        _list = i.get('list')
        _checkmark = Checkmark()
        _checkmark.label = i.get('label')
        item.save()

        return ObjectsList(items = [_list])
