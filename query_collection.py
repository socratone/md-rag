#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chromadb
import argparse
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
    CLI에서 쿼리 텍스트를 받아 쿼리를 수행하는 메인 함수
    """
    # 명령줄 인자 파서 생성
    parser = argparse.ArgumentParser(description="ChromaDB 컬렉션에 쿼리를 수행합니다.")
    
    # 쿼리 텍스트 인자 추가
    parser.add_argument(
        "--query", 
        type=str, 
        default="This is a query document about florida",
        help="검색할 쿼리 텍스트 (기본값: 'This is a query document about florida')"
    )
    
    # 컬렉션 이름 인자 추가
    parser.add_argument(
        "--collection", 
        type=str, 
        default="my_collection",
        help="쿼리할 컬렉션 이름 (기본값: 'my_collection')"
    )
    
    # 결과 수 인자 추가
    parser.add_argument(
        "--n_results", 
        type=int, 
        default=2,
        help="반환할 결과 수 (기본값: 2)"
    )
    
    # 인자 파싱
    args = parser.parse_args()
    
    # 쿼리 수행
    results = query_collection(
        collection_name=args.collection, 
        query_texts=[args.query], 
        n_results=args.n_results
    )

    # 결과 출력
    if results:
        print("쿼리 결과:")
        print(results)


if __name__ == "__main__":
    main()
