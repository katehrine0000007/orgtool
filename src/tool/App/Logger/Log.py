from App.Objects.Object import Object
from . import LogSection, LogPrefix
from pydantic import Field
from datetime import datetime
from typing import Literal
from App import app

class Log(Object):
    class Colors():
        reset = "\033[0m"
        message = "\033[0m"
        section = "\u001b[35m"
        prefix = "\u001b[36m"
        error = "\033[91m"
        success = "\033[92m"
        deprecated = "\033[93m"

    message: str = Field(default="-")
    role: list[Literal['success', 'error', 'deprecated', 'message', 'highlight', 'bright'] | str] = Field(default = ['message'])
    time: datetime = Field(default_factory=lambda: datetime.now())
    section: LogSection.LogSection = Field(default = LogSection.LogSection())
    prefix: LogPrefix.LogPrefix = Field(default = None)

    def toParts(self) -> list[str]:
        RESET = self.Colors.reset

        parts = []
        parts.append(self.time.strftime("%H:%M:%S.%f"))        
        parts.append(self.Colors.section + self.section.toString() + RESET)
        if self.prefix != None:
            parts.append(self.Colors.prefix + self.prefix.toString() + RESET)

        if app.Config.get('logger.show_role') == True:
            if len(self.role) > 0:
                _role = ", ".join(self.role)
                parts.append(self.Colors.deprecated + f"<{_role}>" + RESET)

        parts.append(self.getColor() + self.message + RESET)
        parts.append(RESET)

        return parts

    def toStr(self) -> str:
        return " ".join(self.toParts()).replace("\\n", "\n")

    def getColor(self) -> str:
        for item in ['success', 'error', 'deprecated', 'message']:
            if item in self.role:
                return getattr(self.Colors, item)

        return self.Colors.message
