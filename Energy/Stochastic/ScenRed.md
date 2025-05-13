# Scenario Reduction

## scenario reduction
### backward reduction
delete least important scenarios one by one
- step 1: select scenario with smallest distance to other scenario
- step 2: merge and update scenario weights
- step i: go to step 1 again

### fast forward selection
keep most important scenarios one by one
- step 1:
    - determine the scenario that can represent all scenarios with the min probability distance
    - keep that scenario
- step i:
    - for each remaining scenarios, calculate the min probability distance to other remaining scenarios
    - keep that scenario as well
- do util the number of scenarios to keep reached the provided number

## scenario tree
2003: https://www.wias-berlin.de/people/heitsch/ieee03ghr.pdf
- relative accuracy: eq. (1)
    - when only one scenario is kept, the loss is 100%
    - so use that scenario with the minimum sum prob distance as a base reference
    - when a scenario linked to a deleted scenario is to be deleted, we must update the distance of the deleted scenario to new preserved scenario set
    - as the distance increases so the total loss
- optimal reduction problem:
    - minimize the total min distance between all deleted scenarios to the remaining scenarios
    - each deleted scenario will be merged to one of the remaining scenarios with the shortest distance
    - the sum(p_j * d_ji) is the information loss
- probability redistribution: eq.(2)
    - all deleted scenarios will be merged to one of the scenarios in the remaining set with the shortest distance

## code
c++ version
- https://github.com/Jonas-eng/scenred/issues/1
- https://github.com/Jonas-eng/scenred/blob/master/scenario_reduction_c.pyx

python version (fast forward selection):
- https://github.com/DanieleGioia/ScenarioReducer/blob/main/main_example.py

scenario tree
- https://gitlab.com/supsi-dacd-isaac/scenred
  
## papaers
- 2000: Scenario reduction in stochastic programming: An approach using probability metrics
  https://edoc.hu-berlin.de/bitstream/handle/18452/8896/20.pdf?sequence=1

- 2003: Scenario Reduction and Scenario Tree Construction for Power Management Problems
  https://www.wias-berlin.de/people/heitsch/ieee03ghr.pdf

- 2003: Scenario reduction algorithms in stochastic programming
  - https://edoc.hu-berlin.de/server/api/core/bitstreams/ed72ccea-3fd6-4e4b-8975-53a27184c758/content
  - backward reduction: eq.(12)
  - forward reduction: eq.(13)

- 2008: Scenario tree modelling for multistage stochastic programs
  https://edoc.hu-berlin.de/server/api/core/bitstreams/7f0e1eb1-ca9b-42d5-a213-97b1c0b71764/content

- 2009: Scenario reduction for futures market trading in electricity markets
  https://pdfs.semanticscholar.org/6b05/95e54011b6925647adbf837ebb30f77f29d9.pdf
