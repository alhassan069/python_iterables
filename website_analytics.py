monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user1","user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}


print("Unique visitors across all days")

unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors

print(unique_visitors)

print("Returning Visitors on Tuesday")

print(monday_visitors & tuesday_visitors)

print("New visitors each day")

print("Monday new visitors", monday_visitors)
print("Tuesday new visitors", tuesday_visitors - monday_visitors)
print("Wednesday new visitors", wednesday_visitors - (monday_visitors | tuesday_visitors))

print("Loyal visitors", monday_visitors & tuesday_visitors & wednesday_visitors)


# Daily visitor overlap analysis

print("Monday Tuesday", monday_visitors & tuesday_visitors)
print("Monday Wednesday", monday_visitors & wednesday_visitors)
print("Tuesday Wednesday", tuesday_visitors & wednesday_visitors)
