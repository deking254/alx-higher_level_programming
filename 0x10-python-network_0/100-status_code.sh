#!/bin/bash
#returns status code
curl -sw %{http_code} $1
