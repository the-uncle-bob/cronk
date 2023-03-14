def failing_function():
    m = dict()

    print(m["not_existent_key"])

if __name__ == "__main__":
    failing_function()
