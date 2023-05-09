import json

from src.extract_pipe import get_data, extract_data


def test_get_data():
    data = get_data()
    assert True == (data is not None)


def test_extract_data():
    f = open("mock/data.json")
    data = json.load(f)
    df = extract_data(data)
    assert True == (df is not None)
