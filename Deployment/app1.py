from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model/price.pkl", "rb"))


@app.route("/")
def welcome():
  return "<h1>Welcome to this page</h1>"

@app.route("/new")
def new():
  return "<h1>Welcome to this new page</h1>"


@app.route("/calculate", methods = ["GET", "POST"])
def calculate():

  prediction = None


  if request.method == "POST":
    area = float(request.form.get("area"))
    bedrooms = float(request.form.get("bedrooms"))
    bathrooms = float(request.form.get("bathrooms"))
    feature = [[area, bedrooms, bathrooms]]
    prediction = model.predict(feature)[0]

  return render_template("index1.html", predicted_data = f"price is : {prediction}")

if __name__ == "__main__":
  app.run(debug=True)