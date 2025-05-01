from app import topla 
from app import cikartma 
from app import carpma 
from app import bolme 

def test_topla():
	assert topla(2,3) == 5
	assert topla(-1,1) == 0
def test_cikartma():
	assert cikartma(2,3) == -1
def test_carpma():
	assert carpma(2,3) == 6
def test_bolme():
	assert bolme(3,3) == 1 
