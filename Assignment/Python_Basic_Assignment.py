def validate_usernames(usernames):
    valid_count = 0
    invalid_count = 0

    for name in usernames:
        if len(name) >= 5 and len(name) <= 7 and " " not in name:
            print("VALID:", name)
            valid_count += 1
        else:
            print("INVALID:", name)
            invalid_count += 1

    return valid_count, invalid_count


usernames = []

n = int(input("How many usernames? "))

for i in range(n):
    usernames.append(input("Enter username: "))

total = validate_usernames(usernames)

print("Total valid usernames:", total)