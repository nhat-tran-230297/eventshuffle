from flask_migrate import Migrate

from app import create_app, db
from config import config_dict

config_mode = config_dict['Debug']

"""create app with config mode "Debug" and db migration""" 
app = create_app(config_mode)

if __name__ == '__main__':
    app.run(debug=True)


