t = 0
n = 90

def setup():
    size(1920, 1080)
    fullScreen()
    background(0)
    frameRate(60)
    strokeWeight(2)
    noFill()
    
    
def draw():
    global t, n

    background(0)
    translate(width / 2, height / 2)
    
    for i in range(n):
        rotate(radians(360/n))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t))
        stroke(i*3, 0, 255)
        square(width / 4, height / 4, 200)
        stroke(0, 255, i*3)
        tri(300)
        popMatrix()
    
    t += 1
    
def tri(length):
    triangle(0,
             -length,
             -length * sqrt(3) / 2,
             length / 2,
             length * sqrt(3) / 2,
             length / 2)
