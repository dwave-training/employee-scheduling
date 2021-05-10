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

from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler

def get_token():
    '''Return your personal access token'''
    
    # TODO: Enter your token here
    return 'YOUR-TOKEN-HERE'

# Set the solver we're going to use
def set_sampler():
    '''Returns a dimod sampler'''

    sampler = LeapHybridDQMSampler()

    return sampler

# Set employees and preferences
def employee_preferences():
    '''Returns a dictionary of employees with their preferences'''

    preferences = { "Anna": [1,2,3,4],
                    "Bill": [3,2,1,4],
                    "Chris": [4,2,3,1],
                    "Diane": [4,1,2,3]}

    return preferences

# Create DQM object
def build_dqm():
    '''Builds the DQM for our problem'''

    preferences = employee_preferences()
    num_shifts = 4

    # Initialize the DQM object
    dqm = DiscreteQuadraticModel()

    # Build the DQM starting by adding variables
    for name in preferences:
        dqm.add_variable(num_shifts, label=name)

    # Use linear weights to assign employee preferences
    for name in preferences:
        dqm.set_linear(name, preferences[name])

    return dqm

# Solve the problem
def solve_problem(dqm, sampler):
    '''Runs the provided dqm object on the designated sampler'''

    # Initialize the DQM solver
    sampler = set_sampler()

    # Solve the problem using the DQM solver
    sampleset = sampler.sample_dqm(dqm, label='Training - Employee Scheduling')

    return sampleset

## ------- Main program -------
if __name__ == "__main__":

    # Problem information
    shifts = [1, 2, 3, 4]

    dqm = build_dqm()

    sampler = set_sampler()

    sampleset = solve_problem(dqm, sampler)

    # Get the first solution, and print it
    sample = sampleset.first.sample
    energy = sampleset.first.energy

    # Display sample information
    print(sample, energy, "\n")

    # Interpret according to shifts
    for key, val in sample.items():
        print("Schedule", key, "for shift", shifts[val])
