def setup():
    size(800, 800)
    background(255)
    
    
    for circ in range(400):
        center = (random(100, 700), random(100, 700))
        
        #draw shadow
        noStroke()
        fill(30, 30, 30, 7)
        for i in range(50):
            circle(center[0] + 5, center[1] + 10, 60 - i * 2)
    
        #draw circle
        stroke(0, 0, 0)
        strokeWeight(1)
        fill(random(100, 255), random(100, 255), 150)
        circle(center[0], center[1], 50)
    
    
