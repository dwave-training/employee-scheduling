[![Open in Leap IDE](	
	https://cdn-assets.cloud.dwavesys.com/shared/latest/badges/leapide.svg)](
	https://ide.dwavesys.io/#https://github.com/dwave-training/employee-scheduling)

# The Employee Scheduling Problem

Exercise for D-Wave training courses to demonstrate the CQM solver.

## Exercise 1

We'll be working with the file `scheduling_preferences.py`. This program considers four employees that need to be assigned to four open shifts.  Each employee has a ranking/preference amongst the four shifts according to the image below, where 1 is most preferred and 4 is least preferred.

![Employee preference rankings](scheduling_preferences.png "Employee Preferences")

Open the code file `scheduling_preferences.py` and take a look at how we're building up our constrained quadratic model, or CQM.

1. Initialize the CQM object with `cqm = ConstrainedQuadraticModel()`.
2. Create labels for binary variables for each employee in each shift.
3. Add discrete constraints over employee binaries for each employee with `cqm.add_discrete(...)`.
4. Add objective terms as linear biases based on the employee preferences with `cqm.objective.add_linear_from(...)`.

## Exercise 2

For this exercise, we'll work with the file `scheduling_addemployees.py`. This file is very similar to `scheduling_preferences.py`, and you will be adding additional employees to the schedule.  Add the following employees with their associated preferences for shifts 1-4 in the function `employee_preferences()`. 

1. Erik: [1,3,2,4]
2. Francis: [4,3,2,1]
3. Greta: [2,1,4,3]
4. Harry: [3,2,1,4]

When you run this problem, you should see two employees scheduled for each shift.

## Exercise 3

In this next exercise, we'll work with the file `scheduling_restrictions.py`. In this problem, we have 8 employees and 4 different shift options.  We've set up the initial CQM model for all 8 employees with their preferences over the 4 shifts. Now we need to take into account the following restrictions.

1. Anna is not able to work during shift 4.
2. Bill and Frank cannot work during the same shift.
3. Erica and Harriet would like to work the same shift.

Modify the function `build_cqm()` to reflect these additional constraints. Note that when you run your program, you may not have two employees per shift this time.

## Challenge: Exercise 4

For this final exercise, start with your completed file `scheduling_restrictions.py` from Exercise 3.  The optimal solution for Exercise 3 had some days with just 1 person scheduled and others with many more.  Add some linear and/or quadratic biases to your CQM so that each shift gets exactly two people scheduled.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
