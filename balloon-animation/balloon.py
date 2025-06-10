from graphics import Canvas
import random
import time

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BALLOON_COLORS = [ "#FF0000",   "#00FF00",  "#0000FF",  "#FFFF00", "#FF00FF", "#00FFFF",  "#FFA500", 
    "#FF1493",  "#7CFC00",  "#1E90FF", "#FF4500",  "#00FA9A",  "#DC143C", "#8A2BE2",  
    "#FF69B4",  "#ADFF2F",  "#FF6347",  "#00BFFF",  "#FFD700",  "#40E0D0",  "#FF00FF",  
    "#00FF7F",  "#FF8C00",  "#BA55D3",  "#32CD32",  "#FF6F61",  "#20B2AA",  "#FF3030",  
    "#00CED1",  "#FF1CAE" ]
GROUND_HEIGHT = 60
NUM_BALLOONS = 5

class Balloon:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = random.randint(40, 60)
        self.height = self.width * 1.5
        self.x = random.randint(50, CANVAS_WIDTH - 50)
        self.y = CANVAS_HEIGHT - GROUND_HEIGHT
        self.speed = random.uniform(0.8, 2.5)
        self.color = random.choice(BALLOON_COLORS)
        
        # Creating balloon (oval) and string (rectangle)
        self.oval = canvas.create_oval(
            self.x, 
            self.y - self.height,
            self.x + self.width,
            self.y,
            self.color
        )
        self.string = canvas.create_rectangle(
            self.x + self.width/2 - 1,
            self.y,
            self.x + self.width/2 + 1,
            self.y + self.height/3,
            "black"
        )

    def update(self):
        # Moving balloon upward
        self.y -= self.speed
        self.canvas.moveto(self.oval, self.x, self.y - self.height)
        self.canvas.moveto(self.string, 
                          self.x + self.width/2 - 1, 
                          self.y)
        
        # Checking if balloon is off-screen
        return self.y + self.height < 0

    def delete(self):
        self.canvas.delete(self.oval)
        self.canvas.delete(self.string)

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Creating ground
    canvas.create_rectangle(0, CANVAS_HEIGHT - GROUND_HEIGHT, 
                           CANVAS_WIDTH, CANVAS_HEIGHT, 
                           "brown")
    
    balloons = []
    
    try:
        while True:
            # Creating new balloons if we have less than 3
            if len(balloons) < NUM_BALLOONS and random.random() < 0.05:
                balloons.append(Balloon(canvas))
            
            # Updating existing balloons
            to_remove = []
            for i, balloon in enumerate(balloons):
                if balloon.update():
                    balloon.delete()
                    to_remove.append(i)
            
            # Removing off-screen balloons
            for i in reversed(to_remove):
                balloons.pop(i)
            
            time.sleep(0.016) 
    except KeyboardInterrupt:
        print("Animation stopped")
        canvas.mainloop()

if __name__ == "__main__":
    main()
