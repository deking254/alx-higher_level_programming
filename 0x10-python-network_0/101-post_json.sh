#!/bin/bash
#upload a json
curl -sX POST -d @$1 $2
