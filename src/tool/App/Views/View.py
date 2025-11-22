from App.Objects.Executable import Executable
from App.Arguments.ArgumentsDict import ArgumentsDict
from typing import Any
from pydantic import Field, computed_field
from App.App import App

class View(Executable):
    app: Any = None

    def setApp(self, app: App) -> None:
        self.app = app

    def setAsCommon(self):
        '''
        Sets link that can be used as

        from App import app

        app.Logger.log(...)
        '''
        from App import app

        app.setView(self)

    def implementation(self, i: ArgumentsDict = {}):
        pass
