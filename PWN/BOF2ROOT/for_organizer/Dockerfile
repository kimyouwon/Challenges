# 베이스 이미지 설정
FROM ubuntu:24.04

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    socat \
    bash \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /home/bof2root

# 문제 파일 및 플래그 복사
COPY BOF2ROOT /home/bof2root/BOF2ROOT
COPY flag /home/bof2root/flag

# 사용자 및 권한 설정
RUN useradd -m challenger \
    && chown -R challenger:challenger /home/bof2root \
    && chmod 400 /home/bof2root/flag \
    && chmod +x /home/bof2root/BOF2ROOT

# 사용자로 실행
USER challenger

# 포트 노출 및 문제 실행
EXPOSE 6001
CMD ["socat", "-v","TCP-LISTEN:6001,reuseaddr,fork", "EXEC:/home/bof2root/BOF2ROOT"]
