@echo off
echo Setting up E-Consultancy Backend...

echo Installing dependencies...
pip install -r requirements.txt

echo Running migrations...
python manage.py migrate

echo Creating superuser (if needed)...
python manage.py createsuperuser --noinput --username admin --email admin@example.com || echo Superuser already exists

echo Loading sample data...
python manage.py create_sample_data

echo Setup complete! You can now run:
echo python manage.py runserver

pause