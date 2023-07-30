from website import create_app
from flask import Blueprint
#pode fazer isso por causa do __init__.py

app = create_app()

if __name__ == '__main__': #apenas se esse arquivo rodar
    app.run(debug=True) #auto rerun webserver, turn off in production

