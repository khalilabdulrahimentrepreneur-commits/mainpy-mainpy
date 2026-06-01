# Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/khalilabdulrahimentrepreneur-commits/mainpy-mainpy.git
cd mainpy-mainpy/mindfighter-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file with your configuration settings.

### 5. Run the Application
```bash
uvicorn main:app --reload
```

## Troubleshooting

- Ensure Python version is 3.8+
- Verify all dependencies are installed
- Check environment variables are set correctly