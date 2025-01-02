cities = [
  "los angeles"
  "new york city"
]

how_to_make_money = [
  "actor"
  "uber"
  "instacart"
  "influencer"
  "lottery"
  "robbery"
]

disguises = [
  "among us"
  "agent"
  "dinosaur"
]

houses = [
  "house a"
  "house b"
]
print("Hello criminal! You are currently on the run for murder, and you are wanted by the FBI. You will start in Los Angeles, then get on a plane to New York City. In New York City you will sneak out of the country into a country that won't send you back. I wish you the best of luck!")


prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
elif prompt == "no":
  print("game over") 
  exit(0)
else:
  pass
  

print("You are in Los Angeles at the moment. You have $500, it is a good idea if you buy a disguise. What disguise would you like to buy? Your options are an among us inflatable suit, an agent suit, or a dinosaur inflatable suit. Each costume will cost you $50 say 1 for among us, say 2 for agent, say 3 for dinosaur.")

prompt = input("Which costume would you like to buy?")
if prompt == "1":
  print("you have purchased the among us inflatable suit and now have $450")
elif prompt == "2":
 print("you have purchased the agent suit and now have $450")
elif prompt == "3":
  print("you have purchased the dinosaur inflatable suit and now have $450")
else:
  pass

prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
elif prompt == "no":
 print("Game over")
 exit(0)
else:
  pass

print("You need to find a way to make money, there are many things you can do in the city of Los Angeles to make money. You can be an actor in Holywood, be an uber driver, be an instacart driver, or be an influencer and harrass people with your pranks. Say 1 for actor, say 2 for uber, say 3 for instacart, say 4 for influencer") 

prompt = input("what job do you want?")
if prompt == "1":
 print("You got the job! Time for you to film the next Spider Man movie!")
elif prompt == "2":
  print("You got the job! Thankfully you have a car so you can uber drive people, start driving people that the uber app tells you to!")
elif prompt == "3":
    print("You got the job! Thankfully you have a car so you can deliver people, go deliver some food!")
elif prompt == "4":
    print("You download TikTok and start making videos. You have an idea! You want to make retail workers mad, so you film a video of yourself throwing drinks at the walls! Your video blows up on TikTok because 10 year olds think its funny and think you are cool!")

prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
 print("You had a successful day of work, you made $150 and now have $600! You book a plane ticket of $494 for tomorrow, December 31st. You also need to get yourself a hotel room to stay in tonight.")
 prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
elif prompt == "no":
  print("game over")
  exit(0)
else:
  pass

print("You bought a hotel room for $44. You stay there for the night.")

prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
elif prompt == "no":
  print("game over")
  exit(0)
else:
  pass

print("Good morning! It is 05:00 and you have $18. You need to go catch your flight now.")

prompt = input("On your way to your flight, you see a criminal, should you ask the criminal to go commit burglary with you before your flight? 1 for yes, 2 for no")
 
if prompt == "1":
  print("The criminal was actually an undercover cop, and you get sent to federal prison, game over!")
  exit(0)

elif prompt == "2":
  print("Nice! You dodged an undercover cop! You make it to the airport safely. Once you are at the airport you wait 3 hours for your flight and then board your flight.")

prompt = input("continue?")
if prompt == yes:
  print("\x1b[2J\033[H")
elif prompt == no:
  print("game over")
  exit(0)
else:
  pass

print("You made it to the JFK airport in New York City safely at 20:30.")

prompt = input("You need to find a way to make money, how do you want to make money? You can use your money to buy a lottery ticket, you can be an influencer and vlog yourself at the New Years Eve ball drop, or be an uber driver. What do you want to do? 1 for lottery, 2 for influencer, 3 for uber")

if prompt == "1":
 print("You got lucky and won a million dollars in the lottery and now you have $1,000,018 and can move to Abu Dhabi where you can live a fancy life with no extradition treaty.")
 print("game over!")
 exit(0)

elif prompt == "2":
  print("You go to the ball drop for New Years Eve and you have so much fun. Your video goes viral and you make 100,000 dollars from it, this means you now have $100,018 and you chose to move to Shanghai, where there is no extradition treaty.")
  print("game over!")
  exit(0)

elif prompt == "3":
  print("You drove lots of people to events for New Years Eve and made $300. You now have $318. Unfortunately that's not enough money for a plane ticket, you have to buy a hotel room and do more tomorrow. You book a night at a hostel for $99 and now have $219.")
  
prompt = input("continue?")
if prompt == "yes":
 print("\x1b[2J\033[H")
elif prompt == "no":
 print("Game over")
 exit(0)
else:
  pass

prompt = input("It is morning, you need to figure out how to make money. You decide to rob houses. There are some rich people away on vacation, let's rob them! We can rob house a or house b, which house do you want to rob? 1 for house a, 2 for house b")

if prompt == "1":
 print("You got lots of items and were successful robbing this person on vacation. You go to a shop to sell the items and you earn $1,000 dollars. This means you have $1,219. You use this money to buy a plane ticket to Tbilisi where there is no extradition treaty.")
 print("game over!")
 exit(0)

elif prompt == "2":
  print("You accidentally robbed someone who is home, they called the police and you are now being sent to federal prison.")
  print("game over!")
  exit(0)
