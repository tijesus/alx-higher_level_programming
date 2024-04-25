#!/bin/bash
# Takes in subject and email from a form
curl -sF email=test@gmail.com -F 'subject=I will always be here for PLD' "$1"
