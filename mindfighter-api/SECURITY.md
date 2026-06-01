# Security Guidelines

## Best Practices

### Input Validation
- Validate all user inputs
- Use Pydantic models for request validation
- Sanitize data before processing

### Authentication
- Use secure authentication methods
- Implement JWT or OAuth2
- Never hardcode credentials

### Data Protection
- Use HTTPS for all communications
- Encrypt sensitive data at rest
- Hash passwords securely

### Dependencies
- Keep dependencies up to date
- Audit for known vulnerabilities
- Use `pip-audit` to check for issues

## Environment Variables

Never commit sensitive data:
```bash
# .env (not committed)
DATABASE_URL=...
API_SECRET_KEY=...
```

## Security Checklist

- [ ] All inputs are validated
- [ ] Sensitive data is protected
- [ ] Dependencies are up to date
- [ ] No hardcoded credentials
- [ ] HTTPS is enforced
- [ ] Logging doesn't expose secrets