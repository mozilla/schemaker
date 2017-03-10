Schemaker
=========

The "schema service" is a collection of tools, including a web service and some
glue code that is used to validate incoming telemetry and other data against
the specified schema that the data is supposed to honor, and support the
efforts of converting data from the ingested format (initially JSON) to the
desired storage format (initially Parquet).

[![CircleCI](https://img.shields.io/circleci/project/github/mozilla/schemaker/master.svg)](https://circleci.com/gh/mozilla/schemaker)
[![codecov](https://codecov.io/gh/mozilla/schemaker/branch/master/graph/badge.svg)](https://codecov.io/gh/mozilla/schemaker)

Development Setup
-----------------

This application uses Docker for local development. Please make sure to
[install Docker](https://docs.docker.com/mac/) and
[Docker Compose](https://docs.docker.com/compose/install/).

To start the application, run:

    make up

Run the tests
-------------

Run the tests using the following command on your computer:

    make test

This will spin up a Docker container to run the tests, so please set up
the development setup first.


API Endpoints
=============

### `POST /convert`

Converts the provided schema to the requested output schema.

Query parameters:

* `output` (required): The requested output format. Currently the only format
  supported is 'parquet-mr'.

Provide the input schema as the body of the POST request.

Example output:
```
{
  "parquet-mr": "<full output of schema>"
}
```

