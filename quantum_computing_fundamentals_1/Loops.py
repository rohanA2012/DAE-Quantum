name = input("What is your name? ")

for current_index in range(10):
    print(name)

last_room_checked = int(input("What is the last room? "))

for index in range(1, last_room_checked+1):
    print("Room ",index," Checked.")

# add 0 to 500 and print final sum

total = sum(range(0,501))
print(total)