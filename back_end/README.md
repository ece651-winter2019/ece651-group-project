back_end
========

Getting Started
---------------

- Change directory into your newly created project.

    cd back_end

- Create a Python virtual environment.

    python3.7 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_back_end_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini --reload
    
```bash
cd back_end
python3.7 -m venv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install -e ".[testing]"
env/bin/alembic -c development.ini revision --autogenerate -m "init"
env/bin/alembic -c development.ini upgrade head
env/bin/initialize_back_end_db development.ini
env/bin/pserve development.ini --reload
```
