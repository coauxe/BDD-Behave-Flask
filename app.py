from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
 	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	try:
		meal_cost = int(request.form["meal_cost"])
		tip_percentage = int(request.form["tip_percentage"])
		tip_cost = int(meal_cost) * (int(tip_percentage)*.01)
		try_again = "Please enter a number greater than 0"
		if meal_cost <= 0 or tip_percentage <= 0:
			return render_template('home.html', again=try_again)
		else:
			return render_template('results.html', meal_cost=meal_cost, tip_percentage=tip_percentage, tip_cost=tip_cost)

	except ValueError:
		try_again = "Please enter a valid number"
		return render_template('home.html', again=try_again)
	

if __name__ == '__main__':
  	app.run(debug=True)