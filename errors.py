class InvaildID3(Exception):
    """
    지원되지 않는 ID3 태그 버전이거나 태그를 찾을 수 없을 때 발생하는 오류입니다.
    이 오류가 발생하면 Searcher.search_with_info 를 통해 수동으로 검색하세요.
    """
