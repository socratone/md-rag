# Docker를 이용한 Hello World 프로그램

이 프로젝트는 Docker를 사용하여 간단한 Python "Hello World" 프로그램을 실행하는 예제입니다.

## 파일 구조

- `index.py`: Hello World를 출력하는 Python 스크립트
- `Dockerfile`: Docker 이미지 빌드를 위한 설정 파일
- `docker-compose.yml`: Docker Compose 설정 파일

## 사용 방법

다음 명령어를 사용하여 프로그램을 실행합니다. 실행 후 컨테이너는 자동으로 삭제됩니다:

```bash
docker-compose run --rm app
```

실행 결과로 "Hello World"가 출력됩니다.
