#!/usr/bin/env bash

python3 -m venv .venv --without-pip
source ./.venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
pip install -r requirements.txt
cd sharedcare
python manage.py makemigrations
python manage.py migrate --run-syncdb
cd ..