#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chromadb
from typing import List, Optional, Dict, Any
import os
from utils.file_utils import load_markdown_files


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
