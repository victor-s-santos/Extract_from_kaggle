# Extract from Kaggle

## How to run
* __I. Create an account on Keaggle:__
    - `Go to https://www.kaggle.com/account/login?, and on register`

* __II. Get the credentials:__
    - `Go to https://www.kaggle.com/settings/account, and click on Create New Token, to download the kaggle.json file`
    - ![Create token](images/create_token.png)
    - `Move the kaggle.json file to the this project directory`

* __III. Clone this repository:__
    - `git clone https://github.com/victor-s-santos/Extract_from_kaggle.git`

* __IV. Create and use the virtualenv:__
    - `python -m venv .venv`
    - `source .venv/bin/activate`

* __V. Build the mongo image:__
    - `docker compose up`

* __VI. Install dependencies:__
    - `pip install -r requirements.txt`

* __VII. Create your env file:__
    - `Use the env_sample file to create your env`

* __VIII. Run the python main file:__
    - `python main.py`
