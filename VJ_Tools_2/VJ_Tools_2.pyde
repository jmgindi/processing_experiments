def setup():
    global x, y, z, i, bg, m
    size(1280, 720, P3D)
    background(0)
    ambientLight(255, 255, 255)
    frameRate(30)
    shininess(5.0)
    x = width/2
    y = height/2
    z = 0
    i = 1
    bg = 255
    m = 1

def draw():
    global x, y, z, i, bg, m
    scale_m = [1, 1, 1] # [noise(i), noise(i + 250), noise(i + 500)]
    if mousePressed:
        m = 2
        bg = 250
    else:
        m = 1
        if bg <= 125:
            bg = 0
        else:
            bg -= 50

    background(bg)

    pushMatrix()
    translate(x, y, z)
    rotateY(i / 50 + PI * noise(i) / 4)
    rotateX(PI/5)
    rotateZ(PI/4)
    noStroke()
    fill(random(160, 255), random(0, 255), random(0, 255), random(0, 30 * m))
    box(200 * scale_m[0] * m)
    popMatrix()
    i += 1
    pushMatrix()
    translate(x, y, z)
    rotateY(i / 75 + PI * noise(2 * i) / 4)
    rotateX(PI/5)
    rotateZ(PI/4)
    noStroke()
    fill(random(160, 255), random(0, 255), random(0, 255), random(0, 30 * m))
    box(200 * scale_m[0] * m)
    popMatrix()
    i += 1
    pushMatrix()
    translate(x, y, z)
    rotateY(i / 100 + PI * noise(3 * i) / 4)
    rotateX(PI/5)
    rotateZ(PI/4)
    noStroke()
    fill(random(160, 255), random(0, 255), random(0, 255), random(0, 30 * m))
    box(200 * scale_m[0] * m)
    popMatrix()
    i += 1
    if i > 400:
        i = 1
