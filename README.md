Checkout the project
```
git clone https://github.com/Senofjohan/starter_react_and_fastapi.git
```

Software versions used for project setup.
# Node 10+ should be okay. for launching the frontend
# python 3.6 is required I believe. updating to 3.8 will ensure no conflicts.

josh at starter_react_and_fastapi 🌲 node --version
v14.15.0
josh at starter_react_and_fastapi 🌲 python3 --version
Python 3.8.4
josh at starter_react_and_fastapi 🌲 pip3 --version
pip 20.1.1
josh at starter_react_and_fastapi 🌲 npm --version
6.14.8

# Open coding editor, I prefer one for frontend and one for backend.

Frontend
```
# Install the software dependencies `from npm
npm install
# npm run start which starts the server
npm run start
# open localhost: 3000
```

Backend 
# Create virual environment to install project dependencies into
```
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip list
cd src
uvicorn api:app --reload
```
# Activate the virtual environment so we can install software dependencies into it separate from what is on the system- https://docs.python.org/3.8/library/venv.html
source env/bin/activate
# Install the dependencies from requirements.txt into virtual environment so all team members have same dependencies.
pip install -r requirements.txt
cd backend/src
uvicorn api:app --reload
# Run the app using uvicorn server in reload mode. Changing files in src, will cause the server to automatically load your changes.



# Adding new software dependencies - such as newsapi-python
# make sure virtual env is activated
source env/bin/activate
pip install newsapi-python
# Freeze your current dependencies to the requirements.txt file.
pip freeze > requirements.txt
# Go to directory backend/src where the api.py is.
cd backend/src
# Run the app using uvicorn server in reload mode. Changing files in src, will cause the server to automatically load your changes.
uvicorn api:app —-reload


# If you need to run with the python debugger use - https://fastapi.tiangolo.com/tutorial/debugging/#run-your-code-with-your-debugger

# Useful links
Frontend with react - https://reactjs.org/docs/getting-started.html
Backend with FastApi - https://fastapi.tiangolo.com/

# Special note on connecting frontend and backend:
This project has cors(Cross origin resource sharing) configured using the fastapi documentation so that requests can be received from the frontend - https://fastapi.tiangolo.com/tutorial/cors/?h=+cors
