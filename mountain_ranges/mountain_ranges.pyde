def setup():
    size(1024, 1024)
    background(20)
    start_x = 0
    start_y = 0
    for l in range(128):
        stroke(l + 40)
        strokeWeight(3)
        fill(l + 20)
        beginShape()
        vertex(0, 1024)
        for cvert in range(65):
            yvert = random(0, 50)
            vertex(cvert * 16, start_y - yvert)
        vertex(1024, 1024)
        endShape()
        start_y += 20
    
    
