# Development Guidelines

## Code Standards

### Python Style Guide
- Follow PEP 8
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use type hints where appropriate

### Documentation Standards
- Add docstrings to all functions and classes
- Use Google-style docstrings
- Include examples in docstrings

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/feature-name
   ```

2. **Write code and tests**
   - Write tests before or alongside code (TDD)
   - Ensure all tests pass

3. **Commit changes**
   ```bash
   git commit -m "[TYPE] Description of changes"
   ```

4. **Push to fork**
   ```bash
   git push origin feature/feature-name
   ```

5. **Create pull request**
   - Add clear description
   - Link related issues

## Quality Checks

Before committing:
```bash
# Format code
black .

# Run linter
flake8 .

# Run tests
pytest
```

## Version Management

Use semantic versioning:
- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

Example: v1.0.0