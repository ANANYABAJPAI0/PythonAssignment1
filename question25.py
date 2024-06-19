def copy_file(source_file, destination_file):
    try:
      
        with open(source_file, 'r') as f_source, open(destination_file, 'w') as f_dest:
            
            for line in f_source:
                f_dest.write(line)
        
        print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print("Error: One of the files does not exist.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")
    
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
