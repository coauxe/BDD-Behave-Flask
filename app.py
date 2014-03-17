from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
 	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	try:
		meal_cost = request.form["meal_cost"]
		tip_percentage = request.form["tip_percentage"]
		tip_cost = int(meal_cost) * (int(tip_percentage)*.01)
		return render_template('results.html', meal_cost=meal_cost, tip_percentage=tip_percentage, tip_cost=tip_cost)
	except ValueError:
		try_again = "Please enter a valid number"
		return render_template('home.html', again=try_again)
if __name__ == '__main__':
  	app.run(debug=True)