def setup():
    global x, y, z, i, bg
    size(1280, 720, P3D)
    background(0)
    ambientLight(255, 255, 255)
    frameRate(16)
    shininess(5.0)
    x = width/2
    y = height/2
    z = 0
    i = 1
    bg = 255
    
def draw():
    global x, y, z, i, bg
    if mousePressed:
        bg = 250
        background(bg)
    else:
        if bg <= 125:
            bg = 0
        else:
            bg -= 125
        background(bg)
    pushMatrix()
    translate(x, y, z)
    rotateY(PI / 1000 + i)
    stroke(i, random(i, 2 * i), random(i, 3 * i))
    noFill()
    sphere(250)
    popMatrix()
    pushMatrix()
    translate(x, y, z)
    rotateY(PI/4 * i)
    rotateX(PI/5 * i)
    noStroke()
    fill(random(160, 255), random(0, 255), random(0, 255), random(0, 30 + i))
    box(200)
    popMatrix()
    i += 1
    pushMatrix()
    translate(x, y, z)
    rotateY(PI/4 * random(i, 2 * i))
    rotateX(PI/5 * random(i, 2 * i))
    noStroke()
    fill(random(0, 255), random(160, 255), random(0, 255), random(0, 30 + 2 * i))
    box(200)
    popMatrix()
    i += 1
    pushMatrix()
    translate(x, y, z)
    rotateY(PI/4 * random(i, 3 * i))
    rotateX(PI/5 * random(i, 3 * i))
    noStroke()
    fill(random(0, 255), random(0, 255), random(160, 255), random(0, 30))
    box(200)
    popMatrix()
    i += 1
    if i > 80:
        i = 1
