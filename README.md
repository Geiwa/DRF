#INSTALL 
git clone git@github.com:Geiwa/DRF.git

#CREATE virtuslvenv and install requirements.txt
pip3 install -r requirements.txt


#CREATE file .env and write 
SECRET_KEY='django-insecure-joim0zv#pc)w0s*g8##$1)934rs4%13pb86mo91shmjn*1*5p+'
DATABASE_URL=postgresql://db_name:db_password@localhost:5432/db_username
DJANGO_SETTINGS_MODEL=config.settings
DEBUG=true


#CREATE MIGRATIONS

python3 manage.py makemigrations
python3  manage.py migrate

#CREATE administration
python3 manage.py createsuperuser 


#CREATE file .env and write 
SECRET_KEY='django-insecure-joim0zv#pc)w0s*g8##$1)934rs4%13pb86mo91shmjn*1*5p+'
DATABASE_URL=postgresql://db_name:db_password@localhost:5432/db_username
DJANGO_SETTINGS_MODEL=config.settings
DEBUG=true


#Run server 
python3 manage.py runserver