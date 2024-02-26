from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"
word = "Python"


def test_counter():
    assert count_ocurrences(path, word) == 1639
