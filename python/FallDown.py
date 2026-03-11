def fall_down(values2dim):
    for x in range(len(values2dim[0])):
        for y in range(len(values2dim)-1,-1,-1):
            current_y = y
            while len(values2dim) > current_y > 0 == values2dim[current_y][x] and  values2dim[current_y - 1][x]>0:
                values2dim[current_y][x]=values2dim[current_y-1][x]
                values2dim[current_y-1][x]=0
                current_y+=1

def test_fall():
    values2dim = [[0,1,3,3,0,0],
                  [0,1,0,0,0,0,],
                  [0,0,3,3,0,0],
                  [0,0,0,3,3,4],
                  [0,0,3,0,0,0]]
    fall_down(values2dim)
    expected_board = [[0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,3,3,0,0],
                      [0,1,3,3,0,0],
                      [0,1,3,3,3,4]]
    assert values2dim== expected_board