#!/bin/bash
#Takes in a URL, sends a request to the URL, displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
