#!/bin/sh

host=$1

rsync -av --cvs-exclude . $host:/tmp/miningpool
ssh $host "pip install --upgrade /tmp/miningpool"
