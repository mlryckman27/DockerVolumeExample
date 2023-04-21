# imports go here...


# function definitions...

def write_test_file():
    test_file = open("test.txt", "w")
    test_file.write("This data should persist in a Docker volume.")


# Run the application
if __name__ == "__main__":
    write_test_file()
    file = open("test.txt", "r")
    result = file.read()
    print(result)
