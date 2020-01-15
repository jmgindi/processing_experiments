def setup():
    size(1024, 1024)
    background(0)
    
    #draw stars
    for i in range(1000):
        center = (random(0, 1024), random(0, 1024))

        noStroke()
        fill(255, 255, 255, random(15, 45))
        for i in range(8):
            circle(center[0], center[1], 4 - i/2)

    #draw planets
    for i in range(5):
        center = (random(0, 1024), random(0, 1024))
        
        noStroke()
        fill(random(30, 105), random(30, 105), random(30, 105), 90)
        z = int(random(5, 15))
        for i in range(z):
            if i == z:
                stroke(255, 255, 255, 20)
            circle(center[0], center[1], z - i)
            
    #draw moon(s)
    for i in range(2):
        if random(1,2) == 2:
            center = random(200, 800)
    save("night_sky.jpg")
