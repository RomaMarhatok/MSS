FROM python:3.10

WORKDIR /back
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERCTION=1
RUN echo ls
COPY ./pyproject.toml ./

RUN pip install -U pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install
COPY ./MSSProject ./
COPY ./MSSProject/entrypoint.sh  /back/entrypoint.sh
RUN chmod +x /back/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["sh","/back/entrypoint.sh" ]
