#!/bin/bash
#returns status code
curl -s --output dev/null -w %{response_code} $1
