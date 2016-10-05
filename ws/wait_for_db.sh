#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until mysql -h "$host" -u "root" -c '\l'; do
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - executing command"
exec $cmd