import random
magic_8_ball_responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."]
print ("Welcome to the MAGIC 8 BALLLLLLLLLLLLLL")
raw_input("Please ask a YES or NO question and you will receive your answer.")
print(magic_8_ball_responses[random.randint(0,4)])