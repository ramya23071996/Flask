from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/gallery")
def gallery():
    image_folder = "static/images/gallery"
    image_list = os.listdir(image_folder)
    images = [img for img in image_list if img.lower().endswith((".jpg", ".png", ".jpeg", ".gif"))]
    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)