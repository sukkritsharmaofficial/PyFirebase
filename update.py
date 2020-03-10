from functools import wraps
import sys
import os
from flask import Flask, render_template, redirect, request, url_for, session
import pyrebase
import subprocess
import time

# FIREBASE SETUP
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initializing firebase cred
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://iot-studentreg.firebaseio.com'}) #config

root = db.reference()

user = root.child('Student').child('Attendance').child('s3') 

# DEFINING THE STUDENT DETAILS STRUCTURE JUST ONCE AND PASSING AND UPDATING LATER ON

dat = {"UID": "DEVICE ID", "ID": "REGISTRATION NUMBER", "ATTENDANCE": "FALSE", "TIME STAMP": "TIME OF ENTRY"}
      

def update_attendance(user, p):
      if p == True:
            user.update({"Present" : "True"})
      else:
            user.update({"Present" : "False"})

def add_student(user, name):
      user.child(name).set(dat) # SETTING NEW VALUES

def update_student_info(user, name, dat):
      if user.child(name) is None: # CHECKING FOR EMPTY ENTRY
            user.child(name).set(dat) # UPDATING ENTRY
      else:
            user.child(name).update(dat) # ADDING DATA TO EMPTY ENTRY
