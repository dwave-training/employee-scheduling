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
from collections import defaultdict

# Problem information
# TODO: Add new employees to list
employees = ["Anna", "Bill", "Chris", "Diane"]
shifts = [1, 2, 3, 4]
num_shifts = len(shifts)

# Initialize the DQM object
dqm = DiscreteQuadraticModel()

# Build the DQM starting by adding variables
for name in employees:
    dqm.add_variable(num_shifts, label=name)

# Use linear weights to assign employee preferences
dqm.set_linear("Anna", [1,2,3,4])
dqm.set_linear("Bill", [3,2,1,4])
dqm.set_linear("Chris", [4,2,3,1])
dqm.set_linear("Diane", [4,1,2,3])

# TODO: Add additional employees starting on the next line

# Initialize the DQM solver
sampler = LeapHybridDQMSampler()

# Solve the problem using the DQM solver
sampleset = sampler.sample_dqm(dqm)

# Get the first solution, and print it
sample = sampleset.first.sample
energy = sampleset.first.energy

shift_schedule=[ [] for i in range(num_shifts)]

# Interpret according to shifts
for key, val in sample.items():
    shift_schedule[val].append(key)

for i in range(num_shifts):
    print("Shift:", shifts[i], "\tEmployee(s): ", shift_schedule[i])