from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

db_host = parser.get('db', 'host')
db_port = parser.get('db', 'port')
db_user_name = parser.get('db', 'user_name')
db_user_password = parser.get('db', 'user_password')
