FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y redis-server && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY conf/redis.conf /etc/redis/redis.conf
COPY app/ /app/

EXPOSE 8000

CMD ["/bin/bash", "-c", "redis-server /etc/redis/redis.conf & python /app/app.py"]