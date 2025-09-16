from graphics import *

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setCoords(-1, -1, 1, 1)
    label: Text = Text(Point(0, .9), "Click for coordinates")
    label.draw(win)

    mouse: Circle = Circle(Point(0, 0), .05)
    mouse.setFill('darkgray')
    mouse.draw(win)

    cat: Circle = Circle(Point(2, 0), .2) # Initially off the screen
    cat.setFill('orange')
    cat.draw(win)

    for i in range(6):              # type: ignore
        p: Point = win.getMouse()
        label.setText('Click: ' + str(round(p.getX(), 3)) + ', '
            + str(round(p.getY(), 3)) + '\nClick again')
        
        # Move the mouse to the mouse click
        mousePt: Point = mouse.getCenter()
        dx: float = p.getX() - mousePt.getX()
        dy: float = p.getY() - mousePt.getY()
        mouse.move(dx, dy)

        # Move the cat to where the mouse just was
        catPt: Point = cat.getCenter()
        dx = mousePt.getX() - catPt.getX()
        dy = mousePt.getY() - catPt.getY()
        cat.move(dx, dy)

    label.setText(label.getText() + ' to exit')
    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
