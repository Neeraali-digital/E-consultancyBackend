# eConsultancy Backend

This is a Django backend project for an education consultancy, using PostgreSQL as the database. The project is structured for scalability and maintainability, with normalized database models and all core functionalities required by an education consultancy (student management, course management, application processing, payments, user roles, etc.).

## Getting Started

1. **Install dependencies:**
   - Python 3.8+
   - Django
   - psycopg2 (PostgreSQL adapter)

2. **Configure the database:**
   - Update `DATABASES` in `eConsultancy/settings.py` to use your PostgreSQL credentials.

3. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

## Project Structure
- `eConsultancy/` - Django project settings and configuration
- `manage.py` - Django management script

## Next Steps
- Implement core apps: students, courses, applications, payments, users/roles
- Normalize all models and relationships
- Add API endpoints for all functionalities

---

For more details, see the `.github/copilot-instructions.md` file.
