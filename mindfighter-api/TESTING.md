# Testing Guide

## Running Tests

```bash
pytest
```

## Test Structure

Tests are located in the `tests/` directory and follow the naming convention `test_*.py`.

## Writing Tests

```python
import unittest
from main import MyFunction

class TestMyFunction(unittest.TestCase):
    def test_success(self):
        result = MyFunction()
        self.assertEqual(result, expected_value)
    
    def test_error(self):
        with self.assertRaises(Exception):
            MyFunction()
```

## Coverage

Generate coverage reports:
```bash
pytest --cov=mindfighter_api tests/
```

Target: Maintain >80% code coverage