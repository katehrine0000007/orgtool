from ...Arguments.Argument import Argument
from pydantic import Field, computed_field

class List(Argument):
    '''
    Argument that can return multiple values and converts to another argument ("orig")
    '''

    orig: Argument = Field(default = None)
    allow_commas_fallback: bool = Field(default = True)
    single_recommended: bool = Field(default = False)
    total_count: int = Field(default=0)

    def implementation(self, original_value: str):
        results: list = []

        # WORKAROUND

        from Data.JSON import JSON

        if type(original_value) == str:
            if JSON.isStringValidJson(original_value) == True:
                original_value = JSON.fromText(original_value).data
            else:
                if self.allow_commas_fallback:
                    original_value = original_value.split(',')

        if self.orig == None:
            return original_value

        if original_value == None:
            return None

        for item in original_value:
            _orig = self.orig

            results.append(_orig.getValue(item))

        return results

    def getCount(self):
        return len(self.current)

    def getCompleteness(self):
        return self.getCount() / self.total_count

    def append(self, item):
        self.current.append(item)
