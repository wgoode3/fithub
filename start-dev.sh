# this all assumes we're running it in Linux / MacOS

ActivateVirtualEnv () {
    if [ ! -d server/venv ]; then
        echo "creating virtualenvironment"
        python3 -m venv server/venv
        source server/venv/bin/activate
        echo "installing back-end dependencies"
        echo "this may take a few seconds..."
        pip install -r requirements.txt
    else
        echo "activating virtualenv"
        source server/venv/bin/activate
    fi
}

StartServer () {
    echo "Starting Back-End"
    python server/manage.py runserver
}

StartClient () {
    cd client
    echo "Starting Front-End"
    # npm start
    # prevent's clearing console?
    # https://github.com/facebook/create-react-app/issues/7640
    COLOR=1 npm start | cat
}

# start by activating the virtual environment

ActivateVirtualEnv

# next run both the front-end and back-end at the same time
# solution to start both concurrently from 
# https://stackoverflow.com/questions/3004811/how-do-you-run-multiple-programs-in-parallel-from-a-bash-script#answer-41762802

StartServer &
P1=$!
StartClient &
P2=$!

wait $P! $P2