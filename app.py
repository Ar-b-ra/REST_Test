import argparse
import logging

from flask import Flask, jsonify, request

from deposit_resolver import Deposit, calculate_deposit

app = Flask(__name__)


@app.route("/deposit", methods=["GET"])
def create_deposit():
    deposit_json = request.get_json()
    deposit = Deposit(**deposit_json)
    if result := deposit.validate():
        return jsonify({"error": f"Invalid operators: {result}"}), 400
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
