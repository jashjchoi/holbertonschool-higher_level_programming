#!/bin/bash
# takes in a URL sends a POST request and displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"
