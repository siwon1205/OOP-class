# Task 1
class character:
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print(f"{self.name}'s new level: {self.level}")

# Task 2
kung_fu_panda = character("Kung Fu Panda", "Skadoosh", "You have been blinded by pure awesomeness!")
spiderman = character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood Spiderman")

# Task 3
kung_fu_panda.speak(1)
# Make Spiderman a level 2 character
spiderman.setLevel(2)
# Tell Spiderman to say their secondary catchphrase
spiderman.speak(2)
