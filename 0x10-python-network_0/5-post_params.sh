#!/bin/bash
# takes in a URL sends a POST request and displays the body of the response
curl -s -X POST -L "$1" -d 'email=hr@holbertonschool.com&subject=I will always be there for PLD'
