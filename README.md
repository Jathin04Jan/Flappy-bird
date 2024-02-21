# Flappy Bird AI (Reinforcement Learning)

This project is an implementation of the classic game Flappy Bird using Reinforcement Learning. The AI is trained using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm, which evolves neural networks to play the game effectively.

## About

In this project, the NEAT algorithm is used to train the AI to play the game of Flappy Bird. The AI learns to navigate the bird through gaps in the pipes by predicting the best actions to take based on the current state of the game. The goal is to achieve a high score by avoiding obstacles and staying alive for as long as possible.

## How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip3 install pygame` and 'pip3 install neat-python'.
4. Run the script `flappy_bird.py` by executing `python flappy_bird.py`.

## Game Controls

The game controls are handled by the AI. The AI determines when the bird should jump to avoid obstacles. As a user, you don't have direct control over the bird's actions.

## Game Mechanics

The game is simple: the bird continuously moves forward, and the player (or the AI in this case) has to make the bird jump to avoid obstacles. The player earns points for every obstacle passed. The game ends if the bird collides with an obstacle or falls to the ground.

## Reinforcement Learning

Reinforcement Learning is a type of machine learning in which an agent learns to make decisions by interacting with its environment. In this project, the AI agent learns to play Flappy Bird by receiving feedback (rewards or penalties) based on its actions. Over time, the agent learns to take actions that maximize its rewards.

## NEAT Algorithm

NEAT is used in this implementation to train the AI. It starts with a population of birds with randomly assigned neural networks. Each bird plays the game, and its performance is evaluated. The birds that perform better are selected to breed, and their neural networks are combined and mutated to create the next generation of birds. This process continues until the AI learns to play the game effectively.

## Credits

- The base game implementation is based on the Flappy Bird game created by Dong Nguyen.
- The NEAT algorithm is based on the NEAT-Python library by CodeReclaimers.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
