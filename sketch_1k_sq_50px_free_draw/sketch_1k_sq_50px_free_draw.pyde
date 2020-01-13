def setup():
    size(1000, 1000)

def draw():
    if mousePressed:
        fill(0)
        ellipse(mouseX, mouseY, 80, 80)
