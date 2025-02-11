FROM python:3.8

ENV user=gamja
ENV port=8000

RUN adduser --disabled-password $user
WORKDIR /app

ADD ./deploy /app
RUN apt-get update && apt-get install -y gcc
RUN pip install -r requirements.txt

RUN gcc /app/flag.c -o /flag \
    && chmod 111 /flag && rm /app/flag.c

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]
