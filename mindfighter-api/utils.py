# Utility Functions

"""Common utility functions for the mindfighter-api"""

def format_response(status, data=None, message=None):
    """
    Format API response
    
    Args:
        status (str): Response status ('success' or 'error')
        data (dict, optional): Response data
        message (str, optional): Response message
        
    Returns:
        dict: Formatted response
    """
    return {
        'status': status,
        'data': data or {},
        'message': message or ''
    }

def log_event(level, message):
    """
    Log an event
    
    Args:
        level (str): Log level ('info', 'warning', 'error')
        message (str): Log message
    """
    print(f"[{level.upper()}] {message}")