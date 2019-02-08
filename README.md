### Dev
#### First steps
1. `source venv/bin/activate`
2. install dependencies : `pip install -r requirements.txt`
3. Create .env file containing : 
  - `export FLASK_APP="run.py"`
  - `export FLASK_ENV="yourvalue"`
  - `export APP_SETTINGS="yourvalue"`
  - `export SECRET="yoursecret"`
  - `export SQLALCHEMY_DATABASE_URL="yourdburl"`
  - `export SQLALCHEMY_TEST_DATABASE_URL="yourtestdburl"`
4. source it : `source .env`
5. run : `python run.py`