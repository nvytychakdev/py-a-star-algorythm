import tkinter as tk

class Cell:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2


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
        self.row_length, self.col_length, self.cell_size, 2)

  def _generate_grid(self, row_length, col_length, size, padding=0):
    if row_length > 0 and col_length > 0:
      grid = []
      for i in range(col_length):
        grid.append([])
        y1 = i * size + padding
        y2 = y1 + size - padding
        for j in range(row_length):
          x1 = j * size + padding
          x2 = x1 + size - padding
          grid[i].append(Cell(x1, y1, x2, y2))
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
          canvas.create_rectangle(cell.x1, cell.y1, cell.x2, cell.y2, activefill='#ddd', tag=f'')
          print('cell:' , f'x:{cell.x1} ; y:{cell.y1};', cell.x2, cell.y2)

  def _bind_events(self, canvas):
    canvas.bind('<Motion>', self.on_mouseover)

  def on_mouseover(self, event):
    # TODO: search for event target by tag
    return

  def open(self):
    canvas = self._add_canvas()
    self._draw_grid(canvas)
    self._bind_events(canvas)

    # mainloop will prevent from code execution further
    self._window.mainloop()


def main():
  grid_window = GridWindow()

  # start window execution
  grid_window.open()

  return None


main()
