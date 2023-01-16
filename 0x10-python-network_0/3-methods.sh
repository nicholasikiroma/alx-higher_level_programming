#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server
curl -sLi "$1" | grep "Allow" | sed 's/Allow: //g'
