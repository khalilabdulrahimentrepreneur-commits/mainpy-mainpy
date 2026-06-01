# Examples

## Basic Usage

### Starting the API

```python
from main import app
import uvicorn

uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Making API Calls

```python
import requests

response = requests.get('http://localhost:8000/')
print(response.json())
```

## Common Scenarios

### Scenario 1: Health Check

```bash
curl http://localhost:8000/
```

Response:
```json
{
  "status": "active",
  "message": "Mindfighter E-Product initialized."
}
```

### Scenario 2: Execute Task

```bash
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"task_id": "task-001", "payload": {"action": "process"}}'
```

## Error Handling

```python
try:
    response = requests.post('http://localhost:8000/execute', json=data)
    result = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")