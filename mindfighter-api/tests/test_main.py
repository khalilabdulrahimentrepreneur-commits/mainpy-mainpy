#!/usr/bin/env python
"""Basic test suite for main.py"""

import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):
    """Test cases for main module"""
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "active")
    
    def test_execute_endpoint(self):
        """Test execute endpoint"""
        payload = {
            "task_id": "test-001",
            "payload": {"action": "test"}
        }
        response = client.post("/execute", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")

if __name__ == '__main__':
    unittest.main()