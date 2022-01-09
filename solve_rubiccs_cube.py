import kociemba

def proximity(pos,target):
    delta = 0.2
    result = False
    if pos.x + delta > target[0] and pos.x - delta < target[0]:
        if pos.y + delta > target[1] and pos.y - delta < target[1]:
            if pos.z + delta > target[2] and pos.z - delta < target[2]:
                result = True
    return result
def color_detect(color_value):
    value = (color_value.x,color_value.y,color_value.z)
    color_result = None
    if value == (1,0,0):
        color_result = 'F'
    elif value == (1,1,0):
        color_result = 'R'
    elif value == (1, 0.5, 0):
        color_result = 'B'
    elif value == (1, 1, 1):
        color_result = 'L'
    elif value == (0, 0, 1):
        color_result = 'U'
    elif value == (0, 1, 0):
        color_result = 'D'
    return color_result
def decode_postion(cube):
    '''F = red, R = yellow, B = orange, L = white, U = blue, D = green'''
    value = ['0']*54
    for tile in cube:
        if proximity(tile.pos,(-1,1.5,-1)): #U1
            value[0] = color_detect(tile.color)
        elif proximity(tile.pos,(0,1.5,-1)): #U2
            value[1] = color_detect(tile.color)
        elif proximity(tile.pos,(1,1.5,-1)): #U3
            value[2] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,1.5,0)): #U4
            value[3] = color_detect(tile.color)
        elif proximity(tile.pos,(0,1.5,0)): #U5
            value[4] = color_detect(tile.color)
        elif proximity(tile.pos,(1,1.5,0)): #U6
            value[5] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,1.5,1)): #U7
            value[6] = color_detect(tile.color)
        elif proximity(tile.pos,(0,1.5,1)): #U8
            value[7] = color_detect(tile.color)
        elif proximity(tile.pos,(1,1.5,1)): #U9
            value[8] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,1,1)): #R1
            value[9] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,1,0)): #R2
            value[10] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,1,-1)): #R3
            value[11] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,0,1)): #R4
            value[12] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,0,0)): #R5
            value[13] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,0,-1)): #R6
            value[14] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,-1,1)): #R7
            value[15] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,-1,0)): #R8
            value[16] = color_detect(tile.color)
        elif proximity(tile.pos,(1.5,-1,-1)): #R9
            value[17] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,1,1.5)): #F1
            value[18] = color_detect(tile.color)
        elif proximity(tile.pos,(0,1,1.5)): #F2
            value[19] = color_detect(tile.color)
        elif proximity(tile.pos,(1,1,1.5)): #F3
            value[20] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,0,1.5)): #F4
            value[21] = color_detect(tile.color)
        elif proximity(tile.pos,(0,0,1.5)): #F5
            value[22] = color_detect(tile.color)
        elif proximity(tile.pos,(1,0,1.5)): #F6
            value[23] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,-1,1.5)): #F7
            value[24] = color_detect(tile.color)
        elif proximity(tile.pos,(0,-1,1.5)): #F8
            value[25] = color_detect(tile.color)
        elif proximity(tile.pos,(1,-1,1.5)): #F9
            value[26] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,-1.5,1)): #D1
            value[27] = color_detect(tile.color)
        elif proximity(tile.pos,(0,-1.5,1)): #D2
            value[28] = color_detect(tile.color)
        elif proximity(tile.pos,(1,-1.5,1)): #D3
            value[29] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,-1.5,0)): #D4
            value[30] = color_detect(tile.color)
        elif proximity(tile.pos,(0,-1.5,0)): #D5
            value[31] = color_detect(tile.color)
        elif proximity(tile.pos,(1,-1.5,0)): #D6
            value[32] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,-1.5,-1)): #D7
            value[33] = color_detect(tile.color)
        elif proximity(tile.pos,(0,-1.5,-1)): #D8
            value[34] = color_detect(tile.color)
        elif proximity(tile.pos,(1,-1.5,-1)): #D9
            value[35] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,1,-1)): #L1
            value[36] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,1,0)): #L2
            value[37] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,1,1)): #L3
            value[38] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,0,-1)): #L4
            value[39] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,0,0)): #L5
            value[40] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,0,1)): #L6
            value[41] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,-1,-1)): #L7
            value[42] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,-1,0)): #L8
            value[43] = color_detect(tile.color)
        elif proximity(tile.pos,(-1.5,-1,1)): #L9
            value[44] = color_detect(tile.color)
        elif proximity(tile.pos,(1,1,-1.5)): #B1
            value[45] = color_detect(tile.color)
        elif proximity(tile.pos,(0,1,-1.5)): #B2
            value[46] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,1,-1.5)): #B3
            value[47] = color_detect(tile.color)
        elif proximity(tile.pos,(1,0,-1.5)): #B4
            value[48] = color_detect(tile.color)
        elif proximity(tile.pos,(0,0,-1.5)): #B5
            value[49] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,0,-1.5)): #B6
            value[50] = color_detect(tile.color)
        elif proximity(tile.pos,(1,-1,-1.5)): #B7
            value[51] = color_detect(tile.color)
        elif proximity(tile.pos,(0,-1,-1.5)): #B8
            value[52] = color_detect(tile.color)
        elif proximity(tile.pos,(-1,-1,-1.5)): #B9
            value[53] = color_detect(tile.color)
    return value
def solve(cube):
    values = ""
    values = values.join(decode_postion(cube))
    solution = kociemba.solve(values)
    print('solution is \n' + solution)
    return solution