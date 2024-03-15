FROM public.ecr.aws/lambda/python:3.11

ENV POETRY_HOME=/usr/local/poetry \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    COLUMNS=80

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH

COPY app.py/ ${LAMBDA_TASK_ROOT}/app.py
COPY notification_service/ ${LAMBDA_TASK_ROOT}/notification
COPY pyproject.toml ${LAMBDA_TASK_ROOT}/pyproject.toml
COPY poetry.lock ${LAMBDA_TASK_ROOT}/poetry.lock

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-ansi

CMD ["app.lambda_handler"]
