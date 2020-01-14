def setup():
    size(1024, 1024)
    background(0)
    
    for i in range(1000):
        center = (random(0, 1024), random(0, 1024))
        
        #draw stars
        noStroke()
        fill(255, 255, 255, random(15, 45))
        for i in range(8):
            circle(center[0], center[1], 4 - i/2)
