import argparse
import logging

from flask import Blueprint, Flask, make_response, render_template, request
from flask_restx import Api, Resource, fields

from deposit_resolver import Deposit, calculate_deposit

swagger_blueprint = Blueprint("swagger", __name__, url_prefix="/docs")

app = Flask(__name__, template_folder="templates")
api = Api(app, doc="/swagger")
app.register_blueprint(swagger_blueprint)

deposit_model = api.model(
    "Deposit",
    {
        "date": fields.String(required=True),
        "periods": fields.Integer(required=True),
        "amount": fields.Integer(required=True),
        "rate": fields.Integer(required=True),
    },
)


@api.route("/index")
class Index(Resource):
    def get(self):
        response = make_response(render_template("index.html"))
        response.headers["Content-Type"] = "text/html"
        return response


@api.route("/deposit")
class DepositResolver(Resource):
    @api.doc(responses={200: "Deposit created successfully", 400: "Invalid arguments"})
    @api.expect(deposit_model)
    def get(self):
        deposit_values = {}
        for key, _type in [
            ("date", str),
            ("periods", int),
            ("amount", int),
            ("rate", int),
        ]:
            _value = request.args.get(key)
            try:
                _value = _type(_value)
            except (TypeError, ValueError):
                pass
            finally:
                deposit_values[key] = _value
        deposit = Deposit(**deposit_values)
        if invalid_arguments := deposit.validate():
            return {"error": f"Invalid operators: {invalid_arguments}"}, 400
        result = calculate_deposit(deposit)
        return result, 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--host", default="localhost", type=str, help="Адрес хоста")
    parser.add_argument("--port", "-p", default=8000, type=int, help="Порт")

    args = parser.parse_args()

    # Выводим адрес хоста и порт
    logging.debug(f"Host = {args.host}, port = {args.port}")

    host = args.host
    port = args.port
    app.run(host=host, port=port, debug=True)
