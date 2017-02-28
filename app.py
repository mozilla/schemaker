import falcon

from api.convert import SchemaConvert


app = falcon.API()
app.add_route('/convert', SchemaConvert())
