from strcalculator import add
import pytest

def test_two_numbers():
	assert add('1,2') == 3

def test_many_numbers():
	assert add('1,2,3') == 6
	assert add('1,2,3,4,5') == 15
	assert add('1,2,3,4,5,10') == 25

def test_new_lines():
	assert add('1\n2,3') == 6

def test_different_dilimeters():
	assert add( '//;\n1;2') == 3

def test_negative_numbers():
	with pytest.raises(Exception):
		assert add('1,-2,3')

def test_bigger_thousand():
	assert add('1,2,5,1001') == 8

def test_dilimiter_any_length():
	assert add('//[***]\n1***2***3') == 6

def test_multiple_dilimiters():
	assert add('//[*][%]\n1*2%3') == 6

def test_multiple_neg():
    with pytest.raises(Exception):
	    assert add('-1,-2')
