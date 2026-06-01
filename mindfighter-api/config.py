# Configuration

## Environment Variables

```
API_PORT=8000
API_HOST=0.0.0.0
DEBUG=False
LOG_LEVEL=INFO
```

## Configuration File

Create a `config.py` file to manage settings:

```python
import os

class Config:
    """Base configuration"""
    DEBUG = os.getenv('DEBUG', False)
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    API_PORT = int(os.getenv('API_PORT', 8000))
    API_HOST = os.getenv('API_HOST', '0.0.0.0')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = 'WARNING'
```

## Usage

```python
from config import Config, DevelopmentConfig

# Use appropriate config based on environment
config = DevelopmentConfig()
```