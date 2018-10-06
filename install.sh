pip install -U pip
pip install -r requirements.txt

brew install postgresql

# start postgres with schema.sql
pg_ctl -D /usr/local/var/postgres start
psql postgres < schema.sql