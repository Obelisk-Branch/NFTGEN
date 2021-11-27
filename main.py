import PIL
import random
from PIL import Image

#Can improve this implementation to make more random
#     Generating random number

i = 0
while i < 20:

    rand = random.randint(1, 3)

    base = Image.open("assets/base/" + str(rand) + ".png")
    rand = random.randint(1, 2)

    hair = Image.open("assets/hair/" + str(rand) + ".png")
    rand = random.randint(1, 3)

    nose = Image.open("assets/nose/" + str(rand) + ".png")
    rand = random.randint(1, 2)

    mouth = Image.open("assets/mouth/" + str(rand) + ".png")
    rand = random.randint(1, 2)

    eyes = Image.open("assets/eyes/" + str(rand) + ".png")

    character = base


    (character.paste(hair, (0,0), hair))

    (character.paste(nose, (0,0), nose))

    (character.paste(eyes, (0,0), eyes))

    (character.paste(mouth, (0,0), mouth))

    #Resizing and upsampling the character
    resized_character = character.resize((1200, 1200), resample = Image.NEAREST)
    print("We made a character!")

    #Saving character to path
    resized_character.save("characters/OmicronFailure" + str(i) + ".png", "PNG")
    i += 1