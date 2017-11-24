from agent import Agent
from environment import Environment

class Evolution:
    # Evolution engine.
    #
    # === Attributes ===
    # num_generations: The number of generations to run evolution
    #   for.
    # population_size: The size of the poputation.
    # agents: List of agents, i.e. the population, w/ size
    #   <population_size>

    def __init__(self, num_generations, population_size):
        self.num_generations = num_generations
        self.population_size = population_size
        self.agents = []

    def run(self):
        # Initialize population randomly
        self.agents = self.random_agents(self.population_size)

        for i in range(self.num_generations):
            environment = Environment()
            # TODO: evaluate population against said environment
            # TODO: pick some subset that performed better
            # TODO: expand subset to new population

            # Log generation to screen
            if (i % 10 == 0):
                print(i)

    def random_agents(self, population_size):
        # TODO: implement this method, use list comprehension?
        return []

    def evaluate_population(self, environment):
        # evaluate each agent's fitness in the environment
        return []

    def evaluate_agent(self, agent, environment):
        # evaluate an agent's fitness in the environment
        pass

if __name__ == '__main__':
    evolution = Evolution(1, 1)
    evolution.run()
