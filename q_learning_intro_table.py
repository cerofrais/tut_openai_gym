import gym

env = gym.make("MountainCar-v0")
"""
    Mountain car has 3 actions: discrete
    action 0 = pull left
    action 1 = do nothing
    action 2 = push right
    
    States: Continuous 
    position, velocity
    
    Q learning equation :
    https://wikimedia.org/api/rest_v1/media/math/render/svg/47fa1e5cf8cf75996a777c11c7b9445dc96d4637
     
"""

def print_env_config():
    print(env.observation_space.high)
    print(env.observation_space.low)
    print(env.observation_space.high)

env.reset()

done = False

while not done:
    action =2 # pushing car right
    new_state, reward, done, _ = env.step(action)
    # print(new_state) # position, velocity
    env.render()

env.close()

