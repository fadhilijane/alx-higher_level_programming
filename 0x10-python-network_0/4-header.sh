#!/bin/bash
# takes in a URL as an argument, sends a GET request, and displays the body of the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
