#!/usr/bin/env python
import os

from flask import Flask

from src.routers import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)