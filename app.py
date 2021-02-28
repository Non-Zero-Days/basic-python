
message = input("Please write a message\n")
file = open('test.txt', 'w')
file.write(message)
file.close()