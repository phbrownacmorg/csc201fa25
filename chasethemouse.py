from graphics import *
from math import cos, radians, sin
from typing import cast

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setCoords(-1, -1, 1, 1)
    label: Text = Text(Point(0, .9), "Click for coordinates")
    label.draw(win)

    radius: float = 0.05
    mouse: list[GraphicsObject] = [Circle(Point(0, 0), radius).draw(win)]
    # Ears
    angle: float = radians(60)
    mouse.append(Circle(Point(1.4 * radius * cos(angle),
                              1.4 * radius * sin(angle)), .6 * radius).draw(win))
    mouse.append(Circle(Point(-1.4 * radius * cos(angle),
                              1.4 * radius * sin(angle)), .6 * radius).draw(win))
    for part in mouse: # Head and ears
        part.setFill('darkgray')
        part.setOutline('darkgray')
    # Eyes
    angle = radians(50)
    bottom_x = 0.1
    mouse.append(Oval(Point(radius * bottom_x, 0),
                      Point(radius * (1 - bottom_x) * cos(angle),
                            radius * (1 - bottom_x) * sin(angle))).draw(win))
    mouse.append(Oval(Point(-radius * bottom_x, 0),
                      Point(-radius * (1 - bottom_x) * cos(angle),
                            radius * (1 - bottom_x) * sin(angle))).draw(win))
    for part in mouse[-2:]: # Just the eyes
        part.setFill('black')


    radius = 0.2
    cat: list[GraphicsObject] = [Circle(Point(0, 0), radius).draw(win)]
    # Ears
    # angle is 60 degrees
    earAngle = radians(15)
    cat.append(Polygon(Point(1.6 * radius * cos(angle), 1.6 * radius * sin(angle)),
                       Point(radius * cos(angle-earAngle), radius * sin(angle-earAngle)),
                       Point(radius * cos(angle+earAngle), radius * sin(angle+earAngle))).draw(win))
    cat.append(Polygon(Point(-1.6 * radius * cos(angle), 1.6 * radius * sin(angle)),
                       Point(-radius * cos(angle-earAngle), radius * sin(angle-earAngle)),
                       Point(-radius * cos(angle+earAngle), radius * sin(angle+earAngle))).draw(win))
    for part in cat:
        part.setFill('orange')
        part.setOutline('orange')
    angle = radians(50)
    bottom_x = 0.1
    cat.append(Oval(Point(radius * bottom_x, 0),
                      Point(radius * (1 - bottom_x) * cos(angle),
                            radius * (1 - bottom_x) * sin(angle))).draw(win))
    cat.append(Oval(Point(-radius * bottom_x, 0),
                      Point(-radius * (1 - bottom_x) * cos(angle),
                            radius * (1 - bottom_x) * sin(angle))).draw(win))
    for part in cat[-2:]: # Just the eyes
        part.setFill('green')

    
    for part in cat:
        part.move(2, 0)             # Initially off the screen

    for i in range(6):              # type: ignore
        p: Point = win.getMouse()
        label.setText('Click: ' + str(round(p.getX(), 3)) + ', '
            + str(round(p.getY(), 3)) + '\nClick again')
        
        # Move the mouse to the mouse click
        mousePt: Point = cast(Circle, mouse[0]).getCenter()
        dx: float = p.getX() - mousePt.getX()
        dy: float = p.getY() - mousePt.getY()
        for part in mouse:
            part.move(dx, dy)

        # Move the cat to where the mouse just was
        catPt: Point = cast(Circle, cat[0]).getCenter()
        dx = mousePt.getX() - catPt.getX()
        dy = mousePt.getY() - catPt.getY()
        for part in cat:
            part.move(dx, dy)

    label.setText(label.getText() + ' to exit')
    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
