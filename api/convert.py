import json
import os
import subprocess
import tempfile

import falcon


JSONSCHEMA_PARQUET_PATH = os.environ.get('JSONSCHEMA_PARQUET_PATH')


def validate_content_type(req, resp, resource, params):
    if (not req.content_type or
            req.content_type.split(';')[0] != 'application/json'):
        raise falcon.HTTPBadRequest(
            'Bad request', 'Content type must be `application/json`.')


class SchemaConvert:
    @falcon.before(validate_content_type)
    def on_post(self, req, resp):
        if req.get_param('output') == 'parquet-mr':
            json_schema = req.bounded_stream.read()

            file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
            try:
                file.write(json_schema)
                file.close()

                output = subprocess.check_output(
                    [JSONSCHEMA_PARQUET_PATH,
                     'parquet',
                     '--deref',
                     file.name],
                )
                resp.body = json.dumps({'parquet-mr': output.decode()})

            finally:
                os.remove(file.name)

        else:
            raise falcon.HTTPBadRequest(
                'Bad request', 'Invalid or missing output parameter.')
