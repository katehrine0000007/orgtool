from importlib.metadata import distributions
from pydantic import BaseModel as PydanticBaseModel, computed_field, Field
from typing import ClassVar
from .classproperty import classproperty
from .Outer import Outer

class BaseModel(PydanticBaseModel):
    @computed_field
    @property
    def class_name__(self) -> str:
        return self.meta.class_name_joined

    # we can't use __init__ because of fields initialization, so we creating second constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__class__.constructor(self)

    # *args and **kwargs are not passed
    def constructor(self):
        pass

    # model_dump alias
    def to_json(self, exclude_classname: bool = False):
        # todo remove
        exclude = []
        if exclude_classname == True:
            exclude.append('class_name__')

        return self.model_dump(mode='json',exclude=exclude)

    def init_subclass(cls):
        cls.meta = cls.Meta(cls)

        # cls.submodules = cls.Submodules(cls)

    @classmethod
    def mount(cls):
        '''
        Method that called after loading
        '''
        pass

    def __init_subclass__(cls):
        for item in cls.__mro__:
            if hasattr(item, "init_subclass") == True:
                getattr(item, "init_subclass")(cls)

            if isinstance(item, PydanticBaseModel):
                item.__init_subclass__()

    class Meta(Outer):
        @property
        def mro(self) -> list:
            return self.outer.__mro__

        def getAvailableContexts(self):
            return ['web', 'cli', '*']

        def getRequiredModules(self):
            return []

        def isAbstract(self):
            return False

        def isHidden(self) -> bool:
            return getattr(self, "hidden", False) == True

        @property
        def can_be_executed(self):
            return self.isAbstract() == False and self.isHidden() == False # and self.outer hasclass Execute

        def getNotInstalledModules(self) -> list:
            all_installed = {dist.metadata["Name"].lower() for dist in distributions()}
            satisf_libs = []
            not_libs = []

            for required_module in self.getRequiredModules():
                module_versions = required_module.split("==")
                module_name = module_versions[0]

                if module_name in all_installed:
                    satisf_libs.append(module_name)
                else:
                    not_libs.append(module_name)

            return not_libs

        def isRequiredModulesInstalled(cls) -> bool:
            return len(cls.getNotInstalledModules()) == 0

        @property
        def main_module(cls):
            if hasattr(cls, "outer") == False:
                return None

            for item in cls.outer.__mro__:
                if getattr(item, "outer", None) != None:
                    return item.outer

        @property
        def name_joined(self):
            return ".".join(self.name)

        @property
        def class_name(self):
            return self.name + [self.outer.__name__]

        @property
        def class_name_joined(self):
            return ".".join(self.class_name)

        @property
        def name(self) -> list:
            _class = self.outer.__mro__[0]
            _module = _class.__module__
            _parts = _module.split('.')
            #_parts = _parts[1:]

            return _parts

        @property
        def class_module(cls) -> str:
            return cls.outer.__module__

        def canBeUsedAt(cls, at: str):
            return at in cls.getAvailableContexts()
