from flask import Flask, render_template, request

from api.analytics_api import analytics_api
from api.ai_api import ai_api
from api.kpi_api import kpi_api


def create_app():
    app = Flask(__name__)

    # --------------------
    # Register API Blueprints
    # --------------------
    app.register_blueprint(analytics_api)
    app.register_blueprint(ai_api)
    app.register_blueprint(kpi_api)

    # --------------------
    # Page Routes
    # --------------------
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        mode = request.args.get("mode", "national")
        return render_template("dashboard.html", mode=mode)

    @app.route("/ai")
    def ai_page():
        return render_template("ai.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
