FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
ENV SRC_DIR "/application"
ENV APP_DIR ""
ENV APP_ROOT_DIR "src/app/"

RUN apt-get update && apt-get --assume-yes install make nano netcat

COPY ${APP_DIR} ${SRC_DIR}

WORKDIR ${SRC_DIR}
RUN pip install poetry==1.1.5
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-dev

WORKDIR ${APP_ROOT_DIR}

EXPOSE 8000
