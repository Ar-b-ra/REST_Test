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
    try:
        deposit_values = {"date": request.args.get("date", ""),
                          "periods": int(request.args.get("periods")),
                          "amount": int(request.args.get("amount")),
                          "rate": int(request.args.get("rate"))}
        deposit = Deposit(**deposit_values)
        if result := deposit.validate():
            return jsonify({"error": f"Invalid operators: {result}"}), 400
    except (TypeError, ValueError):
        return jsonify({"error": f"Invalid arguments"}), 400
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
