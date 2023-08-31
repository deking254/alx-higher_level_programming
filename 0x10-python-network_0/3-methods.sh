#!/bin/bash
#retrieve the allowedd methods
curl -sI $1 | grep -i 'Server:'|sed 's/^.*: //'
