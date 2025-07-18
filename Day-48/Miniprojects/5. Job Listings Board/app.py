from flask import Flask, render_template

app = Flask(__name__)

@app.route("/jobs")
def jobs():
    job_list = [
        {
            "title": "Frontend Developer",
            "company": "TechNova",
            "logo": "company1.png",
            "remote": True,
            "location": "Remote"
        },
        {
            "title": "Data Analyst",
            "company": "DataSphere",
            "logo": "company2.png",
            "remote": False,
            "location": "Bangalore"
        },
        {
            "title": "Backend Engineer",
            "company": "CodeCraft",
            "logo": "company3.png",
            "remote": True,
            "location": "Remote"
        }
    ]
    return render_template("jobs.html", jobs=job_list)

if __name__ == "__main__":
    app.run(debug=True)