from graphics import *
from math import cos, hypot, radians, sin
from typing import cast

def separation(p1: Point, p2: Point) -> float:
    return hypot(abs(p1.getX() - p2.getX()), abs(p1.getY() - p2.getY()))
    # dx = abs(p1.getX() - p2.getX())
    # dy = abs(p1.getY() - p2.getY())
    # return sqrt(dx*dx + dy*dy)

def make_button(p1: Point, p2: Point, text: str, w: GraphWin) -> Rectangle:
    button = Rectangle(p1, p2).draw(w)
    label = Text(cast(Rectangle, button).getCenter(), text).draw(w) # type: ignore
    return cast(Rectangle, button)

def in_button(rect: Rectangle, p: Point) -> bool:
    p1: Point = rect.getP1()
    p2: Point = rect.getP2()
    min_x = min(p1.getX(), p2.getX())
    max_x = max(p1.getX(), p2.getX())
    min_y = min(p1.getY(), p2.getY())
    max_y = max(p1.getY(), p2.getY())
    return min_x <= p.getX() <= max_x and \
            min_y <= p.getY() <= max_y

def makeEyes(r: float, w: GraphWin, color: str) -> list[GraphicsObject]:
    eyes: list[GraphicsObject] = []
    angle = radians(50)
    bottom_x = 0.1
    for side in [1, -1]:
        eyes.append(Oval(Point(r * side * bottom_x, 0),
                      Point(r * side * (1 - bottom_x) * cos(angle),
                            r * (1 - bottom_x) * sin(angle))).draw(w))
    for eye in eyes:
        eye.setFill(color)
        eye.setOutline(color)
    return eyes

def makeWhiskers(r: float, w: GraphWin) -> list[GraphicsObject]:
    whiskers: list[GraphicsObject] = []
    innerR: float = 0.8 * r
    outerR: float = 1.8 * r
    whiskerDeg: float = 7
    for side in [1, -1]:
        for angleDeg in [-whiskerDeg, 0, whiskerDeg]:
            angle: float = radians(angleDeg)
            whisker = Line(Point(side * innerR * cos(angle), innerR*sin(angle)),
                           Point(side * outerR * cos(angle), outerR * sin(angle))).draw(w)
            whiskers.append(whisker)

    return whiskers

def makeMouseEars(r: float, w: GraphWin) -> list[GraphicsObject]:
    angle: float = radians(60)
    ears: list[GraphicsObject] = []
    for side in [1, -1]:
        ears.append(Circle(Point(side * 1.4 * r * cos(angle),
                                 1.4 * r * sin(angle)), .6 * r).draw(w))
    return ears

def makeCatEars(r: float, w: GraphWin) -> list[GraphicsObject]:
    angle: float = radians(60)
    earAngle = radians(15)
    ears: list[GraphicsObject] = []
    for side in [1, -1]:
        ears.append(Polygon(Point(side * 1.6 * r * cos(angle), 
                                  1.6 * r * sin(angle)),
                       Point(side * r * cos(angle-earAngle), 
                                r * sin(angle-earAngle)),
                       Point(side * r * cos(angle+earAngle), 
                             r * sin(angle+earAngle))).draw(w))
    return ears

def makeMouse(r: float, w: GraphWin) -> list[GraphicsObject]:
    mouse: list[GraphicsObject] = [Circle(Point(0, 0), r).draw(w)]
    mouse.extend(makeMouseEars(r, w))
    for part in mouse: # Head and ears
        part.setFill('darkgray')
        part.setOutline('darkgray')
    mouse.extend(makeEyes(r, w, 'black'))
    mouse.extend(makeWhiskers(r, w))
    return mouse

def makeCat(r: float, w: GraphWin) -> list[GraphicsObject]:
    cat: list[GraphicsObject] = [Circle(Point(0, 0), r).draw(w)]
    cat.extend(makeCatEars(r, w))
    for part in cat:
        part.setFill('orange')
        part.setOutline('orange')
    cat.extend(makeEyes(r, w, 'green'))
    cat.extend(makeWhiskers(r, w))

    # Move the cat off the screen
    moveTo(cat, Point(2, 0))
    return cat

def moveTo(animal: list[GraphicsObject], p: Point) -> None:
    center: Point = cast(Circle, animal[0]).getCenter()
    dx: float = p.getX() - center.getX()
    dy: float = p.getY() - center.getY()
    for part in animal:
        part.move(dx, dy)

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setCoords(-1, -1, 1, 1)
    label: Text = Text(Point(0, .9), "Click for coordinates")
    label.draw(win)

    # Convention: an animal is a list of GraphicsObjects.
    # The first object on the list has to have getCenter()
    #   defined.

    mouse: list[GraphicsObject] = makeMouse(0.05, win)
    cat_size = 0.2
    cat: list[GraphicsObject] = makeCat(cat_size, win)
    button: Rectangle = make_button(Point(-1, 1), Point(-.8, 0.8), "Quit", win)

    p: Point = Point(0, 0) # Prime the pump
    distance: float = 2 * cat_size

    while distance > cat_size and not in_button(button, p):
        p = win.getMouse() # Update the loop variable.  VERY IMPORTANT!
        label.setText('Click: ' + str(round(p.getX(), 3)) + ', '
            + str(round(p.getY(), 3)) + '\nClick again')
        # Move the mouse to the mouse click
        mousePt: Point = cast(Circle, mouse[0]).getCenter()
        moveTo(mouse, p)
        # Move the cat to where the mouse just was
        moveTo(cat, mousePt)
        distance = separation(cast(Circle, mouse[0]).getCenter(), 
                              cast(Circle, cat[0]).getCenter())
        if distance < cat_size:
            win.setBackground('darkred')
        
    label.setText(label.getText() + ' to exit')
    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
