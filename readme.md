==Polymath, the app==

Polymath is run on Django, deployed to Heroku, and backed by AWS.

To run it locally, you need:
- Python 2.7.2
- Foreman
- A database, preferably Postgres
- These gems:
  - sass
  - compass
  - zurb-foundation

===This is how we do===

  $ git clone https://github.com/gakimball/polymath
  $ cd polymath
  $ virtualenv venv
  $ source venv/bin/activate
  $ pip install
  $ foreman start

===Environemnt variables===

You need some environment variables to make everything work.

  - **DATABASE_URL** uses the dj_database_url library to convert a database URL into a settings object for Django.
  - **DJANGO_DEBUG** enables verbose error messages in Django when set to 1.
  - **DJANGO_SECRET_KEY** can probably be anything because I don't know!
  - The three AWS storage variables aren't needed in development, as Django will use its default file system storage backend instead.