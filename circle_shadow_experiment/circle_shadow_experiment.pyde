def setup():
    size(800, 800)
    background(255)
    
    
    for h in range(400):
        center = (random(100, 700), random(100, 700))
        
        
        #draw shadow
        noStroke()
        fill(30, 30, 30, 7)
        for i in range(50):
            circle(center[0] + 5, center[1] + 10, (h / 25) + (60 - i * 2))
    
        #draw circle
        stroke(0, 0, 0)
        strokeWeight(1)
        fill(random(80, 160), random(100, 255), 180)
        circle(center[0], center[1], (h / 25) + 50)
    
    save("circle_shadows.jpg")
    
