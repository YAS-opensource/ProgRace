from flask import Blueprint

from src.views.ProgressBadge.progress_badge import ProgressBadgeAPI

blueprint = Blueprint("progdown", __name__)

progress_badge = ProgressBadgeAPI.as_view("progress_badge")

blueprint.add_url_rule("/", view_func=progress_badge, methods=["GET"])