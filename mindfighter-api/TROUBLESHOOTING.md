# Troubleshooting Guide

## Common Issues

### Issue: Module Not Found Error

**Problem:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Port Already in Use

**Problem:** `Address already in use`

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
uvicorn main:app --port 8001
```

### Issue: Connection Refused

**Problem:** `Connection refused` when calling API

**Solution:**
- Ensure the server is running
- Check if port 8000 is correct
- Check firewall settings

## Debugging

### Enable Debug Mode

```python
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
```

Or use environment variable:
```bash
export DEBUG=True
```

### Check Logs

```bash
tail -f logs/app.log
```

## Support

If issues persist:
1. Check the troubleshooting guide
2. Review API.md for endpoint documentation
3. Open an issue on GitHub
4. Contact the maintainers