def log_to_file(operation_result, filename="history.txt"):
    with open(filename, "a") as f:
        f.write(operation_result + "\n")
