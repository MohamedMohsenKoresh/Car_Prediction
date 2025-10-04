from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# تحميل النموذج
model = pickle.load(open("car_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        year = int(request.form["year"])
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["kms_driven"])
        fuel_type = int(request.form["fuel_type"])
        seller_type = int(request.form["seller_type"])
        transmission = int(request.form["transmission"])
        owner = int(request.form["owner"])

        # Predict
        prediction_value = model.predict([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])
        prediction = round(prediction_value[0], 2)
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
