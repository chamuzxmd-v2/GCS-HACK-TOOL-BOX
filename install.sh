#!/bin/bash
pkg update -y
pkg install python git -y
pip install -r requirements.txt
python main.py
