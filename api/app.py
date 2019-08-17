#!/usr/bin/env python
import os
import logging
from svg.generator import SVG_map
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    data = request.args
    TITLE = None
    PROGRESS = None
    TOTAL = None

    if "title" in data.keys():
        TITLE = data.get("title")
    if "progress" in data.keys():
        PROGRESS = int(data.get("progress"))
    if "total" in data.keys():
        TOTAL = int(data.get("total"))
    else:
        TOTAL = 100
    
    if TOTAL == 0:
        TOTAL = 1

    if not TITLE and not PROGRESS:
        svg_generator = SVG_map(total=TOTAL)
    elif not TITLE:
        svg_generator = SVG_map(progress=PROGRESS, total=TOTAL)
    elif not PROGRESS:
        svg_generator = SVG_map(title=TITLE, total=TOTAL)
    else:
        svg_generator = SVG_map(title=TITLE, progress=PROGRESS, total=TOTAL)

    return svg_generator.generate()


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=True)
