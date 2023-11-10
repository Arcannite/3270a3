
def read_grid_mdp_problem_p1(file_path):
    #Your p1 code here
    problem = ''
    with open(file_path, 'r') as f:
        problem = f.read()
    lines = problem.split("\n")
    seed = int(lines[0].split("seed: ")[1])
    noise = float(lines[1].split("noise: ")[1])
    living_reward = float(lines[2].split("livingReward: ")[1])
    # the remaining lines are for grid and policy
    # we know that there is the same number of lines describing the grid
    # as the number of lines describing the policy
    grid_height = int((len(lines)-3) /2) -1

    # there are uneven numbers of spaces between each token,
    # a special function must be employed to parse each line
    def parse_token(line):
        # any plaintext between whitespaces is counted as a token
        current_token = ''
        tokens = []
        for char in line:
            if char != ' ':
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                current_token = ''

        # to append the last token
        if current_token:
            tokens.append(current_token)
        current_token = ''

        return tokens

    grid = [parse_token(line) for line in lines[4 : 4+grid_height]]
    policy = [parse_token(line) for line in lines[4+grid_height+1 : ]]

    return seed, noise, living_reward, grid, policy

def read_grid_mdp_problem_p2(file_path):
    #Your p2 code here
    problem = ''
    return problem

def read_grid_mdp_problem_p3(file_path):
    #Your p3 code here
    problem = ''
    return problem

def read_grid_mdp_problem_p4(file_path):
    #Your p4 code here
    problem = ''
    return problem