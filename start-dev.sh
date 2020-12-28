# this all assumes we're running it in Linux / MacOS

StartServer () {
    echo "Activating Virtual Environment"
    source server/venv/bin/activate
    echo "Starting Back-End"
    python3 server/manage.py runserver
}

StartClient() {
    cd client
    echo "Starting Front-End"
    npm start
}

# solution to start both concurrently from 
# https://stackoverflow.com/questions/3004811/how-do-you-run-multiple-programs-in-parallel-from-a-bash-script#answer-41762802
StartServer &
P1=$!
StartClient &
P2=$!

wait $P! $P2

echo "shutting down"
cd ..