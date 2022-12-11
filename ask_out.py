import time
from twilio.rest import Client
import os
name = input("Hey! Please provide your name: ")
print(f"Oh of course I would never forget about you... it's obvious you are {name}")
time.sleep(3)
print("So I have been thinking... I want to challenge you...")
time.sleep(3)
print("The game goes like this:")
day = input("First, give me any number between 2 and 4: ")
list_of_activites = ["1. Climbing","2. Go for a walk in the snow","3. Watch a movie, 4. All of them"]
activity = int(input(f"Second, which of these do you prefer: {list_of_activites}: "))
print("...")
time.sleep(2)
print("Calculating")
time.sleep(2)
print("Calculating")
time.sleep(2)
print("Calculating (my developer sucks.. don't tell him)")
print("...")
time.sleep(2)
answer2 = input("Converged! Press 1 to see output:")
if int(answer2) == 1:
    ans = []
    d = []
    if activity == 1:
        ans.append("Climbing")
    elif activity == 2:
        ans.append("Go for a walk in the snow")
    elif activity == 3:
        ans.append("Watch a movie")
    elif activity == 4:
        ans.append("All of them")
    if int(day) == 2:
        d.append("Tuesday")
    elif int(day) == 3:
        d.append("Wednesday")
    elif int(day) == 4:
        d.append("Thursday")


    print(f"Based on you answers, I have the following suggestion: {ans} on {d} with my goofy developer (he is quite creative though.. )")

ans3 = input("Do you accept? Yes or Yes? ").lower()

if ans3 == "yes":
    number = input("Please provide your phone number in this format: +46709...: ")
    account_sid = "ACaf31350b29028092a0ec9a08c6ed0b84"
    auth_token = "2ebf21c193743ac38b2ead446907fd88"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hi,this is a text confirmation of your scheduled activity with my developer. Please write any feedback to +46709487925",
        from_="+15627844441",
        to=number
)


#print(message.sid)





