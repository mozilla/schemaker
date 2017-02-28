class SchemaConvert:
    def on_post(self, req, resp):
        resp.body = '{"message": "Hi"}'
