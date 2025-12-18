from App.Console.ConsoleView import ConsoleView
from App.Responses.NoneResponse import NoneResponse
from App.Arguments.ArgumentValues import ArgumentValues
from App import app
import traceback

class InteractiveView(ConsoleView):
    async def implementation(self, i):
        is_exit = False
        prev = None
        while is_exit != True:
            self.log('pass the object name (or exit)')

            val = input("")
            if val == 'exit':
                is_exit = True
                break
            if val == 'same':
                val = str(prev)

            self.log('OK')
            self.log('Pass args (like -arg1 val1 -arg2 val2)')

            _args = input("")

            _executable = app.ObjectsList.getByName(val)
            _parse_argv = app.app._parse_argv(['interactive.py'] + _args.split(' '))
            _parsed_args = _parse_argv[0]

            try:
                await self._object_call(_executable.getModule(), True, ArgumentValues(values = _parsed_args))
            except Exception as e:
                traceback.print_exc()

            prev = val
            self.log('\n\n-------\n')

        return NoneResponse()
