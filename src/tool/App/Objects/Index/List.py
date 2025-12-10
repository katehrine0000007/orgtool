from App.Objects.Object import Object
from App.Objects.Increment import Increment
from App.Objects.DictList import DictList
from pathlib import Path
from typing import Generator
from .LoadedObject import LoadedObject, NotAnObjectError
import traceback
from App import app

class List(Object):
    id: Increment = None
    items: DictList = None
    calls: list = []
    special_names: list = [
        {
            'side': 'start',
            'path': 'App\\Storage\\Config.py'
        },
        {
            'side': 'start',
            'path': 'App\\Logger\\Logger.py'
        },
        {
            'side': 'start',
            'path': 'Web\\DownloadManager\\Manager.py'
        },
        {
            'side': 'end',
            'path': 'App\\Storage\\Storage.py'
        }
    ]
    

    def constructor(self):
        self.id = Increment()
        self.items = DictList(items = [])

    def load(self, include: list[Path]):
        # traceback.print_list(traceback.extract_stack())

        # It will never show because Logger is not loaded and mounted at this moment :))
        self.log("Loading objects list")
        _cached_names = []

        for plugin in self.scan(include):
            if plugin.is_prioritized == True:
                plugin.selfInit()

            self.items.append(plugin)

            # Loading submodules
            if plugin.getModule() != None:
                _cached_names.append(plugin.getModule().getClassNameJoined())

                for submodule in plugin.getModule().getAllSubmodules():
                    name = submodule.item.getClassNameJoined()
                    if name in _cached_names:
                        continue

                    _obj = LoadedObject()
                    _obj.is_submodule = True
                    _obj.category = submodule.item.getClassName()
                    _obj.title = submodule.item.__name__
                    _obj._module = submodule.item

                    _obj.succeed_load()

    def scan(self, includes: list[Path]) -> Generator[Path]:
        # TODO rewrite
        global_path = includes[0]
        start_plugins = []
        end_plugins = []
        _side_names = ['', '__pycache__', 'Base.py', 'tool.py', '.gitkeep']

        for plugin in self.special_names:
            _path = global_path.joinpath(Path(plugin.get('path')))
            match (plugin.get('side')):
                case 'start':
                    start_plugins.append(_path)
                case _:
                    end_plugins.append(_path)

        for plugin in start_plugins:
            _plugin = LoadedObject.from_path(plugin.relative_to(global_path))
            _plugin.is_prioritized = True

            yield _plugin

        for path in includes:
            files = path.rglob('*.py')

            for plugin in files:
                if plugin.name not in _side_names and plugin not in start_plugins:
                    yield LoadedObject.from_path(plugin.relative_to(path))

        for plugin in end_plugins:
            _plugin = LoadedObject.from_path(plugin.relative_to(global_path))
            _plugin.is_prioritized = True

            yield _plugin

    def getObjectsByNamespace(self, category: list[str]) -> Generator[LoadedObject]:
        '''
        find by category:

        category="App.Objects" - returns all plugins from App\\Objects
        '''
        for item in self.items.toList():
            # TODO: add a better check
            if '.'.join(item.category).startswith('.'.join(category)):
                yield item

    def getByName(self, key: str, class_name = None) -> LoadedObject:
        _item = self.items.get(key)
        if class_name != None:
            if class_name != _item.self_name:
                return None

        return _item

    def getList(self) -> list:
        return self.items.items
