FROM python:3.8-buster as builder

WORKDIR /app

RUN pip3 install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root



FROM python:3.8-slim-buster as runner

WORKDIR /app

RUN pip3 install --upgrade pip

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/src /usr/local/src

COPY pyproject.toml poetry.lock /app/
COPY attach_ext /app/attach_ext

RUN pip3 install --no-deps . && rm -rf /app
# RUN poetry install --no-dev && rm -rf /app

ENTRYPOINT [ "/usr/local/bin/attach-ext" ]