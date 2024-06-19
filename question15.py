import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
filename = 'demo1.csv'
read_csv_file(filename)
