# Run this program and observe what happens

# def assign_values(x, len):
#     for i in range(len):
#         x[i] = (i + 1) * (i + 1)

# if __name__ == "__main__":
#     data = [0] * 10
#     assign_values(data, 10)
#     print("Done!")

def assign_values(x):
    for i in range(100):
        x[i] = (i + 1) * (i + 1);

if __name__ == "__main__":
    data = [0] * 10
    assign_values(data)
    print("Done!")