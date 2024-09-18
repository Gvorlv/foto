FROM python:3.12-slim

WORKDIR /opt/app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD python main.py