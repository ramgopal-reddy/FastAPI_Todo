# FastAPI Todo CRUD Application

A simple yet powerful FastAPI application demonstrating CRUD operations with Pydantic validation and proper HTTP status codes.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd FastAPI
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API:**
   - API Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - Alternative Docs: `http://localhost:8000/redoc`

## 📁 Project Structure

```
FastAPI/
├── main.py              # Main application entry point
├── students.json        # JSON database file
├── models/
│   └── Todo.py          # Pydantic model for data validation
└── routes/
    └── TodoRoute.py     # API routes for CRUD operations
```

## 🛠️ API Endpoints

### Base Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | `/` | Server health check | 200 |
| GET | `/api/v1/` | Get all todos | 200 |

### Todo Operations

#### Create Todo
```http
POST /api/v1/create
Content-Type: application/json

{
  "title": "Learn FastAPI",
  "desc": "Complete CRUD tutorial",
  "isComplete": false
}
```

**Response:**
```json
{
  "message": "Todo Created Successfully",
  "data": {
    "title": "Learn FastAPI",
    "desc": "Complete CRUD tutorial",
    "isComplete": false,
    "id": 2
  }
}
```

#### Get All Todos
```http
GET /api/v1/
```

**Response:**
```json
[
  {
    "title": "Name",
    "desc": "Section",
    "isComplete": false,
    "id": 1
  }
]
```

#### Get Todo by ID
```http
GET /api/v1/{id}
```

**Example:**
```http
GET /api/v1/1
```

**Response:**
```json
{
  "title": "Name",
  "desc": "Section",
  "isComplete": false,
  "id": 1
}
```

**Error Response (404):**
```json
{
  "detail": "Todo Not Found"
}
```

## 📊 Data Model

### Todo Schema
```python
class Todo(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    desc: str = Field(..., min_length=3)
    isComplete: Optional[bool] = False
```

**Validation Rules:**
- `title`: Required, 3-100 characters
- `desc`: Required, minimum 3 characters
- `isComplete`: Optional, defaults to `false`

## 🧪 Testing the API

### Using curl

**Create Todo:**
```bash
curl -X POST "http://localhost:8000/api/v1/create" \
     -H "Content-Type: application/json" \
     -d '{"title": "Test Todo", "desc": "Testing API", "isComplete": false}'
```

**Get All Todos:**
```bash
curl "http://localhost:8000/api/v1/"
```

**Get Specific Todo:**
```bash
curl "http://localhost:8000/api/v1/1"
```

### Using Python requests

```python
import requests

# Base URL
BASE_URL = "http://localhost:8000/api/v1"

# Create todo
todo_data = {
    "title": "Python Todo",
    "desc": "Created with requests",
    "isComplete": False
}
response = requests.post(f"{BASE_URL}/create", json=todo_data)
print(response.json())

# Get all todos
response = requests.get(f"{BASE_URL}/")
print(response.json())

# Get specific todo
response = requests.get(f"{BASE_URL}/1")
print(response.json())
```

## 🔧 Configuration

### Environment Variables
You can configure the application using environment variables:

```bash
# Server host and port
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Database File
The application uses `students.json` as a simple file-based database. The file is automatically created if it doesn't exist.

## 📝 HTTP Status Codes Used

| Status Code | Meaning | Usage |
|-------------|---------|--------|
| 200 | OK | Successful GET requests |
| 201 | Created | Successful POST (create) |
| 404 | Not Found | Todo not found |
| 422 | Unprocessable Entity | Validation errors |

## 🛡️ Error Handling

The API implements proper error handling with meaningful responses:

### Validation Error (422)
Occurs when request data doesn't match the Pydantic model:
```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "ensure this value has at least 3 characters",
      "type": "value_error.any_str.min_length",
      "ctx": {"limit_value": 3}
    }
  ]
}
```

### Not Found Error (404)
Occurs when requesting a non-existent todo:
```json
{
  "detail": "Todo Not Found"
}
```

## 🔄 Development Workflow

### Making Changes
1. Edit the relevant files in `models/` or `routes/`
2. The server automatically reloads with `--reload` flag
3. Test changes using the interactive docs at `/docs`

### Adding New Endpoints
1. Define the route in `routes/TodoRoute.py`
2. Use proper HTTP methods and status codes
3. Add Pydantic models for request/response validation
4. Update this README with new endpoint documentation

## 🎯 Key Features Demonstrated

- **CRUD Operations**: Create, Read, Update, Delete functionality
- **Pydantic Validation**: Automatic data validation and serialization
- **HTTP Status Codes**: Proper REST API status codes
- **Error Handling**: Structured error responses
- **API Documentation**: Auto-generated OpenAPI/Swagger docs
- **Modular Structure**: Separated models, routes, and main app
- **File-based Storage**: Simple JSON database for demonstration

## 📚 Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [HTTP Status Code Reference](https://httpstatuses.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes to demonstrate FastAPI concepts.
