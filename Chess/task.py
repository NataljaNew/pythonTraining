class Knight:
    BORD_SIZE = 8

    def __init__(self, horizontal, vertical, color):
        self.horizontal, self.vertical, self.color = horizontal, vertical, color

    def get_char(self):
        return 'N'

    def can_move(self, horiz_c, vertic_c):
        return abs(ord(horiz_c) - ord(self.horizontal)) * abs(vertic_c - self.vertical) == 2

    def move_to(self, horiz_c, vertic_c):
        if self.can_move(horiz_c, vertic_c):
            self.horizontal, self.vertical = horiz_c, vertic_c

    def v_to_board_coord(v):
        return v + 1

    def h_to_board_coord(h):
        return chr(ord('a') + h)

    def draw_board(self):
        for v in range(Knight.BORD_SIZE - 1, 0 - 1, -1):
            row_arr = ['.'] * Knight.BORD_SIZE
            for h in range(Knight.BORD_SIZE):
                horiz_c = Knight.h_to_board_coord(h)
                vertic_c = Knight.v_to_board_coord(v)
                if self.horizontal == horiz_c and self.vertical == vertic_c:
                    row_arr[h] = self.get_char()
                elif self.can_move(horiz_c, vertic_c):
                    row_arr[h] = '*'
            print(''.join(row_arr))


knight = Knight('e', 5, 'black')

knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()
