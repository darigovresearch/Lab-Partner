Initial installation
====================

Setup
-----
Clone the repository into your :code:`home` directory
::
    git clone https://github.com/darigovresearch/Lab-Partner.git

Go into the folder that was just created
::
    cd Lab-Partner

On a Raspberry Pi, depending on the image you're using the python package manager pip may not be installed.

Installing pip:
::
    sudo apt install python3-pip

Upgrading pip (needed for opencv):
::
    pip3 install --upgrade pip

If you use environments you can set one up to prevent clashes of installation with other projects.

To create an environment:
::
    python3 -m venv env

To activate the environment:
::
    source env/bin/activate

Install the requirements
::
    pip3 install -r requirements.txt

Run the app:
::
    python3 App/app.py

Now you can navigate to the local URL which can be found on http://0.0.0.0:8765/ or http://localhost:8765/

You may need to enable Raspberry Pi Camera if you've chosen to use one
::
    sudo raspi-config

Test camera accesses
::
    raspistill -o test.jpg


Housekeeping
------------
Make sure if this is a fresh installation to update the default password. This is done by running the following command and following the onscreen prompts. Make sure it's memorable, secure and login again immediately afterwords to ensure the update has taken place.
::
    passwd
