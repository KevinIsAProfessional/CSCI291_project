#!/bin/sh

echo "Enter a commit message"
read MESS

git add *
git commit -m "$MESS"
git push heroku master

echo "done"
