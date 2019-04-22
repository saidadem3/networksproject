# Said Adem
# 1000873053
# 04/21/2019

from tabulate import tabulate
import numpy as np
import time

#Makes a formatted table to display node tables
def tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix):
    m = np.array([['1',nodeone[0], nodeone[1], nodeone[2], nodeone[3], nodeone[4], nodeone[5]], 
                ['2', nodetwo[0], nodetwo[1], nodetwo[2], nodetwo[3], nodetwo[4], nodetwo[5]],
                ['3', nodethree[0], nodethree[1], nodethree[2], nodethree[3], nodethree[4], nodethree[5]],
                ['4', nodefour[0], nodefour[1], nodefour[2], nodefour[3], nodefour[4], nodefour[5]],
                ['5', nodefive[0], nodefive[1], nodefive[2], nodefive[3], nodefive[4],nodefive[5]],
                ['6', nodesix[0], nodesix[1], nodesix[2], nodesix[3], nodesix[4], nodesix[5]]])
    headers = ["", "1", "2", "3","4","5","6"]

    # tabulate data
    table = tabulate(m, headers, tablefmt="fancy_grid")

    # output
    print(table)

#updates nodes shortest path
def update(eval,nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix):
    #set up temportary lists to store the values of the node that that's
    #being passed in + all the values of the nodes that match the values position
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    temp6 = []

    #performs the math to store in the temp lists
    for x in range(len(eval)):
        if x == 1-1:
            for val in nodeone:
                temp1.append(  val + eval[x])
        elif x == 2-1:
            for val in nodetwo:
                temp2.append(  val + eval[x])
        elif x == 3-1:
            for val in nodethree:
                temp3.append(  val + eval[x])
        elif x == 4-1:
            for val in nodefour:
                temp4.append(  val + eval[x])
        elif x == 5-1:
            for val in nodefive:
                temp5.append(  val + eval[x])
        elif x == 6-1:
            for val in nodesix:
                temp6.append(  val + eval[x])


    #compares the values in the temporary lists vs the node that's being passed
    #into the function (eval) and sets (eval) to the lowest index value amongst them
    if nodeone == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp2[x], temp3[x], temp4[x], temp5[x], temp6[x] )
    elif nodetwo == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp1[x], temp3[x], temp4[x], temp5[x], temp6[x] )
    elif nodethree == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp1[x], temp2[x], temp4[x], temp5[x], temp6[x] )
    elif nodefour == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp1[x], temp2[x], temp3[x], temp5[x], temp6[x] )
    elif nodefive == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp1[x], temp2[x], temp3[x], temp4[x], temp6[x] )
    elif nodesix == eval:
        for x in range(len(eval)):
            eval[x] = min( eval[x], temp1[x], temp2[x], temp3[x], temp4[x], temp5[x] )

    return eval

def stepin(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix):
    print("input \"next\" to continue and anything else to cancel")
    print()
    print("iteration 1:")
    print("----------------------------------")
    print()
    #formatted table
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    #updates the costs of the nodes then prints them in a formatted table
    print()
    print("iteration 2:")
    print("----------------------------------")
    print()
    nodeone = update(nodeone, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    print()
    print("iteration 3:")
    print("----------------------------------")
    print()
    nodetwo = update(nodetwo, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    print()
    print("iteration 4:")
    print("----------------------------------")
    print()
    nodethree = update(nodethree, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    print()
    print("iteration 5:")
    print("----------------------------------")
    print()
    nodefour = update(nodefour, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    print()
    print("iteration 6:")
    print("----------------------------------")
    print()
    nodefive = update(nodefive, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    print()
    print("iteration 7:")
    print("----------------------------------")
    print()
    nodesix = update(nodesix, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
    nextstep = input("continue: ")
    if nextstep != "next":
        return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
    
    #store current iteration in comptable to run the while loop
    comptable  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
    comptable2 = []
    #counter for incrementing iteration
    counter = 8

    while comptable != comptable2:
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodeone = update(nodeone, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodetwo = update(nodetwo, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodethree = update(nodethree, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodefour = update(nodefour, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodefive = update(nodefive, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        comptable  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
        print()
        print(f"iteration {counter}:")
        print("----------------------------------")
        print()
        nodesix = update(nodesix, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        counter+=1
        nextstep = input("continue: ")
        if nextstep != "next":
            return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        comptable2  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
        if comptable == comptable2:
            break
    return(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)

def main():
    #initialize a 2d list to later store each row as a seperate node
    table= [ 
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )],
    [float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' ), float( '+inf' )]
    ]

    print("Hello user! Please enter the name of the file you will be using to obtain our nodes.")
    print("Please be aware that only .txt will work")
    filename = input("Enter Filename: ")
    print()
    #opens the .txt file and prints the initial nodes and their link costs
    with open(filename + ".txt", "r") as f:
        for line in f:
            node1, node2, link = line.split()
            print(f'Node {node1} to {node2} has a link of {link}')


    #stores the link cost to their respective nodes
    with open("nodes.txt", "r") as f:
        for line in f:
            node1, node2, link = line.split()
            table[int(node1)-1][int(node2)-1] = int(link)
            table[int(node2)-1][int(node1)-1] = int(link)

    #sets the link cost of every node that reaches itself to zero
    for i in range(len(table)):
        table[i][i] = 0

    #takes the rows from the table and stores them in individual nodes
    nodeone = table[0]
    nodetwo = table[1]
    nodethree = table[2]
    nodefour = table[3]
    nodefive = table[4]
    nodesix = table[5]

    print()    
    print("Enter \"step\" to go step by step or \"stable\" to go until the system hits a stable state?")
    answer = input("How would you like to proceed: ")
    
    #####################################################################################################
    # Nodes update in a step by step matter (passed into stepin function)
    #####################################################################################################

    if answer == 'step':
        stepin(nodeone, nodetwo, nodethree, nodefour, nodefive, nodesix)
        print("Links are in stable state")

    #####################################################################################################
    # Nodes update until they are stable
    #####################################################################################################

    elif answer == 'stable':
        #records the start of the execution
        start = time.time()
        print()
        print("iteration 1:")
        print("----------------------------------")
        print()
        #formatted table
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)

        #updates the costs of the nodes then prints them in a formatted table
        print()
        print("iteration 2:")
        print("----------------------------------")
        print()
        nodeone = update(nodeone, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        print()
        print("iteration 3:")
        print("----------------------------------")
        print()
        nodetwo = update(nodetwo, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        print()
        print("iteration 4:")
        print("----------------------------------")
        print()
        nodethree = update(nodethree, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        print()
        print("iteration 5:")
        print("----------------------------------")
        print()
        nodefour = update(nodefour, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        print()
        print("iteration 6:")
        print("----------------------------------")
        print()
        nodefive = update(nodefive, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        print()
        print("iteration 7:")
        print("----------------------------------")
        print()
        nodesix = update(nodesix, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
        
        #store current iteration in comptable to run the while loop
        comptable  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
        comptable2 = []
        #counter for incrementing iteration
        counter = 8

        while comptable != comptable2:
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodeone = update(nodeone, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodetwo = update(nodetwo, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodethree = update(nodethree, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodefour = update(nodefour, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodefive = update(nodefive, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            comptable  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
            print()
            print(f"iteration {counter}:")
            print("----------------------------------")
            print()
            nodesix = update(nodesix, nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            tab(nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix)
            counter+=1
            comptable2  = [nodeone,nodetwo,nodethree,nodefour,nodefive,nodesix]
            if comptable == comptable2:
                break
        
        #records the end of the execution
        end = time.time()
        print(f"Total execution time was: {end-start}s")
        print("Links are in stable state")


if __name__ == "__main__":
    main()