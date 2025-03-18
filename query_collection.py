#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chromadb
from typing import List, Dict, Any


def query_collection(
    collection_name: str = "my_collection",
    query_texts: List[str] = None,
    n_results: int = 2,
) -> Dict[str, Any]:
    """
    컬렉션에서 쿼리를 수행하는 함수

    Args:
        collection_name: 쿼리할 컬렉션 이름
        query_texts: 쿼리 텍스트 리스트
        n_results: 반환할 결과 수

    Returns:
        쿼리 결과 딕셔너리
    """
    # 기본값 설정
    if query_texts is None:
        query_texts = [""]

    # ChromaDB 클라이언트 생성 - ./db 폴더에서 데이터 읽기
    db_path = "./db"

    # PersistentClient 사용하여 지정된 경로에서 데이터 읽기
    chroma_client = chromadb.PersistentClient(path=db_path)

    try:
        # 컬렉션 가져오기
        collection = chroma_client.get_collection(name=collection_name)

        # 쿼리 수행
        results = collection.query(
            query_texts=query_texts,
            n_results=n_results,
        )

        return results
    except ValueError as e:
        # 컬렉션이 존재하지 않는 경우
        if "Collection" in str(e) and "does not exist" in str(e):
            print(
                f"'{collection_name}' 컬렉션이 존재하지 않습니다. create_collection.py를 먼저 실행해주세요."
            )
        else:
            print(f"쿼리 값 오류: {e}")
        return {}
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
        return {}


def main():
    """
    기본 쿼리를 수행하는 메인 함수
    """
    # 기본 쿼리 텍스트 정의
    default_query = ["This is a query document about florida"]

    # 쿼리 수행
    results = query_collection(
        collection_name="my_collection", query_texts=default_query, n_results=2
    )

    # 결과 출력
    if results:
        print("쿼리 결과:")
        print(results)


if __name__ == "__main__":
    main()
