from App.Objects.Object import Object
from Files.Dir import Dir
from pydantic import Field
from pathlib import Path

class File(Object):
    directory: Dir = Field()
    name: str = Field()
    size: int = Field(default = 0)

    def constructor(self):
        path = Path(self.directory.path).joinpath(self.name)
        stat = path.stat()

        self.size = stat.st_size
