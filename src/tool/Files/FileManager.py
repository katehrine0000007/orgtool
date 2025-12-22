from Files.Navigate import Navigate
from App.Objects.Client import Client
from App.Objects.Relations.Submodule import Submodule
from Files.Dir import Dir
from Files.File import File
from App import app

class FileManager(Client):
    @classmethod
    def getSubmodules(cls):
        return [
            Submodule(
                item = Dir,
            ),
            Submodule(
                item = File,
            ),
            Submodule(
                item = Navigate,
                role = ['wheel']
            )
        ]

    async def implementation(self, i):
        navigate = Navigate()

        return await navigate.execute({'path': str(app.app.cwd)})
