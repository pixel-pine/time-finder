Instructions for running development server:

-Go to terminal and make sure you are in the backend folder. If you are not, type:

```
cd backend
```

It should now say something similar to "~/time-finder/backend"

-Execute these commands:

```

python -m venv venv


#for Windows:
./venv/Scripts/activate

#for mac/linux:
source venv/bin/activate


pip install -r requirements.txt


python manage.py migrate


python manage.py createsuperuser  # follow on screen instructions
 

python manage.py runserver
 

```
Click on the IP address the terminal gives you in order to see the development server or Go to http://localhost:8000/admin and login with your superuser credentials

To stop the server type Ctrl-c in your terminal.

You may need to stop the server and restart it in order to apply changes (follow below instructions):

After you executed all these steps, and want to relaunch the development server, you only need these commands:

```

python -m venv venv


#for Windows:
./venv/Scripts/activate

#for mac/linux:
source venv/bin/activate

#the following two commands are necessary if you've made changes to the backend (ex: editing or creating a new model):
python manage.py makemigrations

python manage.py migrate


python manage.py runserver

```
