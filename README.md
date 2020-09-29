# The Employee Scheduling Problem

Exercise for D-Wave training courses to demonstrate the DQM solver.

## Exercise 1

We'll be working with the file `scheduling_preferences.py`. This program considers four employees that need to be assigned to four open shifts.  Each employee has a ranking/preference amongst the four shifts according to the image below, where 1 is most preferred and 4 is least preferred.

![Employee preference rankings](scheduling_preferences.png "Employee Preferences")

Open the code file `scheduling_preferences.py` and take a look at how we're building up our discrete quadratic model, or DQM.

1. Initialize the DQM object with `dqm = DiscreteQuadraticModel()`.
2. Add the variables we're using with `dqm.add_variable(...)`.
3. Set the linear biases with `dqm.set_linear(...)`.

Note that this problem does not have any quadratic biases - we're only considering the employees' individual rankings at this time.
