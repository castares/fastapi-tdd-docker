# pull official base image
FROM python:3.9.6-slim-bullseye

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
  PYTHONUNBUFFERED 1 \
  POETRY_VERSION=1.1.6

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip \
  && pip install "poetry==1.1.6"
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-interaction --no-ansi $(test "$ENVIRONMENT" == prod && echo "--no-dev")

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
