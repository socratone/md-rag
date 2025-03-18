#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chromadb


def main():
    chroma_client = chromadb.Client()

    # `create_collection`을 `get_or_create_collection`으로 변경하여 매번 새 컬렉션을 생성하지 않도록 함
    collection = chroma_client.get_or_create_collection(name="my_collection")

    # `add`를 `upsert`로 변경하여 동일한 문서를 매번 추가하지 않도록 함
    collection.upsert(
        documents=[
            "This is a document about pineapple",
            "This is a document about oranges",
        ],
        ids=["id1", "id2"],
    )

    results = collection.query(
        query_texts=[
            "This is a query document about florida"
        ],  # Chroma가 자동으로 임베딩을 생성함
        n_results=2,  # 반환할 결과 수
    )

    print(results)


if __name__ == "__main__":
    main()
