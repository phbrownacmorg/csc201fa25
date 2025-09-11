from graphics import *

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setBackground('gray')
    win.setCoords(-1, -1, 1, 1)         # 2x2 square with the origin in the center
    # Plot pixels.  Positions are in raw pixels, unaffected by win.setCoords().
    win.plotPixel(10, 10, 'red')        # Upper left
    win.plotPixel(490, 10, 'green')     # Upper right
    win.plotPixel(10, 490, 'blue')      # Lower left
    win.plotPixel(490, 490, 'black')    # Lower right

    center: Point = Point(0,0)          # Center of screen
    center.setOutline('yellow')
    center.draw(win)

    # Lines
    west: Point = Point(-0.5, 0)
    east: Point = Point(0.5, 0)
    line1: Line = Line(east, west)
    line1.draw(win)

    north: Point = Point(0, .5)
    south: Point = Point(0, -.5)
    line2: Line = Line(north, south)
    line2.setOutline('lightblue')
    line2.setWidth(3)
    line2.setArrow('first')
    line2.draw(win)

    # Circles
    circ: Circle = Circle(center, .1)
    circ.setOutline('purple')
    circ.setFill('gold')
    circ.setWidth(3)
    circ.draw(win)

    # Rectangle
    ese: Point = Point(.5,-0.25)
    rect = Rectangle(ese, south)
    # Draws transparent if no fill is specified
    rect.draw(win)

    # Oval
    oval: Oval = Oval(south, ese)
    oval.setFill('green')
    oval.draw(win)
    print('Center of oval:', oval.getCenter())

    dy = abs(ese.getY() - south.getY())

    oval_clone = oval.clone() # No aliasing here; copy of object
    oval_clone.move(0, dy)
    oval_clone.setFill('lightslateblue')
    oval_clone.draw(win)

    oval_alias = oval    # oval_alias aliases oval
    oval_alias.move(0, -dy)
    #oval_alias.draw(win)  # Would cause a crash, because the object's already drawn

    print('Center of oval:', oval.getCenter()) # But I never changed oval!
    print('Center of oval_clone:', oval_clone.getCenter())
    print('Center of oval_alias:', oval_alias.getCenter())


    # Polygon
    wsw: Point = Point(-.5, -.25)
    poly: Polygon = Polygon(west, wsw, south)
    poly.setFill('pink')
    poly.draw(win)

    # Polygon from a list of Points
    ptslist: list[Point] = [center, wsw, south, ese]
    poly2: Polygon = Polygon(ptslist)
    poly2.setFill(color_rgb(110, 200, 88)) # Color specified with red, green, and blue
    poly2.draw(win)

    # Text object
    anchor: Point = Point(0, .9)
    instructions: Text = Text(anchor, 'Click to close window')
    instructions.draw(win)

    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
