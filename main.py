from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined exchange rates (example values, update as needed)
exchange_rates = {
    "USD": 83.12,  # 1 USD = 83.12 INR
    "EUR": 90.45,  # 1 EUR = 90.45 INR
    "GBP": 104.32, # 1 GBP = 104.32 INR
    "AUD": 55.23,  # 1 AUD = 55.23 INR
    "CAD": 61.34,  # 1 CAD = 61.34 INR
    "JPY": 0.55,   # 1 JPY = 0.55 INR
    "CNY": 11.75   # 1 CNY = 11.75 INR
}

@app.route("/", methods=["GET", "POST"])
def home():
    conversion_result = None
    if request.method == "POST":
        from_currency = request.form.get("from_currency").upper()
        
        if from_currency in exchange_rates:
            inr_rate = exchange_rates[from_currency]
            conversion_result = f"1 {from_currency} = {inr_rate} INR"
        else:
            conversion_result = "Invalid currency code. Try USD, EUR, GBP, etc."

    return render_template("index.html", result=conversion_result)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
