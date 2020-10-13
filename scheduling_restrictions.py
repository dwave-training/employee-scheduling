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

    token = get_token()
    sampler = LeapHybridDQMSampler(endpoint='https://cloud.dwavesys.com/sapi/', 
                                              token=token)

    return sampler

# Create DQM object
def build_dqm(preferences, shifts):
    '''Builds the DQM for our problem'''

    num_shifts = len(shifts)

    # Initialize the DQM object
    dqm = DiscreteQuadraticModel()

    # Build the DQM starting by adding variables
    for name in preferences:
        dqm.add_variable(num_shifts, label=name)

    # Use linear weights to assign employee preferences
    for name in preferences:
        dqm.set_linear(name, preferences[name])

    # TODO: Restrict Anna from working shift 4

    # TODO: Set some quadratic biases to reflect the restrictions in the README.

    return dqm

# Solve the problem
def solve_problem(dqm, sampler):

    # Initialize the DQM solver
    sampler = LeapHybridDQMSampler()

    # Solve the problem using the DQM solver
    sampleset = sampler.sample_dqm(dqm)

    return sampleset

# Process solution
def process_sampleset(sampleset):
   
    # Get the first solution
    sample = sampleset.first.sample

    shift_schedule=[ [] for i in range(num_shifts)]

    # Interpret according to shifts
    for key, val in sample.items():
        shift_schedule[val].append(key)

    return shift_schedule

## ------- Main program -------
if __name__ == "__main__":

    # Problem information
    preferences = { "Anna": [1,2,3,4],
                    "Bill": [3,2,1,4],
                    "Chris": [4,2,3,1],
                    "Diane": [4,1,2,3],
                    "Erica": [1,2,3,4],
                    "Frank": [3,2,1,4],
                    "George": [4,2,3,1],
                    "Harriet": [4,1,2,3]}
    shifts = [1, 2, 3, 4]
    num_shifts = len(shifts)

    dqm = build_dqm(preferences, shifts)

    sampler = set_sampler()

    sampleset = solve_problem(dqm, sampler)

    shift_schedule = process_sampleset(sampleset)

    for i in range(num_shifts):
        print("Shift:", shifts[i], "\tEmployee(s): ", shift_schedule[i])
