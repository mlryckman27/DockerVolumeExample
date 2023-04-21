# imports go here...


# function definitions...

def read_test_file():
    test_file = open("test.txt", "r")
    result = test_file.read()
    return result


# Run the application
if __name__ == "__main__":
    print(read_test_file())
