from App.Objects.Client import Client
from App.Objects.Submodule import Submodule
from Files.Dir import Dir
from Files.File import File

class FileManager(Client):
    @classmethod
    def getSubmodules(cls):
        return [
            Submodule(
                module = Dir,
                value = Submodule.ConnectionEnum.INTERNAL
            ),
            Submodule(
                module = File,
                value = Submodule.ConnectionEnum.INTERNAL
            )
        ]
