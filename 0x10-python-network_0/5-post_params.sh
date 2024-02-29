#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
data="email=test@gmail.com&subject=I will always be here for PLD"
curl -s -X POST -d "$data" "$1"
