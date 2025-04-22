#!/bin/bash

/app/app/misc/schedule_job.sh

ngrok http 5000 --url https://matsuoka.ngrok.app  > /dev/null &

python3 /app/app/starkbank-app.py #&> /dev/null &
