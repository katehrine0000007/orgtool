from App.Objects.Act import Act
from App.Objects.Executable import Executable
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Objects.List import List
from App.Arguments.Types.String import String
from App.Arguments.Types.Boolean import Boolean
from App.Arguments.Objects.Executable import Executable as ExecutableArg
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Arguments.Assertions.InputNotInValues import InputNotInValues
from App.Arguments.ArgumentValues import ArgumentValues
from App.Responses.ObjectsList import ObjectsList
from App.Storage.Movement.Save import Save
from App.Objects.Locale.Documentation import Documentation
from App.Objects.Locale.Key import Key
from App import app

class DefaultExecutorWheel(Act):
    '''
    Class that switches the action looking by object type
    '''

    async def implementation(self, i: ArgumentValues):
        force_flush = i.get('force_flush')
        executable = i.get('i')

        assert executable != None, 'not found object'
        assert app.app.view.canUseObject(executable), 'object cannot be used at this view'
        assert executable.canBeUsedBy(None), 'access denied'

        results = None
        if force_flush == False:
            assert executable.canBeExecuted(), 'object does not contains execute interface'

            _item = executable()
            _item.integrate(i.values)
            results = await _item.execute(i = i)
        else:
            _vals = i.getValues(exclude = ['force_flush', 'i', 'pre_i', 'as_args'])
            results = ObjectsList(items = [])
            _item = executable()

            # isinstance(executable, Executable wont work with cls (

            if hasattr(executable, 'integrate') and i.get('as_args'):
                _item = executable(args = _vals)
            else:
                _item = executable(**_vals)

            results.append(_item)

        if isinstance(results, ObjectsList):
            save_to = i.get('save_to')
            if save_to != None:
                _save = Save()
                await _save.execute({
                    'items': results,
                    'storage': save_to
                })

        return results

    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            ExecutableArg(
                name = 'i',
                # default = 'App.Queue.Run',
                assertions = [
                    NotNoneAssertion(),
                    InputNotInValues(values=['App.Console.ConsoleView', 'App.Console.ConsoleView.ConsoleView'])
                ],
                documentation = Documentation(
                    name = Key(
                        value = 'Main object'
                    )
                ),
            ),
            List(
                name = 'save_to',
                default = [],
                single_recommended = True,
                documentation = Documentation(
                    name = Key(
                        value = 'Save to storages'
                    ),
                    description = Key(
                        value = 'Names of storages where object will be saved (if it returns ObjectsList)'
                    )
                ),
                orig = String(
                    name = 'save_to.item'
                )
            ),
            Boolean(
                name = 'force_flush',
                documentation = Documentation(
                    name = Key(
                        value = 'Flush literally'
                    ),
                    description = Key(
                        value = 'Flush to DB (save_to) ignoring execution interface'
                    )
                ),
                default = False
            ),
            Boolean(
                name = 'as_args',
                default = True,
                documentation = Documentation(
                    name = Key(
                        value = 'Use as args'
                    ),
                    description = Key(
                        value = 'Use another passed arguments for args field, if force_flush = true and i is an executable'
                    )
                ),
            )
        ],
        missing_args_inclusion = True)
