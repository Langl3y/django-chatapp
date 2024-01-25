# Goatstudio Django rest template
<span style="color:red;font-weight:700;font-size:100px">
    Windows are not supported.
</span>

## Requirements

- Ubuntu 22.04 LTS
- Python 3.10
- Django 4.2.5
- MySQL >= 5.8
- Redis >= 6.0

## Install core libs

```shell
./init.sh
```

## Install python modules
If you use Macbook M1 please follow [this guide](https://pypi.org/project/mysqlclient/) to install mysqlclient. 

After that, join Goatstudio VPN and install requirements

```shell
pip install -r requirements.txt
```

**Noted**: If you cannot install uwsgi with miniconda. Please run this script 

```shell
conda install -c conda-forge uwsgi
````

## Env

Create `.env` file

```shell
cp .env.sample .env
```

## Run

Migrate database

```shell
python manage.py migrate
```

Create static assets for prod

```shell
python manage.py collectstatic
```

Run server for test

```shell
python manage.py runserver
```

**Noted**: When deploy to production please start server with uwsgi.

## Test APIs

Cannot test in Chrome without HTTPS. Because chrome never send cookies `cross domain` with SameStime is `None` and
Secure is `False`.

If you test with postman, you have to change SESSION_COOKIE_SECURE to `False`. Otherwise, you have to modify SameStime
in `Postman cookie` to None after login.

## APIs Documentation

Please read at [Goatstudio-Backend.yaml](Goatstudio-Backend.yaml)