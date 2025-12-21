from App.Objects.Act import Act
from App.Arguments.ArgumentDict import ArgumentDict
from App.Responses.ObjectsList import ObjectsList
from App.Storage.Storage import StorageArgument
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Arguments.Objects.Orig import Orig
from App.Arguments.Objects.List import List
from App.Storage.DB.Adapters.Search.Condition import Condition

class Search(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            StorageArgument(
                name = 'storage',
                assertions = [NotNoneAssertion()]
            ),
            List(
                name = 'conditions',
                default = [],
                orig = Orig(
                    name = 'condition',
                    orig = Condition
                )
            )
        ])

    async def implementation(self, i) -> ObjectsList:
        _objects = ObjectsList(items = [])
        _storage = i.get('storage')
        _query = _storage.adapter.getQuery()
        for condition in i.get('conditions'):
            _query.addCondition(condition)

        for item in _query.getAll():
            _objects.append(item.toPython())

        return _objects
