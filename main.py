import os


def main():
    os.environ["FLASK_APP"] = "netflikz"
    os.environ["FLASK_ENV"] = "development"
    os.system("env/bin/python -m flask run")


if __name__ == "__main__":
    main()
