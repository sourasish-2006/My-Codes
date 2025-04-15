import time
current_time = time.strftime("%H:%M:%S")
print(current_time)
hour = int(time.strftime("%H"))
if (5 <= hour < 12):
    print("Good morning sir")
elif (12 <= hour < 17):
    print("Good afternoon sir")
elif (17 <= hour < 21):
    print("Good evening sir")
else:
    print("Good night sir")
