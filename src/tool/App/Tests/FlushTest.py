from App.Tests.Test import Test
from Data.Text import Text
from Data.Random import Random
from App import app

class FlushTest(Test):
    async def implementation(self, i):
        self.log('creating models')

        items = [Text(text='123456'),Text(text='asdfghjkl')]

        print(items)

        _storage = app.Storage.get('content')
        _item = _storage.adapter.insertObject(items[Random().randomInt(0,1)])

        print(_item)
