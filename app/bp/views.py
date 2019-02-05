import apispec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import DocumentedBlueprint, FlaskPlugin
from flask import jsonify
from flask.views import MethodView


spec = apispec.APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

bp = DocumentedBlueprint('documented_bp', __name__, spec)


@bp.route('/')
def index():
    """
    Gist detail view.

    ---
    x-extension: metadata
    get:
        responses:
            200:
                schema:
                    $ref: '#/definitions/Gist'
    """
    return 'index'


bp.add_url_rule('/', view_func=index, methods=['POST'])
bp.add_url_rule('/index', view_func=index)


class Crud(MethodView):

    def get(self):
        """
        Crud get view.

        ---
        x-extension: metadata
        get:
            responses:
                200:
                    schema:
                        $ref: '#/definitions/Crud'
        """
        return 'crud_get'

    def post(self):
        """
        Crud get view.

        ---
        x-extension: metadata
        post:
            responses:
                200:
                    schema:
                        $ref: '#/definitions/Crud'
        """
        return 'crud_get'


bp.add_url_rule('/crud', view_func=Crud.as_view('crud_view'))


@bp.route('/openapi.json')
def get_open_api():
    spec = bp.spec

    return jsonify(spec.to_dict())
