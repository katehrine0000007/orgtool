After run app will load the list of object in program. It stores them in Namespace. You can pass your own namespaces by setting objects.namespaces.

### Globals

LoadedObject will call mount() function of each class. Class can override it to set a property in Wrap.

Wrap is an __init__ file in App dir: it wraps current View and allows to get and set global classes.
