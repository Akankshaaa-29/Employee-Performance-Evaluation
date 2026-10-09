# Employee Performance Evaluation System

## About the Project
This project predicts employee performance levels using machine learning. It uses employee experience, attendance, completed projects, and manager ratings to classify performance as Low, Medium, or High.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Flask
- HTML and CSS
- Jupyter Notebook

## Project Features
- Predicts employee performance using a trained Logistic Regression model.
- Provides a web-based dashboard using Flask.
- Validates user inputs before generating predictions.
- Uses a CSV dataset for model training.

## Project Structure
- `app.py` — Flask application
- `employee_performance.csv` — Sample dataset
- `employee_performance_model.pkl` — Trained model
- `templates/index.html` — Dashboard interface
- `Employee_Performance_Evaluation.ipynb2.ipynb` — Jupyter Notebook

## How to Run
1. Install the required Python libraries: `flask`, `pandas`, and `scikit-learn`.
2. Ensure all project files are in the same project folder and the HTML file is inside `templates`.
3. Run `python app.py` from the project folder.
4. Open `http://127.0.0.1:5000` in your browser.

## Dataset Note
This project currently uses a small sample dataset of 10 records. Predictions are for demonstration and learning purposes, not real-world employee evaluation.

## Future Improvements
- Train and evaluate the model using a larger dataset.
- Improve model evaluation and prediction reliability.
- Add employee records and performance visualizations.
