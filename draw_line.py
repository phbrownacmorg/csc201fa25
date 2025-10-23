from graphics import *
import math
from typing import cast

def fmt_pt(p: Point) -> str:
    prec = 3            # Precision
    return f"({p.getX():.{prec}f}, {p.getY():.{prec}f})"

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 600, 600)
    # Graphics stuff goes here
    win.setCoords(-1, -1, 1, 1)

    msg1 = 'Click once to set an endpoint.'
    msg3 = 'Click once more to exit.'


    instructions: Text = cast(Text, Text(Point(0, .8), msg1).draw(win))
    p1: Point = cast(Point, win.getMouse().draw(win))
    msg2 = f"""Point is {fmt_pt(p1)}.
Click once more to set the other end."""
    instructions.setText(msg2)
    p2: Point = cast(Point, win.getMouse().draw(win))
    Line(p1, p2).draw(win)

    msg3 = f"""Points are {fmt_pt(p1)}, {fmt_pt(p2)}
Line length is {math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2):.3f}.
Click once more to exit."""
    instructions.setText(msg3)

    win.getMouse()  # Wait for a mouse click

    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
