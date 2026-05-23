#!/bin/bash
cd ~/Desktop/echo-loop || exit
git add .
git commit -m "Update: $(date '+%Y-%m-%d %H:%M')"
git push origin main
