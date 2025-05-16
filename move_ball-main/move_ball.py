import curses

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Red on black

    stdscr.nodelay(True)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    x = width // 2
    y = height // 2

    while True:
        stdscr.clear()
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y, x, "O")  # Draw the ball
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and y > 0:
            y -= 1
        elif key == curses.KEY_DOWN and y < height - 1:
            y += 1    
        elif key == ord('q'):
            break

curses.wrapper(main)