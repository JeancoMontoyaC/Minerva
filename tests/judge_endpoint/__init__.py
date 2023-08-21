"""Flask app creation for testing."""

from flask import Flask

from app.ping import ping, judge_endpoint_bp


# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (("/", ping), ("/", judge_endpoint_bp))


def create_app() -> Flask:
    """Create Flask app."""
    app = Flask(__name__)

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app
