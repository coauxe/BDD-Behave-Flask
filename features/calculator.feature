Feature: Confirming that the tip calculator form works

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator 

	Scenario: check that the form submits successfully
		When I go to the tip calculator
    	And I submit the form with a valid total and tip percentage
    	Then I should see the results page

    Scenario: check to see if meal total is correct
    	When I go to the tip calculator
    	And I submit the form with a valid total and tip percentage
    	Then I should see the correct tip amount

    Scenario: check to see if edge cases are handled
        When I go to the tip calculator
        And I enter an invalid number
        Then I should see a message and the home page