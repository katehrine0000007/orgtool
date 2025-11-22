#from App.Documentation.Documentation import Documentation
# from .Assertions.Assertion import Assertion
from App.Objects.Object import Object
from typing import Any, List
from pydantic import Field, computed_field

class Argument(Object):
    name: str = Field()
    default: Any = Field(default = None)
    is_sensitive: bool = Field(default = False)
    auto_apply: bool = Field(default = False)
    #assertions: List[Assertion] = Field(default=[])

    current: Any = Field(default=None)

    # This is an abstract method.
    # I think it should pass self.inputs in i ? i={} as settings will not be used anyway
    def implementation(self, original_value: Any | str) -> Any:
        return self.value

    def getValue(self, original_value: Any | str, *args, **kwargs) -> Any:
        return self.implementation(original_value, *args, **kwargs) #**kwargs

    @computed_field
    @property
    def inputs(self) -> Any:
        if self.input_value == None:
            return self.default

        return self.input_value

    @computed_field
    @property
    def sensitive_default(self) -> Any:
        return self.default

    def checkAssertions(self):
        for assertion in self.assertions:
            assertion.check(self)

    def constructor(self):
        if self.auto_apply == True:
            self.autoApply()

    def autoApply(self):
        self.current = self.getValue()
