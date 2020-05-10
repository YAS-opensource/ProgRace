from flask.views import MethodView
from flask import request, Response

from src.modules.svg.generator import SVG_map

class ProgressBadgeAPI(MethodView):
    """ Resource for buildidng and serving SVG """

    # pylint: disable=R0201
    def get(self):
        """
        Arguments
        ---------
        title : str
            title of the progress-bar
        progress : str
            progress of work
        total : str
            total amount of work

        Returns
        -------

        svg
            returns the generated svg
        """

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

        response = Response(
            svg_generator.generate(), mimetype="image/svg+xml;charset=utf-8"
        )

        return response