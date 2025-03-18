# Docker를 이용한 RAG(Retrieval-Augmented Generation) 시스템

이 프로젝트는 Docker를 사용하여 ChromaDB 기반의 간단한 RAG 시스템을 구현한 예제입니다. 문서를 저장하고 쿼리할 수 있는 기능을 제공합니다.

## 파일 구조

- `create_collection.py`: 문서 컬렉션을 생성하고 샘플 문서를 추가하는 스크립트
- `query_collection.py`: 생성된 컬렉션에서 문서를 검색하는 스크립트
- `requirements.txt`: 필요한 Python 패키지 목록
- `Dockerfile`: Docker 이미지 빌드를 위한 설정 파일
- `docker-compose.yml`: Docker Compose 설정 파일

## 사용 방법

### 1. 컬렉션 생성하기

다음 명령어를 사용하여 기본 문서가 포함된 컬렉션을 생성합니다:

```bash
docker-compose run --rm create
```

### 2. 문서 검색하기

다음 명령어를 사용하여 생성된 컬렉션에서 문서를 검색합니다:

```bash
docker-compose run --rm query
```

#### 사용자 정의 쿼리 사용하기

CLI에서 직접 쿼리 텍스트를 지정하여 검색할 수 있습니다:

```bash
docker-compose run --rm query python query_collection.py --query "여기에 검색할 쿼리 텍스트 입력"
```

추가 옵션:
- `--collection`: 쿼리할 컬렉션 이름 지정 (기본값: "my_collection")
- `--n_results`: 반환할 결과 수 지정 (기본값: 2)

예시:
```bash
docker-compose run --rm query python query_collection.py --query "florida의 날씨는 어떤가요?" --n_results 3
```

## 기술 스택

- Python 3.9
- ChromaDB: 벡터 데이터베이스
- Docker: 컨테이너화

## 데이터 저장

모든 데이터는 `./db` 디렉토리에 저장되며, Docker 컨테이너와 호스트 시스템 간에 볼륨으로 공유됩니다.
