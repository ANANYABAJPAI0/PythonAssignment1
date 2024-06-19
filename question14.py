def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("\nLines entered:")
    for line in lines:
        print(line)

# Call the function to run the program
read_multiple_lines()
