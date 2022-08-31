from app.controllers import selectAll
from app.models import db_setup

if __name__ == '__main__':
    db_setup.init_db()
    # Show all employees
    print('All users')
    selectAll()
