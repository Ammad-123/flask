set Flask_app=myapp.py
echo %FLASK_APP%
flask db init
flask db migrate
flask db upgrade