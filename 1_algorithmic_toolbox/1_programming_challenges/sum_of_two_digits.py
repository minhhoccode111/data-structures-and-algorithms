# # first try
# def rec():
#     try:
#         x = float(input("x: "))
#         y = float(input("y: "))
#         print(x + y)
#     except ValueError as err:
#         print(f"error occurs: {err}")
#         rec()
# rec()

# first passes solution
str = input()
x = int(str.split()[0])
y = int(str.split()[1])
print(x + y)
