# add these 4 lines to the move_ball.py file 

elif key == curses.KEY_LEFT and x > 0:
    x -= 1
elif key == curses.KEY_RIGHT and x < width - 1:
    x += 1




the if block of your code will look like this: 


   if key == curses.KEY_UP and y > 0:
            y -= 1
        elif key == curses.KEY_DOWN and y < height - 1:
            y += 1
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < width - 1:
            x += 1
        elif key == ord('q'):
            break

curses.wrapper(main)