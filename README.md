# chip-client

chip-client is a command line interface for chip-server.
CHiP stands for [Configurable-Http-Proxy](https://github.com/jupyterhub/configurable-http-proxy)

## Basic setup

To create a virtual environment:

```
python3 -m venv
```

Then activate it:
```
source .venv/bin/activate
```

Install the requirements:
```
$ pip install -r requirements.txt
```

Run the application:
```
$ python chip-client.py --help
```

To run the tests:
```
$ pytest
```
