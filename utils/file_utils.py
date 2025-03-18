import os
import glob
from typing import List, Tuple


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

        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없음: '{file_path}', 오류: {e}")
        except PermissionError as e:
            print(f"파일 접근 권한 오류: '{file_path}', 오류: {e}")
        except IOError as e:
            print(f"파일 읽기/쓰기 오류: '{file_path}', 오류: {e}")
        except UnicodeDecodeError as e:
            print(f"파일 인코딩 오류: '{file_path}', 오류: {e}")

    print(f"총 {len(documents)}개의 마크다운 파일을 읽었습니다.")
    return documents, ids
