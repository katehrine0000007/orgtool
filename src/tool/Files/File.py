from App.Objects.Object import Object
from pydantic import Field
from pathlib import Path

class File(Object):
    path: str = Field(default = None)
    name: str = Field(default = None)
    ext: str = Field(default = None)
    size: int = Field(default = 0)
    stat: dict = Field(default = {})
    # is_common: bool = Field(default = True)

    def countStats(self):
        path = Path(self.path)
        stat = path.stat()

        self.name = path.name
        self.size = stat.st_size
        # self.stat = dict(stat)

    @staticmethod
    def fromPath(path: Path):
        from Files.Dir import Dir
        from Files.FileTypes.FileType import FileType

        item = None
        if path.is_dir() == True:
            item = Dir(
                path = str(path)
            )
        else:
            item = File(
                path = str(path)
            )

        item.countStats()

        return FileType(file = item)

    def getParent(self):
        _upper = Path(self.path)

        return _upper.parent

    def getContent(self):
        return [self.to_json()]
