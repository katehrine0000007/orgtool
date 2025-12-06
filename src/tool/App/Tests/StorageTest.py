from App.Tests.Test import Test
from App import app
import asyncio

class StorageTest(Test):
    async def implementation(self, i):
        self.log('storage test')
        for item in app.Storage.items:
            self.log(str(item.to_json()))

        self.log('content db:' + str(app.Storage.get('content')))
        self.log('content db dir: ' + str(app.Storage.get('content').getStorageDir()))
        _unit = app.Storage.get('content').getStorageUnit()
        __name = _unit.getDir().joinpath('tmp')
        __name_2 = _unit.getDir().joinpath('txt.txt')
        _file = open(__name, 'w', encoding='utf-8')
        _file.flush()
        _file.close()

        _file2 = open(__name_2, 'w', encoding='utf-8')
        _file2.write('679878451591561641')
        _file2.flush()
        _file2.close()

        _unit.setCommonFile(__name)
        _unit.files = _unit.genFilesList()

        print(_unit)
        await asyncio.sleep(1)
