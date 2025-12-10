from App.DB.Adapters.ConnectionAdapter import ConnectionAdapter

class MongoAdapter(ConnectionAdapter):
    protocol_name = 'mongo'
