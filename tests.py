import pytest

from mypkg.fibonacci import fibonacci

def test_fib_10():
	assert(fibonacci(10) == 55)

def test_fib_not_20():
	assert(fibonacci(20) != 20)	
© 2021 GitHub, Inc.
