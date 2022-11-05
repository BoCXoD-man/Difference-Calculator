import pytest
from gendiff import engine

json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yml"
result = "tests/fixtures/result"


@pytest.mark.parametrize('path1, path2, expected', [(json_1, json_2, result),
                                                    (yaml_1, yaml_2, result)])
def test_generate_diff(path1, path2, expected):
    with open(expected) as f:
        assert engine.generate_diff(path1, path2) == f.read()