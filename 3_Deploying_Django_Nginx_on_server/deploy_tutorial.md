## Step 1: Creating a VPS(Droplet) on Digital Ocean with free 2 months account:
- https://try.digitalocean.com/freetrialoffer/ register gmail account with free trial for 2 months. 
- You will need to initialize any visa/mastercard by paying 1 euro which you receive back
- Also provide some random but existing european address
- After registration you can delete all your credentials and your card
- Go to https://cloud.digitalocean.com/droplets and click on Create Droplet the button. 
- Select Frankfurt, Ubuntu 22, and remember password. Other fields are not necessary now.
- Copy ipv4 of your droplet. Then use this ip, your password and username 'root', to connect via SSH client (PortX).
- Download PortX (https://portx.online/) to connect to your server. There are all instructions on main page.

## Step 2: Installing Python
- Update packages
```
sudo apt update
```

- Install Python
```
sudo apt install -y python3 python3-pip
```

## Step 3: clone your GitHub repo
- first let's install requirements file with packages from our env inside your Django project
```
source your_env/bin/activate  # On Windows, use: your_env\Scripts\activate

```
- Generate the requirements.txt File in your local Django project
```
pip freeze > requirements.txt

```
- Navigate to Your Django Project's Root Directory
```
cd path_to_your_django_project
```

- Review and Modify (if needed)
- Upload your project to GitHub and clone to your server


## Step 4: install virtualenv
- install pip package
```
sudo pip3 install virtualenv
```

- go to your project directory
```
ls
```

```
cd yourprojectfoldername
```
- create venv 
```
virtualenv env
```
- activate venv
```
source env/bin/activate
```
- install package dependencies
```
pip install -r requirements.txt
```

## Step 5: install Django and gunicorn in your virtual, whitenoise, make migrations and add collect static files
```
pip install django gunicorn
```
- also add your IP address or domain to the ALLOWED_HOSTS variable in settings.py.
- also if you have any migrations to run, perform the action:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py collectstatic
```
- Import Thing about static files: you must make sure to add few lines in your setings.py file. 
- Add this line into your Installed_apps of setting file. 
```
"whitenoise.runserver_nostatic",
```
- Add this line into MiddleWare inside your settings file. 
```
"whitenoise.middleware.WhiteNoiseMiddleware",
```
- Also, add these lines at the bottom of the webapp/urls. py file.
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
```

- Also, add these imports lines at the top of the yourproject/urls. py file.
```
from django.conf import settings # new
from  django.conf.urls.static import static #new
```
- install whitenoise pip package which works with Django WSGI config and simplifies static file serving for Python web apps
```
pip install whitenoise
```

## Step 6: Configuring gunicorn (network communication file)
- Deactivate the virtual environment by executing the command below:
```
deactivate
```

- Let’s create a system socket file for gunicorn now:
```
sudo nano /etc/systemd/system/gunicorn.socket
```

- Paste the contents below and save the file
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
- Use ctrl+o and press enter to save changes, then ctrl+x to exit 
- Next create a service file for gunicorn
```
sudo nano /etc/systemd/system/gunicorn.service
```

- Paste the contents below inside this file (replace directory name and settings folder):
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/YourProjectDirectoryName
ExecStart=/root/YourProjectDirectoryName/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          yourSettingsFileFoldername.wsgi:application
[Install]
WantedBy=multi-user.target
```

- Let's now start and enable the gunicorn socket
```
sudo systemctl start gunicorn.socket
```
```
sudo systemctl enable gunicorn.socket
```

- install nginx in the root
```
sudo apt install -y nginx
```
- start nginx
```
sudo systemctl start nginx
```
- restart gunicorn service
```
sudo service gunicorn restart
```
- restart nginx service
```
sudo service nginx restart
```
- delete nginx default app config
```
cd /etc/nginx/sites-enabled
```
```
sudo rm -f default
```
- Create a configuration file for Nginx using the following command
```
sudo nano /etc/nginx/sites-available/webapp
```
- Paste the below contents inside the file created
```
server {
    listen 80 default_server;
    server_name _;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /YourStaticFilesDirectoryName/ {
        root /root/YourProjectDirectoryName;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

- Create a configuration file for Nginx using the following command

```
sudo ln -s /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/
```
- Run this command to load a static file
```
sudo gpasswd -a www-data root
```