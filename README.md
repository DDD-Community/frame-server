# frame-server

## Start developing

### 1. Install poetry
- Detailed instruction [here](https://python-poetry.org/docs/#installation).
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### 2. Install deps
```sh
poetry install --dev
```

### 3. Run server
```sh
# using poetry
poetry run ./manage.py runserver 0.0.0.0:8000

# using docker
docker build -t frame-server .
docker run -d -p 8000:8000 frame-server:latest
docker run -it -p 8000:8000 frame-server:latest bash
```


## TODO
- replace drf-jwt package (it's deprecated)
