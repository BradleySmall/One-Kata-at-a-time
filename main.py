import pytest

# update name of test_xxx program or remove name completely to run all test_*.py
if __name__ == '__main__':
    pytest.main(["-v", "--tb=short","stringcalc_test.py"])
#  pytest.main(["-v", "--tb=short", "fizzbuzz_test.py"])
#  pytest.main(["-v", "--tb=short", "factor_test.py"])
#  pytest.main(["-v", "--tb=short", "skel_test.py"])
#  pytest.main(["-v", "--tb=short"])
