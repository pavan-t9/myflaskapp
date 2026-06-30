FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

ENV PORT=5000

EXPOSE 5000

CMD ["python","app.py"]

