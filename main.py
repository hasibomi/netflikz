import os


os.environ["FLASK_APP"] = "netflikz"
os.environ["FLASK_ENV"] = "development"
os.system("env/bin/python -m flask run")
