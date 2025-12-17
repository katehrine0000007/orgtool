Storage is a list of StorageItems.

StorageItem is an entity that contains db (ConnectionAdapter) and the storagsunit storage (dir).

StorageUnit is representation of the file. It creates dir from hash (that randomly-generated) that can contain many files and dirs in it.

ConnectionAdapter is an adapter for db connection. It must provide objects and links flush functions. It has ObjectAdapter and ObjectLinkAdapter. The adapter class chooses automatically from the App.Storage.DB.Connection.Adapters from the db in StorageItem.

The object can be flushed and be got from DB. In all cases it sets the "_db" link that allows to access db version of object. If _db was set, getLinkedItems() will get links not from links list but from db.
