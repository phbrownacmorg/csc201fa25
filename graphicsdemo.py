from graphics import *

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 640, 480)
    win.setBackground('gray')
    # Plot pixels
    win.plotPixel(10, 10, 'red')        # Upper left
    win.plotPixel(630, 10, 'green')     # Upper right
    win.plotPixel(10, 470, 'blue')      # Lower left
    win.plotPixel(630, 470, 'black')    # Lower right

    center: Point = Point(320,240)      # Center of screen
    center.setOutline('yellow')
    center.draw(win)

    # Lines
    west: Point = Point(160, 240)
    east: Point = Point(480, 240)
    line1: Line = Line(east, west)
    line1.draw(win)

    north: Point = Point(320, 120)
    south: Point = Point(320, 360)
    line2: Line = Line(north, south)
    line2.setOutline('lightblue')
    line2.setWidth(3)
    line2.setArrow('first')
    line2.draw(win)

    # Circles
    circ: Circle = Circle(center, 30)
    circ.setOutline('purple')
    circ.setFill('gold')
    circ.setWidth(3)
    circ.draw(win)

    # Rectangle
    ese: Point = Point(480,300)
    rect = Rectangle(ese, south)
    # Draws transparent if no fill is specified
    rect.draw(win)

    # Oval
    oval: Oval = Oval(south, ese)
    oval.setFill('green')
    oval.draw(win)

    # Polygon
    wsw: Point = Point(160, 300)
    poly: Polygon = Polygon(west, wsw, south)
    poly.setFill('pink')
    poly.draw(win)

    # Polygon from a list of Points
    ptslist: list[Point] = [center, wsw, south, ese]
    poly2: Polygon = Polygon(ptslist)
    poly2.setFill(color_rgb(110, 200, 88)) # Color specified with red, green, and blue
    poly2.draw(win)

    # Text object
    anchor: Point = Point(320, 40)
    instructions: Text = Text(anchor, 'Click to close window')
    instructions.draw(win)

    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
