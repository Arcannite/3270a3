import sys, random, grader, parse
from copy import deepcopy

def play_episode(problem):
    seed, noise, living_reward, grid, policy = problem
    experience = ''
    if seed!=-1:
        random.seed(seed, version=1)
    d = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}

    def walk(direction, n):
        # given the direction that the agent wants to go and noise,
        # return the direction that it will actually go 
        return random.choices(population=d[direction], weights=[1 - n*2, n, n])[0]

    """
    Two parts of the problem
    1. actually solving the problem
    2. printing out the solution

    """
    print(walk("N", noise))

    return experience

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -8
    problem_id = 1
    grader.grade(problem_id, test_case_id, play_episode, parse.read_grid_mdp_problem_p1)