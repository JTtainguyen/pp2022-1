import curses

def print_menu(stdscr, selected_row_idx):
    menu = ['Add Student', 'Add Course', 'Add Mark', 'Show Student', 'Show Course', 'Show Mark', 'Student Average Gpa',
            'Sort Descending Order', 'Exit']
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
