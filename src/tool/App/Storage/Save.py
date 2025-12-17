from App.Objects.Act import Act

class Save(Act):
    @classmethod
    def getArguments(cls):
        return ArgumentsDict(items = [
            Orig(
                name = 'items',
                orig = ObjectsList
            ),
            String(
                name = 'storage',
                assertions = [NotNullAssertion()]
            ),
            Int(
                name = 'link_max_depth',
                default = 10 # TODO move to const
            )
        ])

    async def implementation(self, i):
        results = []
        storage = i.get('storage')
        for item in i.get('items'):
            item.flush(storage)

        return results
