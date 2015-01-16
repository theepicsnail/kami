from levels import levels
from UF import UF
moves,grid = levels[8]

def get_cell(row, col):
    return row * 10 + col

uf = UF()
for row in xrange(16):
    for col in xrange(10):
        cell_id = get_cell(row, col)
        cell = grid[row][col]

        if row != 15: # Horizontal unioning
            if cell == grid[row][col+1]:
                uf.union(cell_id, get_cell(row, col+1))

        if col != 9: # Vertical unioning
            if cell == get[row+1][col]:
                uf.union(cell_id, get_cell(row+1, col))



