from graphics import *
from typing import cast

def make_button(p1: Point, p2: Point, text: str, w: GraphWin) -> Rectangle:
    button = Rectangle(p1, p2).draw(w)
    label = Text(cast(Rectangle, button).getCenter(), text).draw(w)
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

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setCoords(-1, -1, 1, 1)
    label: Text = Text(Point(0, .9), "Enter a temperature.")
    label.draw(win)

    c_blank: Entry = Entry(Point(-.2, 0), 5)
    c_blank.setText("0")
    c_blank.draw(win)
    output: Text = Text(Point(.1, 0), '\u00b0 C')
    output.draw(win)

    button = make_button(Point(-.5, -.1), Point(.5, -.9), 'Convert', win)

    for i in range(3):          # type: ignore
        click: Point = win.getMouse()
        output.setText('\u00b0 C')
        if in_button(button, click):
            degC: float = float(c_blank.getText())
            degF: float = (9/5) * degC + 32
            output.setText('\u00b0 C = '+ str(round(degF, 1)) + '\u00b0 F')

    label.setText('Click once more to exit')
    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
