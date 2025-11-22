from App.App import App

current = App()
current._constructor()
current.load_plugins(current.cwd)

view_name = current.argv.get('view', 'App.Console.ConsoleView.ConsoleView')
view_class = current.objects.getByName(view_name)
view = view_class.module()
view.setAsCommon()
view.setApp(current)
current.loop.run_until_complete(view.execute(current.argv))
