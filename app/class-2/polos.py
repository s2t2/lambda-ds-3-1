


class Polo():
    def __init__(size, color):
        self.size = size
        self.color = color

    def pop_collar(self):
        print("Popping the collar")


if __name__ == "__main__":

    polo = Polo(color="Blue", size="L")
    polo.pop_collar()
