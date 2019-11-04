character_stats = {
    'Name': 'New Player',
    'Strength': 10,
    'Dexterity': 10,
    'Intelligence': 10,
    'Charisma': 10}

print("What is your name?")
new_name = input()
character_stats['Name'] = new_name
print("Ah, your name is", character_stats['Name'], "what an odd name. But let me learn a little bit about you. If you were met with a conflict would you react by \n A.Running \n B.Fight Back \n C.Out Smart Your Opponent \n D. Talk Your Way out?")
question_one = input()
if question_one == "A":
    character_stats['Dexterity'] += 1
elif question_one == "B":
    character_stats['Strength'] += 1
elif question_one == "C":
    character_stats['Intelligence'] += 1
elif question_one == "D":
    character_stats['Charisma'] += 1
else:
    print("You're not very bright are you?")

print(character_stats['Dexterity'])
