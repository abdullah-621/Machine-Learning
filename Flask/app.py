from flask import Flask, render_template, request
import pickle
app = Flask(__name__, template_folder="templates")
model = pickle.load(open("model/height.pkl", "rb"))

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def pred():
  data = float(request.form.get("height"))
  feature = [[data]]
  prediction = model.predict(feature)

  return render_template("index.html", predicted_data = f"Weight is : {prediction}")

  


if __name__ == "__main__":
  app.run(debug=True)