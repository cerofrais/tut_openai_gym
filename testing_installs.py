from gym import envs
import gym


def gym_install_test():
    env = gym.make('CartPole-v0')
    env.reset()


    for _ in range(100):
        env.render()
        env.step(env.action_space.sample())



if __name__ == '__main__':
    gym_install_test()

