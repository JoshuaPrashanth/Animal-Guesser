# Guess_animal.py
from animal_data import get_animals_data  # Import the animal data function from the new file

class AnimalGuesser:
    def __init__(self):
        # Get the animal data from the imported function
        self.animals = get_animals_data()

    def start_game(self):
        print("Think of an animal, and I'll try to guess it!")
        self.ask_question(self.animals)

    def ask_question(self, remaining_animals):
        # List of questions and corresponding attributes
        questions = [
            ('Is it a mammal?', 'mammal'),
            ('Is it a carnivore?', 'carnivore'),
            ('Does it live on land?', 'lives_on_land'),
            ('Does it have wings?', 'has_wings'),
            ('Does it have feathers?', 'feathers'),
            ('Does it have fur or hair?', 'fur_or_hair'),
            ('Is it warm-blooded?', 'warm_blooded'),
            ('Is it a herbivore?', 'herbivore'),
            ('Is it an omnivore?', 'omnivore'),
            ('Does it live in water?', 'lives_in_water'),
            ('Can it fly?', 'fly'),
            ('Is it a reptile?', 'reptile'),
            ('Is it an amphibian?', 'amphibian'),
            ('Is it a fish?', 'fish'),
            ('Is it domesticated?', 'domesticated'),
            ('Is it a wild animal?', 'wild'),
            ('Is it a vertebrate?', 'vertebrate'),
            ('Is it an insect?', 'insect'),
            ('Is it a predator?', 'predator'),
            ('Is it prey?', 'prey')
        ]

        # Ask questions and filter animals based on responses
        for question, attribute in questions:
            if len(remaining_animals) <= 1:
                break

            answer = input(question + " (yes/no) ").strip().lower()
            
            while answer not in ['yes', 'no']:
                print("Please respond with 'yes' or 'no'.")
                answer = input(question + " (yes/no) ").strip().lower()

            if answer == 'yes':
                remaining_animals = {animal: attributes for animal, attributes in remaining_animals.items() if attributes.get(attribute, False)}
            else:
                remaining_animals = {animal: attributes for animal, attributes in remaining_animals.items() if not attributes.get(attribute, False)}

        # If only one animal remains, make a guess
        if len(remaining_animals) == 1:
            self.guess_animal(list(remaining_animals.keys())[0])
        else:
            print("I'm not sure which animal it is! Maybe you can try again with different answers.")

    def guess_animal(self, guessed_animal):
        print(f"I guess the animal is a {guessed_animal}!")
        self.play_again()

    def play_again(self):
        response = input("Do you want to play again? (yes/no) ").strip().lower()
        while response not in ['yes', 'no']:  # Handle invalid input for play again
            print("Please respond with 'yes' or 'no'.")
            response = input("Do you want to play again? (yes/no) ").strip().lower()

        if response == 'yes':
            self.start_game()
        else:
            print("Thanks for playing! Goodbye.")

# Create a game instance and start the game
game = AnimalGuesser()
game.start_game()
