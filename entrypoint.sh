#!/bin/bash

uwsgi \
  --http-socket :$PORT \
  --module=be.wsgi:application \
  --pidfile=/tmp/be.pid \
  --processes=$PROCESSES \
  --threads=$THREADS  \
  --max-requests=$MAX_REQUEST \
  --master