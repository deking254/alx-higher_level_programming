#!/bin/bash
#upload a json
curl -s -H "Content-Type: application/json" -d @$2 $1
