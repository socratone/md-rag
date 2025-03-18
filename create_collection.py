#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chromadb
from typing import List, Optional, Dict, Any, Tuple
import os
import glob


def load_markdown_files(docs_dir: str = "./docs") -> Tuple[List[str], List[str]]:
    """
    지정된 디렉토리에서 모든 마크다운(.md) 파일을 읽어 내용과 ID를 반환하는 함수

    Args:
        docs_dir: 마크다운 파일이 있는 디렉토리 경로 (기본값: "./docs")

    Returns:
        Tuple[List[str], List[str]]: 문서 내용 리스트와 문서 ID 리스트의 튜플
    """
    # 디렉토리가 존재하는지 확인
    if not os.path.exists(docs_dir):
        raise FileNotFoundError(f"디렉토리가 존재하지 않습니다: {docs_dir}")

    # 모든 마크다운 파일 경로 가져오기
    md_files = glob.glob(os.path.join(docs_dir, "*.md"))

    if not md_files:
        print(f"경고: {docs_dir} 디렉토리에 마크다운 파일이 없습니다.")
        return [], []

    documents = []  # 문서 내용을 저장할 리스트
    ids = []  # 문서 ID를 저장할 리스트

    # 각 마크다운 파일 읽기
    for file_path in md_files:
        try:
            # 파일 이름을 ID로 사용 (확장자 제외)
            file_id = os.path.basename(file_path).replace(".md", "")

            # 파일 내용 읽기
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            # 내용과 ID 추가
            documents.append(content)
            ids.append(file_id)

        except Exception as e:
            print(f"파일 '{file_path}' 읽기 오류: {e}")

    print(f"총 {len(documents)}개의 마크다운 파일을 읽었습니다.")
    return documents, ids


def create_collection(
    collection_name: str = "my_collection",
    documents: Optional[List[str]] = None,
    ids: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    컬렉션을 생성하고 문서를 추가하는 함수

    Args:
        collection_name: 생성할 컬렉션 이름
        documents: 추가할 문서 리스트
        ids: 문서에 대응하는 ID 리스트

    Returns:
        생성된 컬렉션 정보
    """
    # ChromaDB 클라이언트 생성 - 데이터를 ./db 폴더에 저장
    db_path = "./db"

    # db 디렉토리가 없으면 생성
    os.makedirs(db_path, exist_ok=True)

    # PersistentClient 사용하여 지정된 경로에 데이터 저장
    chroma_client = chromadb.PersistentClient(path=db_path)

    # 컬렉션 생성 또는 가져오기
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # 문서가 제공된 경우 추가
    if documents and ids:
        if len(documents) != len(ids):
            raise ValueError("documents와 ids의 길이가 일치해야 합니다.")

        # upsert를 사용하여 동일한 ID의 문서가 있으면 업데이트
        collection.upsert(
            documents=documents,
            ids=ids,
        )
        print(f"컬렉션 '{collection_name}'에 {len(documents)}개 문서가 추가되었습니다.")
    else:
        print(f"컬렉션 '{collection_name}'이 생성되었습니다.")

    # 컬렉션 정보 반환
    return {"name": collection_name, "count": collection.count()}


def main() -> None:
    """
    docs 디렉토리의 마크다운 파일로 컬렉션을 생성하는 메인 함수
    """
    try:
        # docs 디렉토리에서 마크다운 파일 불러오기
        documents, ids = load_markdown_files()

        if not documents:
            print("문서가 없어 기본 예제 문서를 사용합니다.")
            # 기본 문서 및 ID 정의
            documents = [
                "This is a document about pineapple",
                "This is a document about oranges",
            ]
            ids = ["id1", "id2"]

        # 컬렉션 생성 및 문서 추가
        result = create_collection(
            collection_name="my_collection",
            documents=documents,
            ids=ids,
        )
        print(f"컬렉션 정보: {result}")
    except Exception as e:
        print(f"컬렉션 생성 중 오류 발생: {e}")


if __name__ == "__main__":
    main()
