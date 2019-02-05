from flask import Flask, Response


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/url-map')
    def map():
        html = "<h2> Path rules in Flask app.url_map._rules list: </h2>" \
              "<table><tr><th>Path rule</th><th>Methods</th><th>endpoint</th></tr>"
        for rule in app.url_map._rules:
            html += f"<tr><td>{rule.rule}</td><td>{', '.join(rule.methods)}</td><td>{rule.endpoint}</td><tr>"
        html += "</table>"

        html += "<h2> Path rules in Flask app.url_map._rules_by_endpoint dict: </h2>" \
              "<table><th>Key Endpoint</th><th>Path rule</th><th>Methods</th><th>endpoint</th></tr>"
        for endpoint, rules in app.url_map._rules_by_endpoint.items():
            for rule in rules:
                html += f"<tr><td>{endpoint}</td><td>{rule.rule}</td><td>{', '.join(rule.methods)}</td><td>{rule.endpoint}</td><tr>"
        html += "</table>"

        html += "<h2> View functions associated to an endpoint in app.view_functions dict: </h2>" \
              "<table><th>Key Endpoint</th><th>View function module</th><th>View function name</th><th>Object id</th></tr>"
        for endpoint, func in app.view_functions.items():
            html += f"<tr><td>{endpoint}</td><td>{str(func.__module__)}</td><td>{str(func.__name__)}</td><td>{id(func)}</td><tr>"
        html += "</table>"

        return Response(html)

    from .bp import bp as doc_bp
    app.register_blueprint(doc_bp, url_prefix='/api')

    return app
