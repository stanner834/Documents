def printTable(tableData):
    if not tableData:
        return  # Return if the table is empty

    # Create a list to store the maximum width of each column
    colWidths = [0] * len(tableData)

    # Find the maximum width of each column
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    # Transpose the table for easier printing
    transposed = list(map(list, zip(*tableData)))

    # Print the table with right-justified columns
    for i in range(len(transposed)):
        for j in range(len(transposed[i])):
            print(transposed[i][j].rjust(colWidths[j]), end=" ")
        print()  # Start a new line for the next row

# Example table data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Call the function
printTable(tableData)