# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimod import ConstrainedQuadraticModel
from dwave.system import LeapHybridCQMSampler

def get_token():
    '''Returns personal access token. Only required if submitting to autograder.'''
    
    # TODO: Enter your token here
    return 'YOUR-TOKEN-HERE'

# Set the solver we're going to use
def set_sampler():
    '''Returns a dimod sampler'''

    sampler = LeapHybridCQMSampler()

    return sampler

# Set employees and preferences
def employee_preferences():
    '''Returns a dictionary of employees with their preferences'''

    preferences = { "Anna": [1,2,3,4],
                    "Bill": [3,2,1,4],
                    "Chris": [4,2,3,1],
                    "Diane": [4,1,2,3]}

    return preferences

# Create CQM object
def build_cqm():
    '''Builds the CQM for our problem'''

    preferences = employee_preferences()
    num_shifts = 4

    # Initialize the CQM object
    cqm = ConstrainedQuadraticModel()

    # Represent shifts as a set of binary variables for each employee
    for employee, preference in preferences.items():
        # Create labels for binary variables
        labels = [f"x_{employee}_{shift}" for shift in range(num_shifts)]
    
        # Add a discrete constraint over employee binaries
        cqm.add_discrete(labels, label=f"discrete_{employee}")

        # Incrementally add objective terms as list of (label, bias)
        cqm.objective.add_linear_from([*zip(labels, preference)])

    return cqm

# Solve the problem
def solve_problem(cqm, sampler):
    '''Runs the provided cqm object on the designated sampler'''

    # Initialize the CQM solver
    sampler = set_sampler()

    # Solve the problem using the CQM solver
    sampleset = sampler.sample_cqm(cqm, label='Training - Employee Scheduling')

    return sampleset

## ------- Main program -------
if __name__ == "__main__":

    # Problem information
    shifts = [1, 2, 3, 4]

    cqm = build_cqm()

    sampler = set_sampler()

    sampleset = solve_problem(cqm, sampler)

    # Get the first solution, and print it
    sample = sampleset.first.sample
    energy = sampleset.first.energy

    # Interpret according to shifts
    for key, val in sample.items():
        if val ==1.0:
            name = key.split('_')[1]
            shift = int(key.split('_')[2])
            print("Schedule", name, "for shift", shifts[shift])
