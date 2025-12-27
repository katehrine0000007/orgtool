from App.Objects.View import View
from App.Objects.Object import Object
from App.Objects.Arguments.Argument import Argument
from App.Objects.Responses.Error import Error
from Data.String import String
from Data.Int import Int
from Data.Boolean import Boolean
from Data.JSON import JSON
from aiohttp import web
from App import app
import asyncio, traceback

class WebServer(View):
    async def implementation(self, i):
        _pre_i = i.get('pre_i')

        _host = self.getOption("web.options.host")
        _port = self.getOption("web.options.port")
        _app = web.Application()
        _ws_connections = list()

        def _spa(request):
            return web.Response(
                text = 'spa',
                content_type = 'text/html'
            )

        def _get_asset(request):
            pass

        def _get_storage_unit(request):
            pass

        async def _call_shortcut(pre_i, args):
            _json = JSON(data = {})
            results = None
            args['auth'] = app.AuthLayer.users[-1]

            try:
                results = await pre_i.execute(args)
            except Exception as e:
                results = Error(
                    name = e.__class__.__name__,
                    message = str(e)
                )
                traceback.print_exception(e)

            _json.data = results.to_json()

            return _json

        async def _single_call(request):
            pre_i = _pre_i()
            #i = request.match_info.__dict__()
            _i = await request.json()
            self.log('Calling, i={0}'.format(_i.get('i')))

            _json = _call_shortcut(pre_i, _i)

            return web.Response(
                text = _json.dump(),
                content_type = 'application/json'
            )

        async def _ws(request):
            ws = web.WebSocketResponse()
            await ws.prepare(request)
            self.log('websocket connection')

            _ws_connections.append(ws)

            async for msg in ws:
                try:
                    if msg.type != web.WSMsgType.TEXT:
                        continue

                    data = JSON.fromText(text = msg.data).data
                    _type = data.get('type')
                    _event_index = int(data.get('event_index'))
                    _payload = data.get('payload')

                    self.log('got message {0}, index {1}'.format(_type, _event_index))

                    if _type == 'object':
                        pre_i = _pre_i()
                        results = await _call_shortcut(pre_i, _payload)

                        await ws.send_str(JSON(data={
                            'type': _type,
                            'event_index': _event_index,
                            'payload': results.data
                        }).dump())
                except Exception as e:
                    traceback.print_exception(e)

            _ws_connections.remove(ws)

            return ws

        def _upload_storage_unit(request):
            pass

        # scary
        for route in [
            ('/', _spa, 'get'),
            ('/static/{path:.*}', _get_asset, 'get'),
            ('/storage/{id:.*}/{path:.*}', _get_storage_unit, 'get'),
            ('/api', _single_call, 'get'),
            ('/rpc', _ws, 'get'),
            ('/api/upload', _upload_storage_unit, 'get'),
        ]:
            getattr(_app.router, 'add_' + route[2])(route[0], route[1])#(route[0], getattr(self, route[1]))

        runner = web.AppRunner(_app)
        await runner.setup()

        async def _log_ws(to_print, check_categories):
            for connection in _ws_connections:
                await connection.send_str(JSON(data={
                    'type': 'log',
                    'event_index': 0,
                    'payload': to_print.to_json()
                }).dump())
        
        app.Logger.addHook('log', _log_ws)

        site = web.TCPSite(
            runner,
            host = _host,
            port = _port
        )

        await site.start()

        self.log("Started server at {0}:{1}".format(_host, _port))

        while True:
            await asyncio.sleep(3600)

    @classmethod
    def getSettings(cls) -> list:
        return [
            Argument(
                name = 'web.options.host',
                default = '127.0.0.1',
                orig = String
            ),
            Argument(
                name = 'web.options.port',
                default = '22222',
                orig = Int
            ),
            Argument(
                name = 'web.aiohttp.debug',
                default = True,
                orig = Boolean
            )
        ]
