
  
  

# Test automation

  

I have used Python and pytest.

  

## Installation

  

Use pyenv, install deps.

  

    $ python3 -m venv .venv
    
    $ source .venv/bin/activate
    
    $ pip3 install -r requirements.txt

  

## Test automation

    (.venv) ~/source/charles $ python3 -m pytest tests.py -v
    
    ==================================================================== test session starts =====================================================================
    
        platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0 -- /Users/d/source/charles/.venv/bin/python3
        
        cachedir: .pytest_cache
        
        rootdir: /Users/d/source/charles
        
        collected 10 items
        
          
        
        tests.py::test_shares_to_trade_matches_expected[IBM-20-10-150--66] PASSED [ 10%]
        
        tests.py::test_shares_to_trade_matches_expected[MSFT-20-20-90-0] PASSED [ 20%]
        
        tests.py::test_shares_to_trade_matches_expected[ORCL-20-30-220-46] PASSED [ 30%]
        
        tests.py::test_shares_to_trade_matches_expected[AAPL-20-20-450-0] PASSED [ 40%]
        
        tests.py::test_shares_to_trade_matches_expected[HD-20-20-70-0] PASSED [ 50%]
        
        tests.py::test_too_few_shares_buy PASSED [ 60%]
        
        tests.py::test_too_many_shares_sell PASSED [ 70%]
        
        tests.py::test_20_percent_no_trade PASSED [ 80%]
        
        tests.py::test_fractional_shares_round_up PASSED [ 90%]
        
        tests.py::test_invalid_shareprice_is_rejected PASSED [100%]
        
          
        
        ===================================================================== 10 passed in 0.01s =====================================================================


