import random
jobs =[]
jobs.append(input("Enter a Job => "))
jobs.append(input("Enter a Job => "))
jobs.append(input("Enter a Job => "))
jobs.append(input("Enter a Job => "))
jobs.append(input("Enter a Job => ")) # take User Input for Jobs to use in the Atributes later.
names = [
    "Aiden", "Liam", "Noah", "Elijah", "James", "William", "Benjamin", "Lucas",
    "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Matthew", 
    "Jackson", "Sebastian", "Jack", "Owen", "Samuel", "David", "Joseph", 
    "Carter", "Wyatt", "John", "Luke", "Asher", "Gabriel", "Anthony", 
    "Dylan", "Isaac", "Joshua", "Christopher", "Andrew", "Leo", "Lincoln", 
    "Theodore", "Ryan", "Nathan", "Adrian", "Christian", "Maverick", 
    "Colton", "Jaxon", "Easton", "Harrison", "Jeremiah", "Hunter", 
    "Cameron", "Connor", "Santiago", "Eli", "Jameson", "Miles", "Robert", 
    "Julian", "Jordan", "Grayson", "Isaiah", "Zachary", "Charles", 
    "Dominic", "Jose", "Adam", "Ezekiel", "Jesse", "Evan", "Waylon", 
    "Silas", "Axel", "Gavin", "Roman", "Xavier", "Victor", "Carlos", 
    "Eli", "Gage", "Jorge", "Nicolas", "Kaden", "Ryder", "Sawyer", 
    "Tristan", "Dante", "Amari", "Emmett", "Milo", "Theo", "Riley", 
    "Jax", "Kingston", "Rhett", "Zane", "Hayden", "Brandon", "Paxton", 
    "Kai", "Braxton", "Jaden", "Beckett", "Colt", "Luca", "Avery", 
    "Sadie", "Maya", "Aria", "Scarlett", "Ella", "Chloe", "Grace", 
    "Isabella", "Sofia", "Charlotte", "Zoe", "Lily", "Aurora", "Nora", 
    "Hannah", "Aubrey", "Addison", "Layla", "Ellie", "Brielle", "Clara", 
    "Evelyn", "Willow", "Lucy", "Naomi", "Emery", "Nova", "Savannah", 
    "Sienna", "Violet", "Mila", "Cora", "Stella", "Piper", "Riley", 
    "Luna", "Mackenzie", "Bailey", "Kennedy", "Cecilia", "Rachel", 
    "Alyssa", "Samantha", "Madison", "Lydia", "Serenity", "Angela", 
    "Jordan", "Giselle", "Maya", "Lilah", "Leah", "Peyton", "Julia", 
    "Tessa", "Kinsley", "Lola", "Ariana", "Briar", "Remi", "Marley", 
    "Selena", "Zara", "Isla", "Skye", "Daisy", "Aspen", "Greta", 
    "Maggie", "Mia", "Lyra", "Rory", "Willow", "Harper", "Poppy", 
    "Jasmine", "Addilyn", "Finley", "Lennon", "Cassidy", "Alaina", 
    "Savanna", "Brooklyn", "Hadley", "Anastasia", "Callie", "Tatum", 
    "Kaitlyn", "Mabel", "Sloane", "Sabrina", "Holly", "Gianna", 
    "Ember", "Malia", "Lindsey", "Rosalie", "Blaire", "Marigold", 
    "Ayla", "Kylie", "Sierra", "Zuri", "Clementine", "Ophelia", 
    "Raven", "Wren", "Nina", "Jovie", "Sienna", "Dahlia", "Kira", 
    "Mina", "Nyla", "Misty", "Lainey", "Anya", "Zadie", "Elsie", 
    "Freya", "Rhea", "Vera", "Mina", "Juno", "Greer", "Hattie", 
    "Dahlia", "Selah", "Zelda", "Harlow", "Lyric", "Zella", 
    "Gemma", "Everly", "Lacey", "Fern", "Clio", "Breeze", "Sable", 
    "Karma", "Cypress", "Juniper", "Indigo", "Onyx", "Storm", 
    "Willa", "Nova", "Ivy", "Faye", "Zinnia", "Briar", "Autumn", 
    "Brinley", "Cleo", "Dove", "Elowen", "Kaia", "Marin", "Noelle", 
    "Sabine", "Tanith", "Willow", "Zara", "Jade", "Ember", "Celeste", 
    "Lola", "Felicity", "Lana", "Maisie", "Tallulah", "Cressida", 
    "Amaya", "Emilia", "Rhiannon", "Ines", "Elena", "Fiona", 
    "Estelle", "Viola", "Chloe", "Rowan", "Amara", "Laila", 
    "Nadia", "Rina", "Kyra", "Sapphire", "Alba", "Lia", "Soleil", 
    "Blythe", "Inez", "Odette", "Demi", "Siri", "Selene", 
    "Amelie", "Mirabelle", "Coraline", "Opal", "Etta", "Flora", 
    "Mabel", "Cypress", "Clarity", "Adira", "Bijou", "Kalani", 
    "Luna", "Miranda", "Ophelia", "Yara", "Zara", "Kia", 
    "Amani", "Mira", "Cecily", "Briony", "Lilac", "Ember", 
    "Sable", "Vivian", "Odessa", "Ianthe", "Lyra", "Clementine", 
    "Saffron", "Liora", "Soleil", "Elara", "Isolde", "Maia", 
    "Zadie", "Astrid", "Kaia", "Orla", "Lilith", "Harlow", 
    "Zinnia", "Amity", "Romilly", "Carys", "Zuri", "Indie", 
    "Leonie", "Marigold", "Cleo", "Elowen", "Brinley", "Iris", 
    "Seren", "Lyric", "Freya", "Lana", "Opal", "Carys", 
    "Calliope", "Elysia", "Junia", "Amity", "Elara", "Gemma", 
    "Thalia", "Wren", "Flora", "Astrid", "Niamh", "Elodie", 
    "Iona", "Aisling", "Rhiannon", "Cerys", "Imogen", "Sylvie"
]
#Make a pool of names for NPC creation
NPCSn = []
for i in range(11):
    NPCSn.append(random.choice(names))
    
#Create ten NPCS names in A List 
NPCSa = []
for i in range(11):
    NPCSa.append(random.randint(18,60))
#Create a List of Ten NPCS Ages
NPCSj = []
for i in range(11):
     NPCSj.append(random.choice(jobs))
#Add A Job for the NPCs in a list

NPCSe = []
for i in range(11):
     NPCSe.append(random.uniform(1.0, 10000.0))
# :.2f will  Round it in the Print Statement
NPCSp = []
for i in range(11):
     NPCSp.append(random.randint(-100,100))
#Add a Power Level

print("NPC 1", "\n"
    "Name:", NPCSn[1], "\n"
    "Age:", NPCSa[1], "\n"
    "Job:", NPCSj[1], "\n"
    "EXP:", (round(NPCSe[1], 2)), "\n"
    "Power:", NPCSp[1], "\n"
    )
print("NPC 2", "\n"
    "Name:", NPCSn[2], "\n"
    "Age:", NPCSa[2], "\n"
    "Job:", NPCSj[2], "\n"
    "EXP:", (round(NPCSe[2], 2)), "\n"
    "Power:", NPCSp[2], "\n"
    )

print("NPC 3", "\n"
    "Name:", NPCSn[3], "\n"
    "Age:", NPCSa[3], "\n"
    "Job:", NPCSj[3], "\n"
    "EXP:", (round(NPCSe[3], 2)), "\n"
    "Power:", NPCSp[3], "\n"
    )

print("NPC 4", "\n"
    "Name:", NPCSn[4], "\n"
    "Age:", NPCSa[4], "\n"
    "Job:", NPCSj[4], "\n"
    "EXP:", (round(NPCSe[4], 2)), "\n"
    "Power:", NPCSp[4], "\n"
    )

print("NPC 5", "\n"
    "Name:", NPCSn[5], "\n"
    "Age:", NPCSa[5], "\n"
    "Job:", NPCSj[5], "\n"
    "EXP:", (round(NPCSe[5], 2)), "\n"
    "Power:", NPCSp[5], "\n"
    )

print("NPC 6", "\n"
    "Name:", NPCSn[6], "\n"
    "Age:", NPCSa[6], "\n"
    "Job:", NPCSj[6], "\n"
    "EXP:", (round(NPCSe[6], 2)), "\n"
    "Power:", NPCSp[6], "\n"
    )    
    
print("NPC 7", "\n"
    "Name:", NPCSn[7], "\n"
    "Age:", NPCSa[7], "\n"
    "Job:", NPCSj[7], "\n"
    "EXP:", (round(NPCSe[7], 2)), "\n"
    "Power:", NPCSp[7], "\n"
    )
    
print("NPC 8", "\n"
    "Name:", NPCSn[8], "\n"
    "Age:", NPCSa[8], "\n"
    "Job:", NPCSj[8], "\n"
    "EXP:", (round(NPCSe[8], 2)), "\n"
    "Power:", NPCSp[8], "\n"
    )    
print("NPC 9", "\n"
    "Name:", NPCSn[9], "\n"
    "Age:", NPCSa[9],"\n"
    "Job:", NPCSj[9], "\n"
    "EXP:", (round(NPCSe[2], 2)), "\n"
    "Power:", NPCSp[2], "\n"
    )
print("NPC 10", "\n"
    "Name:", NPCSn[10], "\n"
    "Age:", NPCSa[10],"\n"
    "Job:", NPCSj[10], "\n"
    "EXP:", (round(NPCSe[10], 2)), "\n"
    "Power:", NPCSp[10], "\n"
    )
#Display the Ten NPCS Name, Age, and Atribbutes
