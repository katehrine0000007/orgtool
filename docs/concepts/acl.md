There is authentification system. 

### List of users

`app.auth.users` in config allows you to pass all the users:

```
    "app.auth.users": [
        {
            "name": "test",
            "password_hash": "123"
        }
    ]
```

if `root` not in this list, it will be created anyway with password `root`

to generate password_hash, call `App.ACL.GetHash`:

```
> python tool.py -i App.ACL.GetHash -string 123
> 
```
