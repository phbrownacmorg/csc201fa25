from graphics import *

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin("Graphics", 640, 480)
    # Graphics stuff goes here

    win.getMouse()  # Wait for a mouse click
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
