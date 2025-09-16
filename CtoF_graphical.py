from graphics import *

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 500, 500)
    win.setCoords(-1, -1, 1, 1)
    label: Text = Text(Point(0, .9), "Enter a temperature.\nClick to convert.")
    label.draw(win)

    c_blank: Entry = Entry(Point(-.2, 0), 5)
    c_blank.setText("0")
    c_blank.draw(win)
    output: Text = Text(Point(.1, 0), '\u00b0 C')
    output.draw(win)

    for i in range(3):          # type: ignore
        win.getMouse()
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
