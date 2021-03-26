import tkinter as tk

class Cell:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
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

    self.row_length = int(width / cell_size)
    self.col_length = int(height / cell_size)

    self.grid = self._generate_grid(
        self.row_length, self.col_length, self.cell_size)

  def _generate_grid(self, row_length, col_length, cell_size):
    if row_length > 0 and col_length > 0:
      grid = []
      for i in range(col_length + 1):
        grid.append([])
        y_pos = i * self.cell_size
        for j in range(row_length + 1):
          x_pos = j * self.cell_size
          grid[i].append(Cell(x_pos, y_pos, cell_size))
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

  def _draw_grid(self, canvas):
    if self._window:
      grid_builder = Grid(self.width, self.height, 100)
      grid = grid_builder.grid
      for row in grid:
        for cell in row:
          canvas.create_rectangle(cell.x, cell.y, cell.size, cell.size)
          print(cell.x, cell.y, cell.size)

  def open(self):
    canvas = self._add_canvas()
    self._draw_grid(canvas)

    # mainloop will prevent from code execution further
    self._window.mainloop()


def main():
  grid_window = GridWindow()

  # start window execution
  grid_window.open()

  return None


main()
