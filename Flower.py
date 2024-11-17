class Flower:
    def __init__(self, name):
        self.name = name
        # adding the name of the flower

    def grow(self):
        print("The " +self.name + " is growing.")
        # this makes the code print a message when the flower grows

    def bloom(self):
        print("The " + self.name + " is blooming.")
        # This prints a message when the flower blooms

def main():
    flower1 = Flower("Rose") # Making a Flower object named flower1 with name "Rose"
    flower1.grow() # Making the call for the grow method for flower1
    flower1.bloom() # Making the call the bloom method for flower1
    flower2 = Flower("Daisy") # Another Flower object named flower2 with the name "Daisy"
    flower2.grow() # Making the call for the grow method for flower2
    flower2.bloom() # Making the call the bloom method for flower2
    
    flower3 = Flower("Tulip")  # added a third Flower object named flower3 with name "Tulip"
    flower3.grow()  # The call for the grow method for flower3
    flower3.bloom()  # the call for the bloom method for flower3

if __name__ == "__main__":
  main() # This will run the main function when this script is executed