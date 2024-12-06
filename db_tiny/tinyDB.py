from pathlib import Path

from tinydb import TinyDB

BASE_DIR = Path(__file__).parent.parent


def tinydb_form():
    db_path = TinyDB(f"./db_tiny/db.json")
    table = db_path.table("form")
    if len(table.all()) == 0:
        company = {
            "name": "Company",
            "company_email": "email",
            "company_phone": "phone",
            "profile": "str",
        }
        user = {
            "name": "User",
            "email": "email",
            "phone": "phone",
            "birth_date": "data",
        }
        list_profile_form = [company, user]
        for form in list_profile_form:
            table.insert(form)
    return table.all()
