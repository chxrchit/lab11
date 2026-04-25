class Game:
  def __init__ (self, grid):
    self.grid = grid

  def add_randomness(self, r, c, val):
    self.grid[r][c] = val
    
  def move_left(game):
    for i in range(4):        
      game.grid[i] = [x for x in game.grid[i] if x != 0]
    for i in range(4):        
      for j in range(len(game.grid[i]) - 1):
        if game.grid[i][j] == game.grid[i][j+1] :
          game.grid[i][j] += game.grid[i][j+1]
          game.grid[i][j+1].pop()
      game.grid[i] += [0]*(4 - len(game.grid[i]))
      

  def check():
    for i in range(4):
      for j in range(4):
        if game.grid[i][j] == 128:
          return (1)
    return (-1)
          
  
