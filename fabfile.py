from fabric.api import env, local, require

def deploy():
	require('environment')
	maintenance_on()


def maintenance_on():
	require('environment')
	local('heroku maintenance:on --remote %s' % env.environment)

def maintenance_on():
	require('environment')
	local('heroku maintenance:off --remote %s' % env.environment)


def push():
	require('environment')
	local('git push %s master' % env.environment)


def syncdb():
	require('environment')
	if (env.environment == 'development'):
		local('foreman run python manage.py syncdb')
	else:
		local('heroku run python manage.py syncdb --remote %s' % env.environment)

def migrate(app=None):
	require('environment')
	if (env.environment == 'development'):
		if (app is not None):
			local('foreman run python manage.py migrate %s' % app)
		else:
			local('foreman run python manage.py migrate')
	else:
		if (app is not None):
			local('heroku run python manage.py migrate %s --remote %s' % (app, env.environment))
		else:
			local('heroku run python manage.py migrate --remote %s' % env.environment)