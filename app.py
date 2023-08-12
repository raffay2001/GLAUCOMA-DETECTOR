from flask import Flask, render_template, request, jsonify
import os

# from detector.glaucoma_detector import detect_glaucoma

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if "file" not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"})

        if file:
            filename = os.path.join("media", file.filename)
            file.save(filename)
            # processed_image = detect_glaucoma(filename)  # Call your image analysis function
            processed_image = ""  # Call your image analysis function
            return render_template("index.html", processed_image=processed_image)


if __name__ == "__main__":
    app.run(debug=True)
