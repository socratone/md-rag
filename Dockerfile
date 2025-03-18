# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /app/

# 컨테이너가 시작될 때 index.py 실행
CMD ["python", "index.py"]
