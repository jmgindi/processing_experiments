def setup():
    size(1024, 1024)
    background(0)
    loadPixels()
    noiseDetail(5)
    xoff = 0.0
    for x in range(width):
        yoff = 0.0
        for y in range(height):
            bright = map(noise(xoff, yoff), 0, 1, 0, 200)
            #ocean
            if bright >= 60:
                 pixels[x + y * width] = color(60, 100, 200)
            elif 57 < bright < 60:
                 pixels[x + y * width] = color(223, 204, 175)
            #mountains
            elif 30 < bright < 40:
                 pixels[x + y * width] = color(65, 43, 21)
            #snow caps
            elif bright <= 30:
                 pixels[x + y * width] = color(255)
            #grass
            else:
                 pixels[x + y * width] = color(30, 180, 65)
           
            yoff += 0.01
        xoff += 0.01
    updatePixels()
    
    save("map.jpg")
