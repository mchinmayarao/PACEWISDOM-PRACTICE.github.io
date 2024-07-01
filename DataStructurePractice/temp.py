
grid=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]

islands = 0
visited = set()
directions = [[-1,0],[1,0],[0,1],[0,-1]]
rows,cols = len(grid),len(grid[0])
island_size = []
def search(r,c):
    if (
        r not in range(rows)
        or c not in range(cols)
        or grid[r][c] == 0
        or (r, c) in visited
    ):
        return 0 
    size = 1
    visited.add((r,c))
    for dr , dc in directions:
        size += search(r+dr , c+dc)
    return size
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1 and (r,c) not in visited:
            islands +=1
            island_size.append(search(r,c))
            
print(island_size)