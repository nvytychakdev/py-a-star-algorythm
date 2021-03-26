import tkinter as tk

class Cell:
  def __init__(self, size):
    self.size = size


class Grid:
  grid = None
  cell_size = None
  row_length = None
  col_length = None

  def __init__(self, width, height, cell_size=10):
    self.width = width
    self.height = height

    self.cell_size = cell_size

    self.row_length = width / cell_size
    self.col_length = height / cell_size

    self.grid = self._generate_grid(
        self.row_length, self.col_length, self.cell_size)

  def _generate_grid(self, row_length, col_length, cell_size):
    if row_length > 0 and col_length > 0:
      grid = []
      for i in range(0, int(col_length)):
        grid.append([])
        for j in range(0, int(row_length)):
          grid[i] = Cell(cell_size)
      return grid
    return []


class GridWindow():
  _window = tk.Tk()
  _canvas = None

  def __init__(self, width=800, height=600):
    self.width = width
    self.height = height

  def _add_canvas(self):
    if self._window:
      self._canvas = tk.Canvas(
        self._window, width=self.width, height=self.height)
      self._canvas.pack()

      return self._canvas

    return None

  def _draw_grid(self):
    if self._window:
      grid_builder = Grid(self.width, self.height, 100)
      grid = grid_builder.grid
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          grid_cell = grid[i][j]
          cell_size = grid_cell.size
          print(cell_size)

  def open(self):
    canvas = self._add_canvas()
    self._draw_grid()

    # mainloop will prevent from code execution further
    self._window.mainloop()


def main():
  grid_window = GridWindow()

  # start window execution
  grid_window.open()

  return None


main()
