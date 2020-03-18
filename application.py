import requests
from flask import Flask, flash, jsonify, redirect, render_template, request, session

#Change so theres an option for what two currency to look at, change request get so the base is the currency
#to convert from, then search in that JSON for  the currency to convert TO, then export that as data
#Need to add dropdown menus for currency in the form, and display the converted rate better

app = Flask(__name__)
@app.route("/",methods=["Get","POST"])
def index():
	if request.method == "GET":
		return render_template("index.html",data=None)
	if request.method == "POST":
		if not request.form.get("number"):
			return ("Error, enter valid number")
		if not request.form.get("base"):
			return ("Error, enter valid base")
		if not request.form.get("target"):
			return ("Error, enter valid target")
		try:
			number = float(request.form.get("number"))
		except ValueError:
			return ("Error, enter valid number")
		base = request.form.get("base")
		target = request.form.get("target")
		url = str("https://api.exchangeratesapi.io/latest?base="+str(base))
		res = requests.get(url)
		data = res.json()
		rate = data["rates"][target]
		converted = float(rate)*number
		return render_template("index.html", converted=converted)
app.run(debug=False)
# res = requests.get("http://data.fixer.io/api/latest?access_key=5b800ef845f47b03d7fece279dd48065")
# if res.status_code != 200:
# 	raise Exception("ERROR")
# data = res.json()
# print(data)


