from flask import Flask, render_template

app = Flask(__name__)

@app.route("/blogs")
def blogs():
    blog_list = [
        {
            "title": "Designing with Purpose",
            "author": "Ramya",
            "snippet": "Explore how intentional design choices shape user experience.",
            "image": "blog1.jpg",
            "featured": True
        },
        {
            "title": "Python for Automation",
            "author": "Ramya",
            "snippet": "Learn how to automate daily tasks using Python scripts.",
            "image": "blog2.jpg",
            "featured": False
        },
        {
            "title": "Mastering Flask",
            "author": "Ramya",
            "snippet": "A deep dive into Flask routing, templates, and deployment.",
            "image": "blog3.jpg",
            "featured": True
        }
    ]
    return render_template("blogs.html", blogs=blog_list)

if __name__ == "__main__":
    app.run(debug=True)