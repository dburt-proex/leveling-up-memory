from app.indexer import rebuild_index


def test_rebuild_index_runs():
    result = rebuild_index()
    assert "count" in result
    assert "types" in result
    assert isinstance(result["count"], int)
