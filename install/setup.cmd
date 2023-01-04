@echo off
pip install virtualenv
virtualenv venv
cmd /k "venv\Scripts\activate & pip install selenium & cls &echo DONE... & pause & exit"
