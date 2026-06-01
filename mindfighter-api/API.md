# API Documentation

## Endpoints

### Overview
The Mindfighter API provides endpoints for managing mind-related operations.

## Request/Response Format

### Headers
```
Content-Type: application/json
```

### Response Structure
```json
{
  "status": "success",
  "data": {},
  "message": "Operation completed"
}
```

## Error Handling
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error