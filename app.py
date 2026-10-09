from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load trained ML model
with open("employee_performance_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            experience = float(request.form["experience"])
            attendance = float(request.form["attendance"])
            projects = int(request.form["projects"])
            rating = float(request.form["rating"])

            if experience < 0:
                raise ValueError("Experience cannot be negative.")
            if not 0 <= attendance <= 100:
                raise ValueError("Attendance must be between 0 and 100.")
            if projects < 0:
                raise ValueError("Projects cannot be negative.")
            if not 1 <= rating <= 5:
                raise ValueError("Rating must be between 1 and 5.")

            employee = pd.DataFrame([{
                "experience_years": experience,
                "attendance_percent": attendance,
                "projects_completed": projects,
                "manager_rating": rating
            }])

            prediction = model.predict(employee)[0]

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
