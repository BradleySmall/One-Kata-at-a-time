import pytest

# update name of test_xxx program or remove name completely to run all test_*.py
if __name__ == '__main__':
    pytest.main(["-v", "--tb=short", "test_stringcalc.py"])
#  pytest.main(["-v", "--tb=short", "test_fizzbuzz.py"])
#  pytest.main(["-v", "--tb=short", "test_factor.py"])
#  pytest.main(["-v", "--tb=short", "test_skel.py"])
#  pytest.main(["-v", "--tb=short"])
