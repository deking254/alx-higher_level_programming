#!/bin/bash
#retrieve the allowedd methods
curl -sI $1 | grep -i 'Allow:'|sed 's/^.*: //'
