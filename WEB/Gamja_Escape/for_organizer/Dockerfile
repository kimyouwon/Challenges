FROM python:3.8

# 환경변수 설정
ENV user=gamja
ENV port=8000

# 사용자 추가 및 작업 디렉토리 설정
RUN adduser --disabled-password $user
WORKDIR /app

# 애플리케이션 파일 복사 및 Python 패키지 설치
ADD ./deploy /app
RUN apt-get update && apt-get install -y gcc
RUN pip install -r requirements.txt

# 플래그 파일 추가 및 권한 설정
RUN gcc /app/flag.c -o /flag \
    && chmod 111 /flag && rm /app/flag.c

# Flask 앱 실행을 위한 설정
USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]
