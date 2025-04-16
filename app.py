from flask import Flask
from flask import render_template
from data import calc_data

app = Flask(__name__)


# Step 1.2: Add the route decorator for the home function
@app.route('/')
def home():
    # Fetch the churn prediction data using calc_data()
    avg_churn_prob, high_risk_customers, churn_rate_by_state, high_risk_by_state = calc_data()

    # Render the index.html template with the necessary data
    return render_template("index.html",
                           avg_churn_prob=avg_churn_prob,
                           high_risk_customers=high_risk_customers,
                           churn_rate_by_state=churn_rate_by_state.to_dict(orient='records'),
                           high_risk_by_state=high_risk_by_state.to_dict(orient='records')
                           )


if __name__ == "__main__":
    # Start the Flask application in debug mode
    app.run(debug=True)
