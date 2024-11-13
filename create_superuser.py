import subprocess
import os

def create_superuser():
    user_name = os.environ.get("SUPERUSER_USERNAME")
    email = os.environ.get("SUPERUSER_EMAIL")
    password = os.environ.get("SUPERUSER_PASSWORD")

    if user_name is None or email is None or password is None:
        return

    subprocess.run(["python", "manage.py", "createsuperuser",
                    "--username", user_name,
                    "--email", email,
                    "--password", password])
    
create_superuser()