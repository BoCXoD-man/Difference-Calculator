import pytest
from gendiff import engine

json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yml"
result = "tests/fixtures/result"


formats = ['stylish', 'plain', 'json']

@pytest.mark.parametrize('path1, path2, format_name, expected', [(json_1, json_2, formats[0], result),
                                                                 (yaml_1, yaml_2, formats[0], result)])
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as f:
        assert gen_diff.generate_diff(path1, path2, format_name) == f.read()