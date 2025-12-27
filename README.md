# SiteStore - React + Django Full Stack Application

A modern full-stack application with React frontend and Django backend, configured for both development and production environments.

## Project Structure

```
sitestore/
├── backend/          # Django backend
│   ├── api/         # API app with models, views, serializers
│   ├── config/      # Django project settings
│   └── manage.py
├── frontend/        # React frontend (Vite)
│   ├── src/
│   └── package.json
└── README.md
```

## Features

- ✅ React frontend with Vite
- ✅ Django REST Framework backend
- ✅ CORS configured for development
- ✅ Production-ready configuration
- ✅ Example CRUD API (Items)
- ✅ Modern, responsive UI

## Prerequisites

- Python 3.8+
- Node.js 16+ and npm/yarn
- Virtual environment (recommended)

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your `SECRET_KEY`:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
   CORS_ALLOW_ALL_ORIGINS=True
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

## Development Mode

### Running the Application

**Terminal 1 - Django Backend:**
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python manage.py runserver
```
Backend will run on `http://localhost:8000`

**Terminal 2 - React Frontend:**
```bash
cd frontend
npm run dev
```
Frontend will run on `http://localhost:5173`

### Development Features

- **Hot Module Replacement (HMR)** - React changes update instantly
- **Proxy Configuration** - Vite proxies `/api` requests to Django backend
- **CORS Enabled** - Backend allows requests from frontend origin
- **Separate Servers** - Frontend and backend run independently

### API Endpoints

- `GET /api/health/` - Health check
- `GET /api/items/` - List all items
- `POST /api/items/` - Create new item
- `GET /api/items/<id>/` - Get item details
- `PUT /api/items/<id>/` - Update item
- `DELETE /api/items/<id>/` - Delete item

## Production Mode

### Building for Production

1. **Build React frontend:**
   ```bash
   cd frontend
   npm run build
   ```
   This creates a `dist/` folder with optimized production build.

2. **Configure Django for production:**
   Update `backend/.env`:
   ```env
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   CORS_ALLOW_ALL_ORIGINS=False
   CORS_ALLOWED_ORIGINS=https://yourdomain.com
   ```

3. **Collect static files:**
   ```bash
   cd backend
   python manage.py collectstatic --noinput
   ```

4. **Run Django server:**
   ```bash
   python manage.py runserver
   ```
   Or use a production server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn config.wsgi:application
   ```

### Production Features

- **Single Server** - Django serves both API and React app
- **Optimized Build** - React app is minified and optimized
- **Static File Serving** - Django serves React static assets
- **Security** - CORS restricted, DEBUG disabled

## Deployment Options

### Option 1: Django Serves Everything (Current Setup)
- Django serves React build files
- Single server deployment
- Good for small to medium applications

### Option 2: Separate Frontend/Backend
- Deploy React to CDN (Vercel, Netlify, etc.)
- Deploy Django to cloud (Heroku, AWS, etc.)
- Update CORS settings to allow frontend domain

## Troubleshooting

### CORS Errors
- Ensure `django-cors-headers` is installed
- Check `CORS_ALLOWED_ORIGINS` in settings
- Verify frontend URL matches CORS configuration

### Static Files Not Loading in Production
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATICFILES_DIRS` in settings
- Verify file permissions

### API Connection Issues
- Check backend is running on port 8000
- Verify proxy configuration in `vite.config.js`
- Check browser console for errors

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## License

MIT

