depandancies

1 > python 2.7 or later

2 > postgres 9.5 or later

after installation
login into postgres and
create database in postgres with following command

> create database pharmeasy_db;

exit from postgres console,

goto pharmeasy repo root folder.

execute pharmeasy_db.pgsql sript with following command

> psql -U username pharmeasy_db < pharmeasy_db.pgsql

install following python depandacies

> pip install -r requirements.txt

execute following command to run web_service

> python web_service.py

servie will be running on 5000 port

to verify all tests
execute following command

> python test_runner.py

should be able to pass all 14 test cases (13 unittest, 1 intigration test)

