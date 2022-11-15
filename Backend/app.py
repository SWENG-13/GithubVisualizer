from flask import Flask

app = Flask(__name__)

# Serve static files
@app.route('/')
def serve_index():
  return send_from_directory('../Frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory('../Frontend', path)


# A test endpoint
@app.route("/testendpoint")
def test_endpoint():
    return "Test"
