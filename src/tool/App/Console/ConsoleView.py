from App.Views.View import View

class ConsoleView(View):
    def implementation(self, i: dict = {}):
        print(i.get('type'))
