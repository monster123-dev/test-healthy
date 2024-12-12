from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Generate static HTML
    output_dir = "static_site"
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        with open(os.path.join(output_dir, "index.html"), "w") as f:
            f.write(render_template("index.html"))

    print(f"Static site saved to {output_dir}")
