# def cost(table):
#     indexrow = 1
#     indexcol = 1
#     for row in table:
#         for col in row:
#             if col > 0 and col < float('+inf'):
#                 print(f'{indexrow},{indexcol} = {col}')
#             if indexcol < 6:
#                 indexcol += 1
#             else:
#                 indexcol = 1
#         indexrow += 1
#     return

def cost(table):
    indexrow = 1
    indexcol = 1
    for row in table:
        for col in row:
            if col > 0 and col < float('+inf'):
                print(f'{indexrow},{indexcol} = {col}')
            if indexcol < 6:
                indexcol += 1
            else:
                indexcol = 1
        indexrow += 1
    return

def main():
    table= [ 
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )]
    ]


    with open("nodes.txt", "r") as f:
        for line in f:
            node1, node2, link = line.split()
            print(f'Node {node1} to {node2} has a link of {link}')

    print()
    print("first iteration")
    print("----------------------------------")
    print()

    with open("nodes.txt", "r") as f:
        for line in f:
            node1, node2, link = line.split()
            table[int(node1)-1][int(node2)-1] = int(link)
            table[int(node2)-1][int(node1)-1] = int(link)
    
    for i in range(len(table)):
        table[i][i] = 0
    
    for row in table:
        print(row)


    print()
    print("second iteration")
    print("----------------------------------")
    print()

    cost(table)

    #Dx(y) = min{c(x,y) + Dy(y), c(x,z) + Dz(y)}



if __name__ == "__main__":
    main()