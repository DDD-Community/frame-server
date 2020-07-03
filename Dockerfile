FROM python:3.8-slim

WORKDIR /code

# copy poetry files
ENV PATH="/root/.poetry/bin:$PATH"
COPY poetry.lock pyproject.toml /code/

# install system packages
RUN set -ex \
    && apt-get update \
    && apt-get install -y \
        curl \
        build-essential \
        libpq-dev

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version=1.0.9 \
    && poetry config virtualenvs.create false

# install poetry packages
RUN poetry install --no-dev

# copy source codes
COPY . ./

# run gunicorn
CMD poetry run gunicorn frame.wsgi:application --bind 0.0.0.0:$PORT
