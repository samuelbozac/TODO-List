FROM python:3.12-alpine as req-stage

WORKDIR /tmp

RUN pip install "poetry==1.8.5"

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt

FROM req-stage

WORKDIR /app

COPY --from=req-stage /tmp/requirements.txt /app/requirements.txt

RUN addgroup -S app && adduser -S app -G app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install fastapi-pagination

COPY ./src /app

RUN chown -R app:app /app

USER app

CMD uvicorn --host 0.0.0.0 --port 8000 --forwarded-allow-ips='*' --proxy-headers --reload --lifespan on main:app --limit-max-requests 10000
