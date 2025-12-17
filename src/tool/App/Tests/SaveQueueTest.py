from App.Objects.Test import Test
from Data.Random import Random
from App.Queue.Run import Run
from App.Storage.Save import Save

class SaveQueueTest(Test):
    async def implementation(self, i):
        '''
        runs = Run()
        args = {
            'items': [
                {
                    'predicate': 'Data.Random.Random',
                    'arguments': {
                        'min': 999,
                        'max': 8888888
                    }
                },
                {
                    "predicate": "App.Storage.Save.Save",
                    "arguments": {
                        "equate_this": {
                            "direct_value": "$0"
                        },
                    }
                }
            ]
        }'''

        rnd = Random()
        val = await rnd.execute({'min': 99, 'max': 8888})
        _sav = Save()
        
        return _sav.execute({'items': val})
