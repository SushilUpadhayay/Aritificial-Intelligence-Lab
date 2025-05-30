import random
class RoomCleanerAgent:
    def __init__(self, room_size=(10, 10)):
        self.room_size = room_size
        # Initialize the room as a 10x10 grid with random 0 (clean) and 1 (dirty) cells
        self.grid = [[random.choice([0, 1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
        # Initialize the agent's position randomly
        self.current_position = (random.randint(0, room_size[0] - 1), random.randint(0, room_size[1] - 1))

    def display_room(self):
        # Display the current status of the room grid
        for row in self.grid:
          for cell in row:
            print(str(cell), end = '')
          print("\n")

    def perceive(self):
        # Perceive the cleanliness of the current cell
        x, y = self.current_position
        return self.grid[x][y]

    def act(self):
        # Perform action based on the perception (clean the cell if dirty)
        x, y = self.current_position
        if self.perceive() == 1:  # If the current cell is dirty (1)
            print(f"Cell ({x}, {y}) is Dirty. Cleaning...")
            self.grid[x][y] = 0  # Clean the cell (set to 0)
            print(f"Cell ({x}, {y}) is now Clean.")
        else:
            print(f"Cell ({x}, {y}) is already Clean.")

    def move(self):
        # Systematic movement to cover the entire grid row by row
        x, y = self.current_position
        if y < self.room_size[1] - 1:  # Move to the next cell in the same row
            self.current_position = (x, y + 1)
        elif x < self.room_size[0] - 1:  # Move to the first cell of the next row
            self.current_position = (x + 1, 0)
        else:
            self.current_position = None  # All cells have been visited

    def is_room_clean(self):
        # Check if the entire room is clean
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        # Display initial status of the room
        print("Initial Room Status:")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            print(f"\nStep {steps + 1}:")
            self.act()
            self.move()
            steps += 1
            if self.current_position is None:
                # Restart from the top-left corner if needed to ensure all cells are visited
                self.current_position = (0, 0)

        # Display final status of the room
        print("\nFinal Room Status:")
        self.display_room()
        print(f"Room cleaned in {steps} steps.")

# Create and run the Room Cleaner Agent
agent = RoomCleanerAgent()
agent.run()
