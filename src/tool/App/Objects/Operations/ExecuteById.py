from App.Objects.Act import Act
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Types.Int import Int
from App.Arguments.Types.Boolean import Boolean
from App.Storage.Storage import StorageArgument
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Responses.ObjectsList import ObjectsList

class ExecuteById(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            StorageArgument(
                name = 'storage',
                assertions = [NotNoneAssertion()]
            ),
            Int(
                name = 'uuid',
                assertions = [NotNoneAssertion()]
            ),
            Boolean(
                name = 'link',
                default = True
            ),
            Boolean(
                name = 'sift',
                default = True
            )
        ])

    async def implementation(self, i):
        _storage = i.get('storage')
        obj = _storage.adapter.ObjectAdapter.getById(i.get('uuid'))

        assert obj != None, 'object with this uuid not found'

        _old = obj.toPython()
        _exec = obj.toPython()
        _args = _exec.args.copy()
        _args.update(i.getValues(exclude = ['storage', 'uuid', 'link', 'sift']))

        assert _exec != None, 'not found object'
        assert _exec.canBeExecuted(), 'object does not contains execute interface'

        _res = await _exec.execute(i = _args)

        if i.get('sift') == True:
            _res = await _exec.sift(_old, _res)

        obj.flush_content(_exec)
        if isinstance(_res, ObjectsList):
            if i.get('link') == True:
                for item in _res.getItems():
                    _exec.link(item)

        return _res
