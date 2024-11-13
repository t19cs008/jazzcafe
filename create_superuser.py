import subprocess
import os

def create_superuser():
    user_name = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if user_name is None or email is None or password is None:
        return

    subprocess.run(["python", "manage.py", "createsuperuser", "--noinput"])
    
create_superuser()