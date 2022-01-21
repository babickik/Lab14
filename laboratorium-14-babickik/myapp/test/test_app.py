
import pytest
import app

def test_hello():
    got = app.hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

    
testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = app.extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert app.text_contain_word(word, sample) == expected_output


testdata3 = [
    ([1,3,5,7,9,8,6,4,2], [1,2,3,4,5,6,7,8,9]),
    ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]),
    ([5,4,6,3,7,2,8,1,9], [1,2,3,4,5,6,7,8,9]),
    ([], 'Pusta lista')
    ]

@pytest.mark.parametrize('sample, expected_output', testdata3)
def test_bouble_sort(sample, expected_output):

    assert app.sortowanie_babelkowe(sample) == expected_output