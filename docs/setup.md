Instrusctions to set up development environment:

1.  Install homebrew

    `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2.  Install node, yarn, and postgres

    ```bash
    brew install node
    brew install yarn
    brew install postgres
    ```

3.  Install virtualenv

    `pip install virtualenv`

4.  Install python packages

    ```bash
    cd PTracker
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    ```

5.  Set environment variables (in PyCharm)

    ```bash
    APP_SETTINGS=development
    SQLALCHEMY_DATABASE_URI=postgres://127.0.0.1:5432/localptracker
    ```

6.  Install node packages

    ```bash
    cd client
    npm install --save react-redux
    npm install @types/react-redux
    npm install --save redux-thunk
    npm install classnames --save
    npm install --save-dev typings-for-css-modules-loader
    npm install --save-dev css-loader
    npm install react-spinkit --save
    npm install
    ```

7.  Install VSCode extensions
    npm 0.3.5
    Prettier 1.5.0
    Python 2018.6.0
    TSLint 1.0.33
    vscode-icons 7.24.0

8.  Setup formatOnSave
    cmd+shift+p to bring up workspace settings
    make sure it has all these settings:

    ```bash
        "[javascript]": {
            "editor.formatOnSave": true
        },
        "[typescript]": {
            "editor.formatOnSave": true
        },
        "editor.formatOnSave": true
    ```

9.  Create postgres DB

    ```bash
    psql postgres
    postgres=# CREATE DATABASE localptracker;
    postgres=# \c localptracker;
    postgres=# \q;
    export APP_SETTINGS=development
    export SQLALCHEMY_DATABASE_URI=postgres://127.0.0.1:5432/localptracker
    venv/bin/python manage.py db init
    venv/bin/python manage.py db upgrade
    venv/bin/python manage.py db migrate
    venv/bin/python manage.py db upgrate
    ```

10. Run the python server

    choose PTracker/venv/Python as project interpreter
    click the green run triangle

11. Run the frontend (live) rebuilder


    ```bash
    cd PTracker/client
    npm run dev
    ```

ANY TIME YOU CHANGE MODELS.PY, YOU NEED TO MIGRATE AND UPGRADE ON LOCAL, AND THIS:
`heroku run python manage.py db upgrade --app p-tracker`
