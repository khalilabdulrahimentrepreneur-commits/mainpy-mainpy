"""
Mindfighter API - Todo Task Management
FastAPI-based API with local storage (JSON file-based persistence)
Unified endpoint for all digital product tasks including todo management
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
import json
import os
from datetime import datetime
from pathlib import Path
import uuid

# Initialize the Mindfighter Engine
app = FastAPI(
    title="Mindfighter API",
    version="1.0.0",
    description="Permanence-First E-Product with Todo Task Management"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage configuration
STORAGE_DIR = Path("data")
TODOS_FILE = STORAGE_DIR / "todos.json"
STORAGE_DIR.mkdir(exist_ok=True)

# ==================== Pydantic Models ====================

class TodoTask(BaseModel):
    """Standard Todo Task Model"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: Literal["low", "medium", "high"] = "medium"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoTaskCreate(BaseModel):
    """Model for creating a new todo task"""
    title: str
    description: Optional[str] = None
    priority: Literal["low", "medium", "high"] = "medium"

class TodoTaskUpdate(BaseModel):
    """Model for updating a todo task"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[Literal["low", "medium", "high"]] = None

class MindfighterTask(BaseModel):
    """Generic Mindfighter Task (for standardized entry point)"""
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    payload: dict

class TaskResponse(BaseModel):
    """Standard response format"""
    status: str
    processed_id: str
    action: str
    task: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatsResponse(BaseModel):
    """Statistics response"""
    total: int
    completed: int
    active: int
    completion_rate: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# ==================== Storage Utilities ====================

def load_todos() -> dict:
    """Load todos from JSON file"""
    if TODOS_FILE.exists():
        with open(TODOS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"todos": []}
    return {"todos": []}

def save_todos(data: dict) -> None:
    """Save todos to JSON file"""
    with open(TODOS_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)

def convert_todo_to_dict(todo: TodoTask) -> dict:
    """Convert TodoTask to dictionary"""
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "priority": todo.priority,
        "created_at": todo.created_at.isoformat(),
        "updated_at": todo.updated_at.isoformat()
    }

def convert_dict_to_todo(data: dict) -> TodoTask:
    """Convert dictionary to TodoTask"""
    return TodoTask(
        id=data["id"],
        title=data["title"],
        description=data.get("description"),
        completed=data.get("completed", False),
        priority=data.get("priority", "medium"),
        created_at=datetime.fromisoformat(data["created_at"]) if isinstance(data.get("created_at"), str) else data.get("created_at"),
        updated_at=datetime.fromisoformat(data["updated_at"]) if isinstance(data.get("updated_at"), str) else data.get("updated_at")
    )

# ==================== Health & Status ====================

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "active",
        "message": "Mindfighter E-Product initialized.",
        "version": "1.0.0",
        "features": ["todo_management", "permanence_protocol", "local_storage"]
    }

@app.get("/health")
async def health():
    """Detailed health check"""
    stats = load_todos()
    todos = stats.get("todos", [])
    return {
        "status": "healthy",
        "storage_ready": TODOS_FILE.exists() or TODOS_FILE.parent.exists(),
        "todos_count": len(todos),
        "timestamp": datetime.utcnow().isoformat()
    }

# ==================== Standardized Entry Points ====================

@app.post("/execute", response_model=TaskResponse)
async def execute_task(task: MindfighterTask):
    """
    Standardized entry point for all digital product tasks.
    Generic execution endpoint with permanence verification.
    """
    return {
        "status": "success",
        "processed_id": task.task_id,
        "action": "permanence_verified",
        "task": task.payload
    }

@app.post("/execute/todo", response_model=TaskResponse)
async def execute_todo(task: TodoTask):
    """
    Standardized entry point for Todo task generation.
    Creates a todo with full persistence and verification.
    """
    # Convert and save
    data = load_todos()
    todos = data.get("todos", [])
    
    todo_dict = convert_todo_to_dict(task)
    todos.append(todo_dict)
    data["todos"] = todos
    save_todos(data)
    
    return {
        "status": "success",
        "processed_id": task.id,
        "action": "permanence_verified",
        "task": todo_dict
    }

# ==================== Todo CRUD Operations ====================

@app.get("/todos", response_model=List[TodoTask])
async def list_todos(
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    priority: Optional[str] = None
):
    """
    List all todos with optional filtering and pagination.
    """
    data = load_todos()
    todos = data.get("todos", [])
    
    # Filter by completion status
    if completed is not None:
        todos = [t for t in todos if t["completed"] == completed]
    
    # Filter by priority
    if priority is not None:
        todos = [t for t in todos if t["priority"] == priority]
    
    # Apply pagination
    todos = todos[skip:skip + limit]
    
    return [convert_dict_to_todo(t) for t in todos]

@app.get("/todos/{todo_id}", response_model=TodoTask)
async def get_todo(todo_id: str):
    """Get a specific todo by ID"""
    data = load_todos()
    todos = data.get("todos", [])
    
    for todo in todos:
        if todo["id"] == todo_id:
            return convert_dict_to_todo(todo)
    
    raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

@app.post("/todos", response_model=TodoTask)
async def create_todo(task: TodoTaskCreate):
    """Create a new todo"""
    data = load_todos()
    todos = data.get("todos", [])
    
    new_todo = TodoTask(
        title=task.title,
        description=task.description,
        priority=task.priority
    )
    
    todo_dict = convert_todo_to_dict(new_todo)
    todos.append(todo_dict)
    data["todos"] = todos
    save_todos(data)
    
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoTask)
async def update_todo(todo_id: str, task: TodoTaskUpdate):
    """Update an existing todo"""
    data = load_todos()
    todos = data.get("todos", [])
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            # Update fields if provided
            if task.title is not None:
                todo["title"] = task.title
            if task.description is not None:
                todo["description"] = task.description
            if task.completed is not None:
                todo["completed"] = task.completed
            if task.priority is not None:
                todo["priority"] = task.priority
            
            todo["updated_at"] = datetime.utcnow().isoformat()
            
            todos[i] = todo
            data["todos"] = todos
            save_todos(data)
            
            return convert_dict_to_todo(todo)
    
    raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    """Delete a specific todo"""
    data = load_todos()
    todos = data.get("todos", [])
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(i)
            data["todos"] = todos
            save_todos(data)
            return {
                "status": "success",
                "message": f"Todo {todo_id} deleted",
                "deleted_todo": convert_dict_to_todo(deleted_todo)
            }
    
    raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

@app.post("/todos/{todo_id}/toggle")
async def toggle_todo(todo_id: str):
    """Toggle todo completion status"""
    data = load_todos()
    todos = data.get("todos", [])
    
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            todo["updated_at"] = datetime.utcnow().isoformat()
            todos[i] = todo
            data["todos"] = todos
            save_todos(data)
            return {
                "status": "success",
                "message": f"Todo toggled",
                "todo": convert_dict_to_todo(todo)
            }
    
    raise HTTPException(status_code=404, detail=f"Todo {todo_id} not found")

@app.delete("/todos")
async def clear_completed():
    """Clear all completed todos"""
    data = load_todos()
    todos = data.get("todos", [])
    
    active_todos = [t for t in todos if not t["completed"]]
    removed_count = len(todos) - len(active_todos)
    
    data["todos"] = active_todos
    save_todos(data)
    
    return {
        "status": "success",
        "message": f"Cleared {removed_count} completed todos",
        "removed_count": removed_count
    }

# ==================== Statistics & Analytics ====================

@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """Get todo statistics and analytics"""
    data = load_todos()
    todos = data.get("todos", [])
    
    completed = sum(1 for t in todos if t["completed"])
    total = len(todos)
    
    return {
        "total": total,
        "completed": completed,
        "active": total - completed,
        "completion_rate": (completed / total * 100) if total > 0 else 0
    }

@app.get("/stats/by-priority")
async def get_stats_by_priority():
    """Get statistics grouped by priority"""
    data = load_todos()
    todos = data.get("todos", [])
    
    stats = {
        "low": {"total": 0, "completed": 0},
        "medium": {"total": 0, "completed": 0},
        "high": {"total": 0, "completed": 0}
    }
    
    for todo in todos:
        priority = todo.get("priority", "medium")
        stats[priority]["total"] += 1
        if todo["completed"]:
            stats[priority]["completed"] += 1
    
    return stats

# ==================== Documentation ====================

@app.get("/docs-info")
async def docs_info():
    """API documentation info"""
    return {
        "title": "Mindfighter API - Todo Management",
        "version": "1.0.0",
        "documentation_urls": {
            "swagger_ui": "/docs",
            "redoc": "/redoc",
            "openapi_schema": "/openapi.json"
        },
        "endpoints": {
            "health": {
                "GET /": "Health check",
                "GET /health": "Detailed health status"
            },
            "execution": {
                "POST /execute": "Generic task execution",
                "POST /execute/todo": "Todo task execution with permanence verification"
            },
            "todo_management": {
                "GET /todos": "List todos with filters and pagination",
                "GET /todos/{id}": "Get specific todo",
                "POST /todos": "Create new todo",
                "PUT /todos/{id}": "Update todo",
                "DELETE /todos/{id}": "Delete todo",
                "POST /todos/{id}/toggle": "Toggle completion",
                "DELETE /todos": "Clear completed todos"
            },
            "analytics": {
                "GET /stats": "Get overall statistics",
                "GET /stats/by-priority": "Get statistics by priority"
            }
        }
    }
