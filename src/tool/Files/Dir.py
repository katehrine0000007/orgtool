from App.Objects.Object import Object
from App.Executables.Act import Act
from App.Objects.Submodule import Submodule
from pydantic import Field
from pathlib import Path

class Dir(Object):
    path: str = Field(default = None)

    def getContent(self) -> list:
        from Files.File import File

        path = Path(self.path)
        files = []

        for item in path.iterdir():
            files.append(File(
                directory = self,
                name = Path(item).name
            ))

        return files
