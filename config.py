import os

class Config(object):
	SECRET_KEY = ''
	#Token Domicilion
	os.environ['PAGE_ACCESS_TOKEN'] = ''

	# Cliente id DEV
	os.environ['APP_CLIENT_ID'] = ''
	# ID secreto
	os.environ['APP_CLIENT_SECRET'] = ''
	# Token de la app
	os.environ['APP_TOKEN'] = ''
	# Variable codigo viejo
	USER_GEONAMES = os.environ.get('USER_GEONAMES')

class DevelopmentConfig(Config):
	DEBUG = True
	