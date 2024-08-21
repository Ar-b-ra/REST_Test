import argparse
import logging

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', default='localhost', type=str, help='Адрес хоста')
    parser.add_argument('--port', '-p', default=8000, type=int, help='Порт')

    args = parser.parse_args()

    # Выводим адрес хоста и порт
    logging.debug(f"Host = {args.host}, port = {args.port}")

    host = args.host
    port = args.port
    app.run(host=host, port=port, debug=True)
