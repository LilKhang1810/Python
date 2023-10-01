import random
import itertools
from simpleai.search import SearchProblem, genetic
from copy import deepcopy

class RegionColoringProblem(object):

    def __init__(self, regions,color,constraints):
        super().__init__(initial_state=regions)
        self.color = color
        self.constraints = constraints

    def generate_random_state(self):
        # Tạo một trạng thái ngẫu nhiên
        state = dict(
            (region, random.choice(self.color[region]))
            for region in self.color
        )
        return state

    def value(self, state):
        sastified_constraints = list(filter(self.func_constraint_neighbors(state), self.constraints))

        return len(sastified_constraints) / len(self.constraints)

    def crossover(self, state1, state2):
        # Tạo ra một trạng thái mới bằng cách lai hai trạng thái hiện tại
        # (Ví dụ: lai hai màu đỏ và xanh lá cây sẽ tạo ra màu vàng)
        new_state = state1.copy()
        for region in new_state:
            new_state[region] = random.choice([state1[region], state2[region]])
        return new_state

    def mutate(self, state):
        # Tạo ra một trạng thái mới bằng cách đột biến một trạng thái hiện tại
        # (Ví dụ: thay đổi màu của một vùng)
        region = random.choice(list(state.keys()))
        new_color = random.choice(self.regions)
        new_state = state.copy()
        new_state[region] = new_color
        return new_state

    def func_constraint_neighbors(self, regions_state):
        def constraint(regions):
            first_region =  regions[0]
            second_region =  regions[1]
            return regions_state[first_region] != regions_state[second_region] and regions_state[first_region] in self.regions_colors[first_region] and regions_state[second_region] in self.regions_colors[second_region]
        return constraint

regions = {'Mark': None, 'Julia': None, 'Steve': None, 'Amanda': None, 'Brian': None,
           'Joanne': None, 'Derek': None, 'Allan': None, 'Michelle': None, 'Kelly': None, 'Chris': None}

color_avai = dict(
    (region,  ['red', 'green', 'blue', 'yellow']) for region in regions
)
print(regions)
print(color_avai)

constraints = [
    ('Mark', 'Julia'), ('Mark', 'Steve'),

    ('Steve', 'Julia'), ('Steve', 'Amanda'), ('Steve', 'Allan'), ('Steve', 'Michelle'),

    ('Allan', 'Michelle'),

    ('Julia', 'Brian'), ('Julia', 'Derek'), ('Julia', 'Amanda'),

    ('Amanda', 'Derek'), ('Amanda', 'Joanne'), ('Amanda', 'Michelle'),

    ('Michelle', 'Joanne'),

    ('Brian', 'Kelly'), ('Brian', 'Derek'),

    ('Derek', 'Kelly'), ('Derek', 'Chris'), ('Derek', 'Joanne'),

    ('Joanne', 'Chris'),

    ('Kelly', 'Chris'),
]
Coloring = RegionColoringProblem(regions, color_avai, constraints)

print(regions)
result = genetic(Coloring, iterations_limit=1e4)

for region, color in result.state.items():
    print(region, '==>', color)

print(Coloring.value(result.state))

