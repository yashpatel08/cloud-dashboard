# Cloud Optimization Dashboard

A full-stack web application that analyzes cloud infrastructure resources and provides cost optimization recommendations. Built with React, FastAPI, and PostgreSQL.

## 🏗️ Architecture

```
PostgreSQL ← FastAPI ← React Dashboard
```

- **Frontend**: React with TypeScript, Tailwind CSS
- **Backend**: FastAPI with SQLAlchemy ORM
- **Database**: PostgreSQL
- **API**: RESTful endpoints with JSON responses

## 📋 Prerequisites

- Node.js 16+ and npm
- Python 3.8+
- PostgreSQL 12+

## 🛠️ Installation & Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd cloud-optimization-dashboard
```

### 2. Database Setup
```bash
# Create PostgreSQL database
createdb cloud_optimizer

# Or using SQL
psql -U postgres
CREATE DATABASE cloud_optimizer;
\q
```

### 3. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-multipart pydantic

# Or install from requirements.txt
pip install -r requirements.txt

# Update database connection in app/database.py
# DATABASE_URL = "postgresql://username:password@localhost/cloud_optimizer"

# Initialize database with sample data
python init_db.py

# Start backend server
uvicorn main:app --reload --port 8000
```

### 4. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Install Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Start development server
npm start
```

### 5. Verify Setup
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Frontend Dashboard: http://localhost:5173

## 🌐 Usage

### Dashboard Navigation
1. **Access Dashboard**: Open `http://localhost:5173`
2. **View Summary**: Check total resources, costs, and savings at the top
3. **Monitor Resources**: Review all infrastructure in the resources table
4. **Check Recommendations**: View optimization opportunities
5. **Implement Changes**: Mark recommendations as completed
6. **Track Progress**: Monitor total potential savings

### Understanding the Interface

#### Summary Cards
- **Resources**: Total count of monitored infrastructure
- **Monthly Cost**: Current spending across all resources
- **Potential Savings**: Estimated cost reductions available
- **Opportunities**: Number of actionable recommendations

#### Resource Table
- **CPU/Storage Column**: Shows CPU utilization for compute resources, storage size for storage resources
- **Memory Column**: Shows memory utilization (compute only)
- **Color Coding**: 
  - 🟡 Yellow: Under-utilized (CPU <30%, Memory <50%)
  - 🟢 Green: Well-utilized
  - 🔵 Blue: Storage information

#### Recommendations Cards
- **Reason**: Explanation of why optimization is recommended
- **Current Cost**: Monthly cost of the resource
- **Estimated Savings**: Potential monthly savings
- **Confidence**: Algorithm confidence level (High/Medium/Low)
- **Implementation**: Button to mark as completed

## 📊 Sample Data

The application comes pre-loaded with realistic sample resources:

### Over-Provisioned Instances (Optimization Opportunities)
```
web-server-1    | t3.xlarge      | 15% CPU, 25% Memory | $150/month
api-server-2    | m5.large       | 12% CPU, 30% Memory | $90/month  
worker-3        | Standard_D2s_v3| 8% CPU, 20% Memory  | $70/month
```

### Well-Utilized Resources
```
database-1      | m5.xlarge      | 75% CPU, 85% Memory | $180/month
cache-server    | n1-standard-2  | 65% CPU, 70% Memory | $50/month
```

### Storage Resources
```
backup-storage  | 1000GB | AWS    | $100/month (optimization candidate)
log-storage     | 500GB  | Azure  | $75/month  (optimization candidate)
database-storage| 200GB  | GCP    | $25/month  (well-utilized)
```

## 🤖 Optimization Rules

### 1. Instance Downsizing
- **Criteria**: CPU < 30% AND Memory < 50%
- **Action**: Recommend smaller instance type
- **Savings**: 40-60% cost reduction
- **Confidence**: High
- **Example**: t3.xlarge → t3.large

### 2. Storage Optimization  
- **Criteria**: Storage volumes > 500GB
- **Action**: Suggest reducing storage size
- **Savings**: 20-40% cost reduction
- **Confidence**: Medium
- **Example**: 1000GB → 500GB

### 3. Confidence Levels
- **High**: Clear optimization opportunity with significant savings
- **Medium**: Moderate optimization potential
- **Low**: Minor optimization with small savings

## 🛡️ API Endpoints

### Resources
```http
GET /resources
```
Returns all cloud resources with utilization and cost data.

**Response:**
```json
[
  {
    "id": 1,
    "name": "web-server-1",
    "resource_type": "instance",
    "provider": "AWS",
    "instance_type": "t3.xlarge",
    "cpu_utilization": 15.0,
    "memory_utilization": 25.0,
    "monthly_cost": 150.0,
    "recommendations": [...]
  }
]
```

```http
POST /resources
```
Create a new cloud resource.

### Recommendations
```http
GET /recommendations
```
Returns all optimization recommendations.

**Response:**
```json
[
  {
    "id": 1,
    "resource_id": 1,
    "name": "web-server-1",
    "reason": "Over-provisioned instance. Recommend downsizing.",
    "current_cost": 150.0,
    "estimated_savings": 75.0,
    "confidence": "high",
    "implemented": false
  }
]
```

```http
PATCH /recommendations/{id}/implement
```
Mark a recommendation as implemented.

### Health Check
```http
GET /
```
API status check.

## 📁 Project Structure

```
cloud-optimization-dashboard/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py          # Database connection
│   │   ├── models.py            # SQLAlchemy models
│   │   ├── schemas.py           # Pydantic schemas
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── resources.py     # API endpoints
│   ├── main.py                  # FastAPI application
│   ├── init_db.py               # Database initialization
│   └── requirements.txt         # Python dependencies
└── frontend/
|    ├── node_modules/
|    ├── public/
|    │   └── index.html
|    ├── src/
|    │   ├── api/
|    │   │   └── api.ts
|    │   ├── assets/
|    │   │   └── react.svg
|    │   ├── components/
|    │   │   ├── Recommendations.tsx
|    │   │   ├── ResourceTable.tsx
|    │   │   |── Summary.tsx
|    │   │   └── ui/
|    │   │       ├── card.tsx     # Card component
|    │   │       └── button.tsx   # Button component
|    │   ├── pages/
|    │   │   └── Dashboard.tsx
|    │   ├── types/
|    │   │   └── index.ts
|    │   ├── App.css
|    │   ├── App.tsx
|    │   ├── index.css
|    │   ├── main.tsx
|    │   └── vite-env.d.ts
|    ├── .gitignore
|    ├── components.json
|    ├── eslint.config.js
|    ├── index.html
|    ├── package-lock.json
|    └── package.json
└── README.md
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:
```bash
DATABASE_URL=postgresql://username:password@localhost/cloud_optimizer
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
```

### Database Configuration
Update `app/database.py` with your PostgreSQL credentials:
```python
DATABASE_URL = "postgresql://username:password@localhost/cloud_optimizer"
```

### Frontend Configuration
Update API URL in frontend components if needed:
```typescript
const API_BASE_URL = "http://localhost:8000";
```

## 🚀 Deployment

### Backend Deployment (Production)
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Or using Docker
docker build -t cloud-dashboard-api .
docker run -p 8000:8000 cloud-dashboard-api
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Serve static files
npm install -g serve
serve -s build -l 3000

# Or deploy to Netlify/Vercel
```

### Database Deployment
```bash
# Production PostgreSQL setup
# Update DATABASE_URL for production database
# Run migrations
python init_db.py
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pip install pytest pytest-asyncio httpx
python -m pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm test
npm run test:coverage
```

### API Testing
Use the interactive API documentation at `http://localhost:8000/docs` to test endpoints.

## 📈 Monitoring & Analytics

### Key Metrics Tracked
- **Total Resources**: Count of monitored infrastructure
- **Monthly Costs**: Current spending across all resources  
- **Potential Savings**: Estimated cost reductions from recommendations
- **Optimization Opportunities**: Number of actionable recommendations
- **Implementation Rate**: Percentage of recommendations completed

### Performance Insights
- **Over-provisioned Resources**: Resources with low utilization
- **Cost Optimization**: Potential monthly savings per resource
- **Provider Distribution**: Resources across AWS, Azure, GCP
- **Resource Types**: Breakdown of compute vs storage resources

## 🔍 Troubleshooting

### Common Issues

#### Database Connection Error
```bash
# Check PostgreSQL is running
pg_ctl status

# Verify database exists
psql -l | grep cloud_optimizer

# Test connection
psql -d cloud_optimizer -c "SELECT 1;"
```

#### Frontend API Connection Error
```bash
# Verify backend is running
curl http://localhost:8000/

# Check CORS configuration in main.py
# Ensure allow_origins includes frontend URL
```

#### Missing Dependencies
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
npm audit fix
```

#### Port Already in Use
```bash
# Backend (change port)
uvicorn main:app --reload --port 8001

# Frontend (change port)
PORT=3001 npm start
```

### Debug Mode
Enable debug logging in FastAPI:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
