# Quick Start Guide

## Development Setup (5 minutes)

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set SECRET_KEY
python manage.py migrate
python manage.py runserver
```

Backend runs on: http://localhost:8000

### 2. Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: http://localhost:5173

### 3. Test the Application
- Open http://localhost:5173 in your browser
- You should see the SiteStore app
- Try adding an item to test the API connection

## Production Build

### 1. Build React App
```bash
cd frontend
npm run build
```

### 2. Configure Django for Production
Edit `backend/.env`:
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com
```

### 3. Collect Static Files
```bash
cd backend
python manage.py collectstatic --noinput
```

### 4. Run Production Server
```bash
python manage.py runserver
# Or use Gunicorn:
# pip install gunicorn
# gunicorn config.wsgi:application
```

Visit http://localhost:8000 - Django serves both API and React app!

## Troubleshooting

**CORS Errors?**
- Make sure backend is running
- Check `CORS_ALLOWED_ORIGINS` in backend settings

**API Not Working?**
- Verify backend is on port 8000
- Check browser console for errors
- Test API directly: http://localhost:8000/api/health/

**Static Files Not Loading in Production?**
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` in settings
- Verify React build exists in `frontend/dist/`

