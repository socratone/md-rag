# 🔍 ChromaDB 기반 RAG(Retrieval-Augmented Generation) 시스템

이 프로젝트는 ChromaDB를 활용한 간단한 RAG(Retrieval-Augmented Generation) 시스템을 구현한 예제입니다. 마크다운 문서를 벡터 데이터베이스에 저장하고 의미적 검색을 수행할 수 있습니다.

## 🌟 주요 기능

- **문서 저장**: 마크다운(.md) 파일을 ChromaDB 컬렉션에 저장
- **의미 기반 검색**: 자연어 쿼리를 사용하여 관련 문서 검색
- **Docker 지원**: 컨테이너화된 환경에서 쉽게 실행 가능

## 📋 시스템 요구사항

- Python 3.9 이상
- Docker 및 Docker Compose (컨테이너 실행 시)

## 🔧 설치 방법

```bash
# Docker 이미지 빌드
docker-compose build
```

## 🚀 사용 방법

### 1. 문서 준비

`docs` 디렉토리에 마크다운(.md) 파일을 저장합니다. 이 파일들이 벡터 데이터베이스에 저장될 문서입니다.

### 2. 컬렉션 생성

```bash
docker-compose run --rm create
```

### 3. 문서 검색

```bash
# 기본 쿼리 사용
docker-compose run --rm query

# 사용자 정의 쿼리 사용
docker-compose run --rm query python query_collection.py --query "검색할 내용" --n_results 3
```

## ⚙️ 주요 설정 옵션

### 컬렉션 생성 (`create_collection.py`)

- 기본 컬렉션 이름: `my_collection`
- 문서 디렉토리: `./docs`

### 문서 검색 (`query_collection.py`)

- `--query`: 검색할 쿼리 텍스트 (기본값: "This is a query document about florida")
- `--collection`: 검색할 컬렉션 이름 (기본값: "my_collection")
- `--n_results`: 반환할 결과 수 (기본값: 2)

## 🔍 예제

```bash
# 특정 주제에 대한 문서 검색
docker-compose run --rm query python query_collection.py --query "인공지능의 윤리적 문제" --n_results 5

# 영어 쿼리 예제
docker-compose run --rm query python query_collection.py --query "ethical issues in artificial intelligence" --n_results 3
```

## 📚 기술 스택

- **Python 3.9**: 기본 프로그래밍 언어
- **ChromaDB**: 벡터 데이터베이스 및 임베딩 저장소
- **Docker**: 애플리케이션 컨테이너화
