Config is an entity that allows to define what options the app takes. All config entries applies from all app's classes (ObjectsList). The passed values are getting from storage/config/config.json. Config entries uses Argument classes, like in validation. But you also can pass role that can be "config" or "env".

Env is also a config but for sensitive data, values also are taking from json file.
