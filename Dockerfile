FROM python:3.10-alpine3.14

RUN apk add --no-cache gcc libc-dev linux-headers build-base libffi-dev curl && \
	python -m pip install --upgrade pip

ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /whosoncall
COPY ./pyproject.toml /whosoncall/.
COPY ./poetry.lock /whosoncall/.

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /whosoncall

CMD ["python", "main.py"]
