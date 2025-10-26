FROM python:3.13-slim AS runtime
WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY services/bot/pyproject.toml /app/pyproject.toml
COPY services/bot/uv.lock /app/uv.lock
RUN pip install --no-cache-dir uv==0.4.0 \
 && uv export --frozen --no-dev -o req.txt \
 && pip install --no-cache-dir -r req.txt

ARG WHEELS_DIR=.wheels
COPY ${WHEELS_DIR}/ /wheels/
RUN pip install --no-index --find-links=/wheels questkeeper-render-sdk questkeeper-api-contracts

COPY services/bot/app ./app

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "bot.app:app", "--host", "0.0.0.0", "--port", "8000"]
