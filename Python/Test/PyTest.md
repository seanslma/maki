# PyTest

## run from vscode terminal 
```
pytest .
```

## run test on file
```
pytest test_myfile.py -sv #print output and test name
pytest test_myfile.py -sv -k "get"  #run test method matches 'get'
pytest Test_myfile.py -sv -m "skip or login" #run test with specific mark or category, either
pytest Test_myfile.py -sv -m "skip and login" #run test with specific mark or category, both, not can be used as well
```

## skip test method
https://docs.pytest.org/en/latest/how-to/skipping.html#skipping-test-functions
```
@pytest.mark.skip(reason="no way of currently testing this")
def test_my_method():
...

#or skip during test
def test_my_method():
    if not valid_config():
        pytest.skip("unsupported configuration")
```

## skip the whole test module
```
if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```

## skip test module if import fails
https://docs.pytest.org/en/stable/reference/reference.html#pytest-importorskip-ref
```
docutils = pytest.importorskip("docutils")
```
