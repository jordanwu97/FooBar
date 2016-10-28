def removeBestWall(maze): 
  maxSize = 0
  bestWall = [0, 0]
  for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
      size = getRoomSize(maze, i, j)
      if size > maxSize:
        maxSize = size
        bestWall = [i, j]
  print (bestWall)
  return bestWall


def getRoomSize(maze, i, j):
  if(maze[i][j] == 1): 
    return 0
  newMaze = maze
  newMaze[i][j] = 1
  size = 1;
  return size + getRoomSize(newMaze, i, j + 1) + getRoomSize(newMaze, i, j - 1) + getRoomSize(newMaze, i + 1, j) + getRoomSize(newMaze, i - 1, j);

maze = [[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]]

removeBestWall(maze)