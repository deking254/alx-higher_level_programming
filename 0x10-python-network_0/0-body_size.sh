#!/bin/bash
#return body size of response
curl -sw  %{size_download}"\n" $1 -o /dev/null
