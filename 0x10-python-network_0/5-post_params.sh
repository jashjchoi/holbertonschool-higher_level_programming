#!/bin/bash
# takes in a URL sends a POST request and displays the response
curl -sX POST -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD' "$1"
