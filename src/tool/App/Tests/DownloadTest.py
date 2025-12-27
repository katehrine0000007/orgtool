from App.Objects.Test import Test
from App.Objects.Responses.ObjectsList import ObjectsList
from App import app
import asyncio

class DownloadTest(Test):
    async def implementation(self, i):
        storage = app.Storage.get('content')
        _url = "https://i.ibb.co/4gZHtNKL/image.png"
        _unit = storage.getStorageUnit()

        self.log('sleep')
        await asyncio.sleep(10)
        self.log('.')

        item = app.DownloadManager.addURL(_url, _unit, 'image.png')
        await item.start()

        return ObjectsList(items = [_unit])
