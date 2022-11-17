# talent-eng-ll

# Requirements
Requires Python 3.8+ as a base requirement.

Install virtualenv if not present:
```bash
pip3 install virtualenv
```

Create new enviroment via:
```bash
python3 -m virtualenv venv
```

Then depending on your OS:
|OS|Command|
|---|---|
|On Linux|`source venv/bin/activate`|
|On Windows (Powershell)|`venv\Scripts\activate.ps1`|
|On Windows (cmd)|`venv\Scripts\activate.bat`|

Install required packages via:
```bash
pip3 install -r requirements.txt
```

# Structure
|Directory|Purpose|
|---|---|
|`src/config`|Configuration and configuration providers definitions.|
|`src/data`|Data definitions and data descriptors.|
|`src/models`|Data models.|
|`src/providers`|Data providers and processors.|
|`envs_configs/`|Enviroment configuration. Contains JSON files to use with JSONConfigProvider.|
|`tests/`|Tests.|
|`conftest.py`|Configuration file for pyTest.|

# How to run tests

To run tests simply:
```bash
python3 -m pytest
```

# Before commit
Run black and isort
```bash
isort .
black .
```