import argparse
import logging

from flask import Flask, jsonify, render_template, request

from deposit_resolver import Deposit, calculate_deposit

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/deposit", methods=["GET"])
def create_deposit():
    deposit_values = {}
    for key, _type in [("date", str), ("periods", int), ("amount", int), ("rate", int)]:
        _value = request.args.get(key)
        try:
            _value = _type(_value)
        except (TypeError, ValueError):
            pass
        finally:
            deposit_values[key] = _value
    deposit = Deposit(**deposit_values)
    if invalid_arguments := deposit.validate():
        return jsonify({"error": f"Invalid operators: {invalid_arguments}"}), 400
    result = calculate_deposit(deposit)
    return jsonify(result), 200


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
