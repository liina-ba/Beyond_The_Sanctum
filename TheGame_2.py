import pygame
import sys
pygame.init()
import CharactersDetails
pygame.mouse.set_visible(False)


def play_click_sound():
    click_sound.play()
click_sound = pygame.mixer.Sound("mouse-click-153941.mp3")
def play_game2():
    global scroll_speed

    WIDTH, HEIGHT = 1238, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Beyond The Sanctum")
    background = pygame.image.load('BG4.png')
    background1= pygame.image.load('BG4.png')
    font = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 25)
    font0 = pygame.font.Font("times new roman italic.ttf", 20)
    font1 = pygame.font.Font("Cinzel-VariableFont_wght.ttf", 30)
    font2 = pygame.font.Font("CinzelDecorative-Regular.ttf", 60)
    font3 = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 70)
    font0_0 = pygame.font.Font("times new roman italic.ttf", 25)
    timer = pygame.time.Clock()

    scroll_offset = 0
    scroll_speed = 30
    line_visible = True

    text16_5 = "I am a beacon in the dark, yet unseen;\nI am a guide in times of doubt, yet unseen;\nI am a wellspring of truth, yet unseen;\nI am a treasure of the mind, yet unseen.\nWhat am I?"
    text16_6 = "Be cautious, you have only one opportunity.\n Press  'Play'  for a hint to solve the riddle. "
    text17 = "CONGRATULATIONS! You've solved the riddle and uncovered the answer. 'Wisdom' || smartness is indeed the key to unlocking many doors. Well done!”\n\nAs Aiden confidently speaks the word ”wisdom”  aloud, he steps forward to the grating, fingers poised over the keypad attached to its surface. With each letter input, there's a soft beep, echoing in the stillness of the forest. As the final letter is en-tered, there's a moment of suspense, followed by a satisfying click.The door opens "
    text17_1 = "As you and Thalos step into the grate , a strange scent fills the air. It's both sweet and musky, enveloping them completely.\n Suddenly, they feel dizzy, their vision blurring as they collapse to the ground, uncon-scious. \n\nOnce you opens your eyes, you find yourself surrounded by humans like you, their eyes fixed upon you with a mixture of curiosity and caution.. \n\n“who are you and how did you find us?!” yells at you Raventhorn, the leader of the tribe. "
    text17_1_1 = "“it’s not what you think I promise!” you say with a shaking voice\n\nraventhorn : “why would we believe you”\n\nand before you say another word The guards tie you up\n\nThalos : “ see aiden you should’ve let me speak”"
    text17_2 = "Thalos : “we are not with the Grimroshers”\n\nraventhorn : “why would we believe you”\n\nand before you say another word The guards tie you up"
    text17_3 = "an old feminine voice resonates within the cave..\n\nBeth : “this is a human like us! Set them free, it’s an order,\n\nmay you excuse them, please follow me ”"
    text17_5 = "you follow Beth to a very old fashioned chamber, isolated from the rest of the tribe.\n\nBeth: “please come in..”"
    text18_1 = "“thank you for believing us.. who are you madam?”\n\nBeth : “Elizabeth, you can call me Beth, that’s it you have your answer”"
    text18_2 = "Beth : “I saw in you something little boy, something I didn’t see in anyone before, what’s your name?”\n\n“I am aiden”\n\nBeth : “and you are..?” she asks thalos\n\nthalos : “my name is thalos, Aiden's guide.”\n\nBeth : “Oh are you a centaur ? ..this  reminds me a lot of Marcus Evergreen when he tried once to make a serum to fight the Grim rushers..”\nyou and thalos look at each other flabbergasted from what you just heard\n\nThalos : “I took his serum, and aiden is his son..”\n\nBeth : “seems like Im still pretty good at it, I knew it from the beginning!” she smirks, “now tell me aiden, what brought you here?” "
    text19 = "you explain everything to Elizabeth..\n\nBeth : “could you show me the recipe,please”"
    text19_1 = "“here..”\nBeth : “oh lord.. you found it!! it’s the Zafr!”\n\n“im sorry.. what?” you ask confused\n\nBeth : “this is the recipe we have been searching for decades, it’s their drink, Zafr!”\n\n“I still don’t get it ma’am ..”\n\nThalos : “will you please let her explain aiden?? ”\n\nBeth : “ (we owe it our survival) they said..\nthis, is the drink the grimrushers get their power from, tons of books have been writ-ten about it, but no one ever knew what it was made of. ”\n\nElizabeth rushes upstairs to get a book, “the Grimrushers and beyond”.\n\nBeth : “it says ..\n\neach month, in a place where the four paths meet, at the first beam of moonight, the veroccuso and shivereana rise, small as a hand palm, strong as the ocean in a stormy night, in the lowest yet highest room of the palace, the crytalin water gushes, all in the service of what they need.. beware, they see you, and hear each step..”\n\n“do you know where the four paths meet?”\n\nBeth : “oh yes I do, it’s a tedious challenging journey, but it’s worth all your efforts, our future saviors”"
    text19_2 = "Aiden:“also.. like I told you earlier, the serum I took gave me some powers, but I don’t really know how to control them”\n\nBeth : “Haha I knew it, you’ve come to the right place Aiden"
    text19_3 = "Beth laughs hard at your statement, skeptical, \nBeth : “aiden you are not going anywhere, not until you learn to control your powers, you are too weak now..”\n\n“don’t I already know how to do that?” you ask\n\nBeth : “aiden, you don’t need to know how to do it, you need to master\nit, it’s not a game..”"
    text19_4 = "“Elizabeth approaches the wall and performs strange movements with her hands, and then the wall opens, revealing a very large training room equipped with all the necessary tools.“\n\n“Beth! That’s crazy!” you say excitingly \n\nBeth : “I know ! Please come in.. you thalos can read the book I brought earlier, it will help a lot” \n\nThalos looks at you for reassurance, asking if everything will be alright. \n\nWith a nod, you reassure him."
    text19_5 = "you approach the old lady, your gaze filled with curiosity and apprehension… \n\n“so, how will you teach me to control my powers?“ you ask.\n\nThe old lady smiled gently before responding. She began by recounting an ancient tale…"
    text19_6 = "you stood before Beth ready to embark on your journey to master your powers.\n\nBeth begins by initiating you into connecting you with your mind, allowing you to discover your inner voice, insisting that therein lay the key to mastery.\n\nBeth : “ready?” type ready if you are."
    text20 = "The first step : is  learning how to control fire and light. Ready?”\n\nAiden:”yes”\n\nFocus on the fire burning within you, that burning energy that seeks to express itself. "
    text20_1 = "Now Imagine yourself surrounded by flames, but instead of consuming you, you control them and Feel their warmth, their power, but also their obedience to your will.\n\nBeth : “Do you see that flame there? I want you to recreate it with one hand.“ \n\nyou try really hard, laser focused, but yet, fail to create a single small flame.\n\n“ Beth I.. I can’t it doesn’t work! What am I doing wrong?”\n\nBeth : “the only thing you did wrong, is that you tried one single time, I will let you few hours alone, keep practicing, practice makes perfect son. Believe in yourself, because I believe in you, we all do”\n\n“maybe I should ask thalos for help, or shouldn’t I?” you think"
    text20_2 = "you decide to make it your own responsibility, and keep practicing alone like beth said."
    text20_3 = "“hey thalos, I need your help..”\n\nThalos : “ is it about the fire you couldn’t make? Beth knew you were going to ask me, I can’t aiden I’m not allowed to..”\n\n“but why? Does she hate me?”\n\nThalos : “it’s the opposite aiden She believes in you..it’s your responsibility, your powers, your life, what if I die? Or go to jail?”\n\nyou know he is right, you thank him and leave to keep practicing."
    text20_5 = "Few hours passed, failure after failure, you finally make it, you manage to create your first flame. \n\n“Yes ,I did it!! I can’t believe it, Beth!”\nyou run to beth to announce it to her.\n\nBeth : “see son, never back down never what?”\n\n“ Never Give Up“\n Beth : “ you have to rest now..” "
    text20_6 = "The Next Day………..\n\nyou wake up excited for what is waiting for you today, you run to beth..\n\n“good morning Elizabeth!! I. Am. Ready.” you say excitingly\n\nBeth : “that’s the energy you need in life, today we will work on your power of light, as far as I know you did it before, so we will make slightly more complicated”\n\nFirst imagine yourself surrounded by a luminous aura, but instead of being dazzled, you are its master.\n\n Feel its brightness, its clarity, but also its gentleness. See yourself full on light to the point where you are.. invisible"
    text20_7 = "After much perseverance, you succeed in the challenge. you open your eyes, your determination reflected in your gaze.\n\nWith one hand, you control the dancing flames, while with the other, you modulate the light, directing it confidently to the desired location.\n\nCongratulations Aiden, you've done 30% of the work, but the hardest part remains : learning to control minds.\nBut now you must take a reset we will continue tomorw."
    text20_8 = "The Next Day...\nBeth : “good morning aiden! Today, you will learn to control minds.\n\nThe first step : is influencing the thoughts of others. \n\n“You see that vase on the floor, you must be able to command me to lift it and place it on the table.“ \n\nwrite “done” for each accomplishment.\n\nFirst, close your eyes, let your mind calm. Listen to the whispers of your soul, feel its presence within you. \n\nNow, focus on your goal. Visualize what you want to accomplish and  choose a thought you want to transmit to me.\n\nBeth :  ”Give me an order.” \n\nSpeak your message with confidence, it is the moment. Let your voice resonate with the authority of your mind, persuading those who listen to follow your will."
    text20_9 = "With a hypnotic voice, you dictate to her what she must do. Suddenly, Beth lifts the vase and places it on the table without\n\nrealizing it, then regains her senses. Impressed by what you had just accomplished, the woman is sure you are the chosen one.\n\nBeth : “Impressive! How did you manage to do it on your first try? I am proud of you, but know that learning to control minds is an immense responsibility. You will need to show discipline and discernment\n\nWe will keep practicing for the upcoming weeks until you are the master.”\n\nWith each success, your confidence grows.. Guided by the teachings of Elizabeth and faced with a series of challenges, you begin to grasp the extent of your potential. "
    text21 = "Beth : “ aiden darling we ran out of fuel could you please warm my tea?”\n\n“sure ma’am.. !” you smirk\n\nyou and beth sit in silence when thalos comes in ..\n\nThalos : “Elizabeth, I’ve read all the books and scriptures, what’s next?”\n\nBeth : “next step is you leave for the ‘where the four paths meet’ ”\n\nsurprised you ask : “should we move already? Isn’t it too early?”\n\nBeth : “no aiden, it’s the perfect time now, the grimrushers are busy preparing for their royal ceremony..”"
    text21_1 = "“sure thing then, we will leave.. and we will come back winners Elizabeth! Thank you again for everyhing”\n\nBeth : “ Oh! I almost forgot, my memory’s leaving soon may you please forgive me ”\n\n“it’s okay beth, what is it?”\n\nBeth : “see on the map, there is a sculpture, when you reach it, you know you’re there. Take this sword aiden, you have to kill the king with this sword.”\n\nAiden: “Why exactly is this sword so special?“ Beth: This sword was created at the same time as the first Grimrushers, using the same serum, to neutralize them in case of rebellion. However, it mysteriously disappeared without a trace. Fortunately, one of our men found it at the bottom of a river and brought it back to us.\n\n“how do we know we’ve reached the sculpture?”\n\nBeth : “ask the villagers, ask them for the fontain”\nyou say your last goodbyes to Elizabeth, pack your things and leave for an unknown future searching for the composants of the Zafr."
    text21_2 = "you and Thalos stand at the entry of the Soliar catacomb.. your faces etched with determination.\n“This is it, Thalos,“ you say, your voice tinged with excitement as you adjust the strap of his pack. “The beginning of our journey.“\n\nthalos : “the map aiden”\n\n“here..”\n\nthalos : “ Beth said that it’s not too far away from the palace, so let’s go there”\nyou nod in agreement.\n\nyou start moving towards the kingdom facing multiple difficulties, the first one is dealing with the forest’s monsters..\n\neach night you camp in the woods hoping that nothing sees you there\n\nyou see a nice place to camp, move there\n"
    text21_3 = "“seems good thalos doesn’t it?”\n\nthalos : “i’d say so, light the fire let’s fuel our bodies”\n\nyou and thalos eat from what Beth gave you before you left, and went to sleep.\nYou hear some heavy footsteps near the tent, scared you wake thalos up\n\n“did you hear that?”\n\nThalos : “I did but it’s no big deal I guess”\n\n“it it!, I’m going out to see what’s in there”\n\nfew seconds after you left the tent and see a huge animal about to attack you.."
    text22_1 = "nice choice.\n\nFocus.\n\nlook at the animal , raise your hand and make lots of light to scare it away."
    text22_2 = "This option doesn’t work with animal, it only works on creatures who have consciousness"
    text23 = "Thalos : “what was that?! Are you okay?”\n\n“yes perfectly intact, you?”\n\nthalos : “couldn’t you wait for me to come”\n\n“we would be dead..”\n\nyou go back to sleep, and keep seeking the palace.\n\ndays have passed, and you are now out of the forest.\n\n“so what does the map say? Are we close enough?”\n\nthalos : “almost I guess.. we are close to the sculpture”\n\n“the moonlit night is close too isn’t it, we have to rush”\n\nthalos : “yes it’s in two days, we don’t have much time left”\n\n“there is a villager there, let’s ask him”\n\nthalos : “you know what to do aiden..”"
    text24 = "villager : “You are human! I will call the guards! Guards! GUARDS!”\nyou have to control his mind to tell you what you want.\n Look at him closely, focus on him and set clear what you want from him.\n\nvillager : “oh sorry little boy, was I shouting at you ?”\n\n“n-no it’s okay.. please sir where can we find the Foutain? Show him the map thalos”\n\nvillager : “ you’re almost there sir, see that mountain ?” he said pointing at the mountain, “the foutain is just behind it”\n\nthalos : “thanks a lot we will leave now”"
    text25 = "You are now at The Fountain.\n\n“great so we are now at The Fountain which is also Where the four paths meet, what now thalos?”\n\nthalos : “in a book I read, it said we have to tell them what they want to hear”\n\n“who is them?”\n\nthalos :  “the Guardians, it’s a very sacred place for the grimrushers, they owe it their survival”\n\n“what could they possibly want to hear?”\n\nthalos : “our voice? Our Echo in the place? ”\n\n“you are so funny thalos, literally so funny that I’m dead”\n\nwhen suddenly, the mountain you passed earlier produces a loud sound, you turn around and see an entry in the mountain that appeared out of nowhere.\n\n“thalos! Do you see that!”\n\nthalos : “I can’t believe it.. let’s enter”"
    text26 = "you hear a voice saying..\n\nCongratulations grims, you found the word.. you can come in.\n\n“we said the word? What was it?”"
    text28 = "Correct! The word was “Echo” remember it in case you need it.\n\n“it’s easier than what I thought!”\n\nthalos : “we were lucky on this one, let’s not waste more time now, it’s almost night time and we must be there at midnight and get the plants before the grimrushers, we have three hours left aiden”\n\nthere are very high stairs in the place, "
    text29 = "“It seems like we’re at the top of the mountain!”\n\nYou see a small cave near by to hide until midnight comes.\n\nthalos : “let’s move now aiden, it’s time”"
    text30 = "you start walking trying to find the plants, when you see a green light in the horizon..\nyou go to the light.\n\nthalos : “Aiden! There! Th-The plants!!”"
    text30_1 = "you perceive \n\nThe plants are planted in a sumptuous royal garden well guarded by a powerful green sphere..\n\n“how do we get rid of the sphere?” you ask\n\nthalos : “the sphere is made of pure emotions, the grimrushers are very angry creatures, the strongest the anger, the stronger the sphere, it should be weaker by now since it’s almost midnight, Beth handed me a powder that I can use break the sphere with my powers”\n\n“perfect! So you disable the sphere and I burn the plants, once done we go seperate ways to avoid getting caught, I’ll hide now”"
    text32 = "you are now hidden in a small trap near thalos waiting for him to break the sphere. When you suddenly hear the grimrushers coming to the place.\n\n“thalos hurry up!they’re coming!” you whisper \n\nthalos manages to break the sphere successfully withing a couple minutes.\n\nthalos : “great! The plants now! few minutes left before the grims arrive, you go east I go west”\n\nyour turn aiden, you have to burn the plants now.\n\nFocus on the target and make the fire."
    text33 = "You go to the next area of the land and Make fire.\n\n The plants are burning, the smoke is spreading.. \n\nyou hear the grimrushers screaming like beasts from the south area..\n\nreaussured you say : “thank god thalos is at the west..”\n\nsuddenly you hear a famillar voice fighting the monsters. It’s thalos, they’re taking him with them."
    text33_1 = "you are brave aiden. But remember what thalos said before the mission started..\n\n“if anything happens to me.. Don’t. Come. Thay can’t take us both, Flee!”"
    text33_2 = "great choice. You decide to stay hidden and follow Thalos and his captors to the Grimrusheres' village.\n\n“I don’t even have the map.. gotta find another way”\n\nGuided by your determination, you avoid monster patrols, seeking a way to save you captured friend. \n\nAiden, are you ready to plunge into the lion's den?"
    text34 = "you spot lamplights illuminating every street corner. Whispers carry your name through the dark alleys, revealing that the entire village is searching you.\n\nWill Aiden remain hidden?"
    text36 = "“GET HIM! IT’S A HUMAN!” the guards caught you running, you can’t control all their minds.\n\nThey tie you up.\n\nGuard1 : “Haha-where did you think you were going little human? ”\n\nGuard2 : “to the dungeon most definitely am I right?!”"
    text38 = "Aiden decides to hide, monitoring the situation. As dawn breaks, the commotion subsides, and most Grimrockers return to their usual concerns. This land is bordered by wooden stakes, marking the boundary between civilization and the darkness of the surrounding forest. Security is not as strict as expected, with only a few Grimrockers lazily patrolling.\n\nApproaching the village, Aiden spots a group of guards patrolling near the entrance."
    text39 = "Using his mastery of light magic, he suddenly creates a dazzling explosion in the sky, temporarily blinding the Grimrockers.\n\nWhile they blink disoriented, Aiden skillfully throws a branch into the woods, creating a resounding noise that attracts their attention. As the guards rush to investigate, Aiden sneaks into the village unnoticed.\n\nMoving through the alleys without being caught, Aiden is astonished to discover that the Grimrockers live like humans, cultivating their own fruits and vegetables and favoring barter over money for trade. He sees their children laughing and running around. This observation challenges his perception of Grimrockers as enemies. Suddenly, Aiden remembers his mission, turning back.\n\nHe is approached by a huge Grimrosher dressed in nomadic attire, wearing a scarf on his head who reveals that he was searching for him and that he is on the same side as him."
    text39_1 = "You decide to flee but suddenly the Grim pulls you towards him to hide you from the guards\n\nSeeing what he has done, you decide to trust him."
    text39_2 = "[Grim] “I am opposed to the system that tortures and eats humans.“ The Grimrucher expresses admiration for Aiden's exploits and his willingness to help in his quest to destroy their system that aimed to Harm humanity. Aiden realizes that there are unlikely allies even among the declared enemies of Sanctum.\n\nAware of the danger awaiting Aiden in the Grimruchers' village, the  Grimrucher proposes to guide him to the castle where Thalos was held. "
    text40 = "With caution, you navigate through the dark alleys, avoiding the curious glances of the village inhabitants. The Nomad knows the secret passages and detoured paths that lead to the castle, having explored every corner of the village in his quest for freedom. He guides you with quiet determination until you reach a small door.\n\nGrim : “that’s it aiden, I can’t go any further or they will notice my disappearence, this secret passage will lead you directly to the palace”\n\nBefore parting ways, he shares information about the guards' habits and the traps to avoid along the way.\n\n“thanks a lot sir! May you tell me your name so that I can tell the humans about you when I go back”\n\n[grim]:”call me just the Nomad”.\n\nAs you advance through the dark corridors of the castle, you suddenly face an unexpected obstacle: a series of magical traps hidden in the floor. These traps are activated by magical sensors, making their detection difficult for someone who is unaware of their existence.\n\nAiden, you must find a way to bypass these traps without triggering their detection mechanism."
    text40_1 = "you carefully observe the floor, looking for subtle signs that could indicate the presence of these deadly traps. Look at a series of engraved patterns on the floor, indicating the exact locations of the magical sensors."
    text40_2 = " yes.. you can make fire, light and control people’s minds, but you are not invisible.."
    text41 = "you use your magic to temporarily deactivate the sensors, allowing you to safely cross the trap-ridden area.\n\nFinally, you reach a grand staircase leading to the upper floors of the castle. With increased caution, you ascend the steps. At the top of the stairs, you find themselves facing a large ornate door, guarded by two Grimrucher soldiers.\n\nAs you try to escape after being spotted by the soldiers, you quickly find yourself surrounded and captured by the royal guard. Despite your efforts to break free, you are quickly subdued and dragged to the throne room, where the Grimrucher king awaits you with a mocking smile.\n\nKing : “kneel down Aiden”"
    text42 = "“no, I will not!”\n\nThe king then orders his two soldiers to hold you on your knees before him. your muscles tensed from the struggle and resistance, you are forced to kneel down\n\nking : “well, you just did :) ”"
    text43 = "“Oh, Aiden, what a pleasure to see you, you resemble your father so much,“ his eyes filled with rage and anger, with a burning desire for revenge. “Before I execute you, I will do you the honor of telling you a story. Long ago, humans lived in harmony with nature and themselves. The joy of life and brotherhood were ingrained in their veins. Years passed and man evolved and so did science. The government assembled a team of researchers and scientists to create a stronger, faster, and magically empowered supernatural being that would change the course of history. After 20 years of relentless research, they developed a serum composed of a substance extracted from a rock called Jadeite, the only one that existed in this world, and other molecules. They ended up injecting it into me, who was part of the project without my knowledge. At first, everyone was happy. The serum worked wonders. I was subjected to trials that no human being could pass. The government ordered more like me to be created, and since it was impossible to create other serums, they took stem cells from me and injected them into the blood of other humans who were not aware of the project like me. Subsequently, things started to go wrong. Our metabolism and physique changed, anger invaded our hearts, and our strength became increasingly uncontrollable. Scientists and the government were worried but what they didn't know yet was that our intelligence had also greatly developed. We became monsters and eventually established an escape plan. We managed to escape and wreaked havoc among humans. Many lost their lives until the day they built Sanctum, we call it the humans' cage. We allowed them to live there but under one condition: that no one would leave the walls. Everything went as planned until the system decided to send explorers outside of Sanctum. We killed and ate them one by one. Including your father, Aiden.“"
    text44 = "Overwhelmed by anger and melancholy, you use your voice. your eyes change color, reflecting the total void that fills your being. \n\nWith a deep, thunderous voice, you order one of the Grimrushers to kill his comrade. "
    text45 = "As this happens, you approache the king and strangle him with all your strength. The king, unable to call for help, arrogantly asserts his immortality, declaring that humanity is coming to an end. \n\n“things have changed your majesty, and I, will take revenge of all the innocent souls you killed, including my father” you say heartbroken \n\nyou remember the sword that elizabeth gave you.. “ it’s time” you think"
    text46 = "you then grabs the sword given to you by elizabeth and plunge it into the king's heart. \n\nThe monarch, bewildered, breathes his last breath as his soul sinks into the darkness of hell. > free thalos\n\nthalos : “Aiden you made it!! your father would be so proud”\n\nan awkward silence follows thalos words..\n\nthalos : “I am sorry for your loss aiden, guess we still have each other”\n\n“it’s okay thalos, thanks a lot, without you I couldn’t have made it! let’s move now”\n\nTriumphant, you leave the castle and realize that all the Grimrushers are also dead. \n\n“what? How is that even possible? It the sword?”"
    text47 = "thalos : “yes!Aiden, they are all connected!”\n\n“what do you mean?”\n\nthalos : “look at that dying cell of the body, it’s the same cell in all the bodies, they carry the kings blood, if he dies, they all do”\n\nTriumphant, you leaves the castle and realize that all the Grimrushers are also dead. It is then that you understand that the Grimrockers were linked not only to the potion but also to the king himself, as they all carried his cells in their bodies and were connected to him.\n\nsince that day, humanity has experienced better days, and Aiden has become their hero and savior, and his name will be part of history now."
    text48 = "CONGRATULATIONS"
    text48_1 = " You have won and saved humanity."
    tex = "your fierce battle catches the attention of other Grimrushers lurking nearby and you find yourselves surrounded by a horde of snarling creatures, despite your best efforts, the sheer number of Grimrushers overwhelms you, with a heavy heart, you realize that victory is beyond your grasp and your journey comes to a premature end."

    def button_click_action2():
        CharactersDetails.BethDescreption(screen)

    class Button:
        def __init__(self, text, position, width, height):
            self.text = text
            self.initial_position = position
            self.rect = pygame.Rect(position, (width, height))
            self.color = (168, 127, 71)  # Default color for text
            self.hover_color = (210, 182, 143)  # Color when hovered
            self.clicked_color = (0, 0, 0)  # Color when clicked
            self.clicked = False
            self.visible = True  # Flag to determine if button is visible

        def draw(self, surface, scroll_offset):
            if self.visible:  # Only draw if visible
                # Adjust the button position based on scroll_offset
                adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
                self.rect = pygame.Rect(adjusted_position, self.rect.size)
                font_surface = font.render(self.text, True, self.color)
                font_rect = font_surface.get_rect(center=self.rect.center)
                surface.blit(font_surface, font_rect)

        def check_hover(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.color = self.hover_color
            else:
                self.color = (168, 127, 71)  # Reset to default color

        def check_click(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                # self.clicked = True
                self.color = self.clicked_color
                # self.visible = False  # Button is no longer visible
                return True
            return False

        def reset_click(self):
            self.clicked = False

    class CharButton:
        def __init__(self, text, position, width, height, action=None):
            self.text = text
            self.initial_position = position
            self.rect = pygame.Rect(position, (width, height))
            self.color = (168, 127, 71)  # Default color for text
            self.hover_color = (210, 182, 143)  # Color when hovered
            self.clicked_color = (0, 0, 0)  # Color when clicked
            self.clicked = False
            self.visible = True  # Flag to determine if button is visible
            self.action = action  # Action to perform when clicked

        def draw(self, surface, scroll_offset):
            if self.visible:  # Only draw if visible
                # Adjust the button position based on scroll_offset
                adjusted_position = (self.initial_position[0], self.initial_position[1] + scroll_offset)
                self.rect = pygame.Rect(adjusted_position, self.rect.size)
                font = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 25)
                font_surface = font.render(self.text, True, self.color)
                font_rect = font_surface.get_rect(center=self.rect.center)
                surface.blit(font_surface, font_rect)

        def check_hover(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.color = self.hover_color
            else:
                self.color = (168, 127, 71)  # Reset to default color

        def check_click(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                self.clicked = True
                self.color = self.clicked_color
                if self.action:
                    self.action()  # Perform the action
                return True
            return False

    def button_click_action():
        CharactersDetails.centaurs(screen)

    def button_click_action3():
        CharactersDetails.CryptedLetter(screen)

    def button_click_action1():
        CharactersDetails.RoyalCeremony(screen)

    def display_text(surface, text, pos, font, color, scroll_offset):
        max_width = WIDTH - 110  # Maximum line width
        space = font.size(' ')[0]
        line_spacing = 20  # Adjust this value for desired line spacing
        x, y = pos
        words = [word.split(' ') for word in text.splitlines()]
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height + line_spacing
                surface.blit(word_surface, (x, y + scroll_offset))
                x += word_width + space
            x = pos[0]
            y += word_height + line_spacing

    def draw_text_box(surface, position, size, background_color, border_color, alpha1, scroll_offset):
        # Define the padding and border width
        padding = 15
        border_width = 1

        # Adjust the position based on the scroll offset
        adjusted_position = (position[0], position[1] + scroll_offset)

        # Create a transparent surface for the box
        box_surface = pygame.Surface(size, pygame.SRCALPHA)
        box_surface.fill((*background_color, alpha1))

        # Draw the border rectangle on the transparent surface
        border_rect = pygame.Rect((0, 0), size)
        pygame.draw.rect(box_surface, border_color, border_rect, border_width)

        # Blit the box surface onto the main surface
        surface.blit(box_surface, adjusted_position)

    def draw_line(surface, x1, y1, x2, y2, width, color, scroll_offset, visible=True):
        if visible:
            pygame.draw.line(surface, color, (x1, y1 + scroll_offset), (x2, y2 + scroll_offset), width)

    class TextField:
        def __init__(self, position, size, border_color, text_color, max_chars, correct_word, callback=None,
                     wrong_callback=None):
            self.rect = pygame.Rect(position, size)
            self.border_color = border_color
            self.text_color = text_color
            self.max_chars = max_chars
            self.text = ""
            self.active = False
            self.correct_word = correct_word
            self.callback = callback
            self.wrong_callback = wrong_callback
            self.gameover = False
            self.cursor_visible = True
            self.cursor_timer = 0

        def draw(self, surface, scroll_offset):
            # Adjust the position of the text field based on the scroll offset
            adjusted_y = self.rect.y + scroll_offset

            # Draw the text field at the adjusted position
            adjusted_rect = pygame.Rect(self.rect.x, adjusted_y, self.rect.width, self.rect.height)
            pygame.draw.rect(surface, self.border_color, adjusted_rect, 1)
            font = pygame.font.Font("EBGaramond-VariableFont_wght.ttf", 25)
            text_surface = font.render(self.text, True, self.text_color)
            surface.blit(text_surface, (self.rect.x + 5, adjusted_y + 5))

            # Draw cursor if active
            if self.active and self.cursor_visible:
                cursor_x = self.rect.x + 5 + font.size(self.text)[0]
                cursor_y = adjusted_y + 5
                pygame.draw.line(surface, self.text_color, (cursor_x, cursor_y),
                                 (cursor_x, cursor_y + font.size("A")[1]))

            # Display message if any

        def handle_event(self, event, scroll_offset):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse click is inside the text field
                if self.rect.collidepoint((event.pos[0], event.pos[1] - scroll_offset)):
                    self.active = True
                else:
                    self.active = False
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        # Check if entered text is correct
                        if self.text == self.correct_word:
                            # Execute callback function if provided
                            if self.callback:
                                self.callback()
                        else:
                            if self.wrong_callback:
                                self.wrong_callback()
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif len(self.text) < self.max_chars:
                        self.text += event.unicode

        def update_cursor(self, dt):
            # Update cursor visibility every 500 milliseconds
            self.cursor_timer += dt
            if self.cursor_timer >= 500:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer %= 500

    def handle_correct_answer():
        nonlocal dn
        # Set boolean value to true or perform any other action
        dn = True

    def handle_wrong_answer():
        nonlocal dn1
        dn1 = True



    dn = False
    done16_5 = False
    done17 = False
    done17_1 = False
    done17_2 = False
    done17_3 = False
    done17_4 = False
    done17_5 = False
    done18_1 = False
    done18_2 = False
    done19 = False
    done19_1 = False
    done19_2 = False
    done19_3 = False
    done19_4 = False
    done19_5 = False
    done19_6 = False
    done19_7 = False
    done19_8 = False
    done19_9 = False
    done20 = False
    done20_1 = False
    done20_2 = False
    done20_3 = False
    done20_4 = False
    done20_5 = False
    done20_6 = False
    done20_7 = False
    done20_8 = False
    done20_9 = False
    done21 = False
    done21_1 = False
    done21_2 = False
    done21_3 = False
    done21_4 = False
    done22_1 = False
    done23 = False
    done24 = False
    done25 = False
    done26 = False
    done27_1 = False
    done27_2 = False
    done27_3 = False
    done28 = False
    done29 = False
    done30 = False
    done30_1 = False
    done30_2 = False
    done31_1 = False
    done31 = False
    done32 = False
    done33_1 = False
    done33_2 = False
    done34_1 = False
    done34_2 = False
    done35_1 = False
    done35_2 = False
    done36 = False
    done37 = False
    done38 = False
    done39_1 = False
    done39_2 = False
    done39_3 = False
    done39_4 = False
    done40_1 = False
    done40_2 = False
    done40_3 = False
    done40_4 = False
    done41_1 = False
    done41_2 = False
    done42 = False
    done42_1 = False
    done42_2 = False
    done44 = False
    done45 = False
    done46 = False
    done36_3 = False
    done37_3 = False
    done37_2 = False
    done49 = False
    dn1 = False
    done16_4 = True

    button16_5 = Button(" > Play", (120, 570), 200, 50)
    button17 = Button(" > Enter the grate..", (90, 550), 300, 50)
    button17_1 = Button(" > 1- Respond", (120, 570), 210, 50)
    button17_2 = Button(" > 2- Let Thalos respond", (120, 630), 300, 50)
    button17_3 = Button(" > Continue", (120, 570), 200, 50)
    button17_4 = Button(" > Continue", (120, 460), 200, 50)
    button17_5 = Button(" > Continue", (120, 535), 200, 50)
    button18_1 = Button(" > 1- you ask her who she is and how she knows you", (130, 390), 520, 50)
    button18_2 = Button(" > 2- let her speak first", (120, 450), 250, 50)
    button19 = Button(" →", (960, 410), 200, 50)
    button19_1 = Button(" > Explain", (120, 980), 200, 50)
    button19_2 = Button(" > Take", (100, 435), 300, 50)
    button19_3 = Button(" > 1- Ask her about your powers.", (140, 1570), 330, 50)
    button19_4 = Button(" > 2- Ask her for the way where the four paths meet.", (200, 1630), 400, 50)
    button19_5 = Button(" > Continue", (120, 440), 200, 50)
    button19_6 = Button(" > Continue", (120, 550), 200, 50)
    button19_7 = Button(" > Follow Beth", (120, 660), 200, 50)
    button19_8 = Button(" > Continue", (120, 535), 200, 50)
    button19_9 = Button(" > Ready", (120, 480), 200, 50)
    button20 = Button(" > Done", (120, 480), 200, 50)
    button20_1 = Button(" > 1- keep practicing alone", (150, 830), 300, 50)
    button20_2 = Button(" > 2- reach out to thalos for help", (150, 890), 350, 50)
    button20_3 = Button(" > Continue", (120, 340), 200, 50)
    button20_4 = Button(" > Continue", (120, 760), 200, 50)
    button20_5 = Button(" > Rest", (120, 620), 200, 50)
    button20_6 = Button(" > Done", (120, 820), 200, 50)
    button20_7 = Button(" > Rest", (120, 650), 200, 50)
    button20_8 = Button(" > Done", (120, 1080), 200, 50)
    button20_9 = Button(" > Continue", (120, 830), 200, 50)
    button21 = Button(" > Continue", (120, 980), 200, 50)
    button21_1 = Button(" > Leave", (120, 1150), 200, 50)
    button21_2 = Button(" > Move", (120, 1030), 200, 50)
    button21_3 = Button(" > 1- Use light", (120, 880), 220, 50)
    button21_4 = Button(" > 2- Control its mind", (120, 940), 300, 50)
    button22_1 = Button(" > 1- Use light", (120, 350), 200, 50)
    button23 = Button(" > Go see the villager", (120, 1360), 300, 50)
    button24 = Button(" →", (960, 480), 200, 50)
    button25 = Button(" > Go behind the mountain", (120, 775), 350, 50)
    button26 = Button(" > Enter", (120, 1320), 200, 50)
    button27_1 = Button(" > 1- Voice ", (120, 450), 200, 50)
    button27_2 = Button(" > 2- Echo", (120, 510), 200, 50)
    button27_3 = Button(" > 2- Echo", (120, 370), 200, 50)
    button28 = Button(" > Go upstairs.", (120, 600), 250, 50)
    button29 = Button(" > Go out of the Cave.", (120, 460), 350, 50)
    button30_1 = Button(" > 1- A small trap on the floor ", (120, 1010), 400, 50)
    button30_2 = Button(" > 2- Behind a tree", (120, 1070), 300, 50)
    button31_1 = Button(" > Try again. ", (120, 350), 300, 50)
    button31 = Button(" →", (960, 350), 200, 50)
    button32 = Button(" > Done. ", (120, 750), 200, 50)
    button33_1 = Button(" > 1- go to save him", (120, 620), 280, 50)
    button33_2 = Button(" > 2- stay at your place and save him at the palace ", (120, 680), 550, 50)
    button34_1 = Button(" > Try Agian", (120, 380), 250, 50)
    button34_2 = Button(" > Ready ", (120, 555), 200, 50)
    button35_1 = Button(" > 1- Or will he rush without considering the consequences? ", (130, 450), 590, 50)
    button35_2 = Button(" > 2- Will Aiden remain hidden?", (120, 510), 350, 50)
    button37 = Button(" MENU ", (500, 580), 200, 50)
    button37_1 = Button(" MENU ", (500, 580), 200, 50)
    button37_2 = Button(" MENU ", (500, 580), 200, 50)
    button38 = Button(" > Use light magic to blind them. ", (120, 510), 400, 50)
    button39_1 = Button(" > 1- Flee ", (120, 830), 200, 50)
    button39_2 = Button(" > 2- Listen to what he has to say. ", (120, 890), 430, 50)
    button39_3 = Button(" > 2- Listen to what he has to say. ", (120, 400), 430, 50)
    button39_4 = Button(" > Accept ", (120, 500), 200, 50)
    button40_1 = Button(" > 1- Observe the room carefully. ", (120, 1160), 400, 50)
    button40_2 = Button(" > 2- Pass and trigger the mechanism. ", (120, 1220), 420, 50)
    button40_3 = Button(" > Magic ", (120, 340), 200, 50)
    button40_4 = Button(" > Try Agian ", (120, 310), 200, 50)
    button41_1 = Button(" > 1- Refuse. ", (120, 700), 200, 50)
    button41_2 = Button(" > 2- kneel down to king. ", (120, 760), 320, 50)
    button42 = Button(" →", (960, 480), 200, 50)
    button42_1 = Button(" > 1- You give up and accept your fate ", (120, 1320), 420, 50)
    button42_2 = Button(" > 2- You defend yourself and avenge your father.", (120, 1380), 500, 50)
    button44 = Button(" > Approach the king ", (120, 430), 300, 50)
    button45 = Button(" > Pull out the sword ", (120, 560), 300, 50)
    button46 = Button(" > take a look at a grimrushers body.", (120, 940), 460, 50)
    button49 = Button(" →", (960, 840), 200, 50)
    button37_3 = Button(" MENU ", (500, 480), 200, 50)

    Beth = CharButton(" Beth", (64, 247), 150, 50, button_click_action2)
    Script = CharButton(" scripts", (368, 296), 200, 50, button_click_action3)
    Royal = CharButton(" royal ceremony", (910, 830), 200, 50, button_click_action1)

    Wisdom = TextField((140, 690), (940, 40), (255, 255, 255), (255, 255, 255), 10, "wisdom", handle_correct_answer, handle_wrong_answer)

    while True:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        dt = timer.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            Wisdom.handle_event(events, scroll_offset)
            if events.type == pygame.MOUSEBUTTONDOWN:
                play_click_sound()
                if button16_5.check_click(mouse_pos) and done16_4:
                    done16_5 = True
                    scroll_offset = 0
                elif button17.check_click(mouse_pos)  and dn :
                    done17 = True
                    scroll_offset = 0
                elif button17_1.check_click(mouse_pos) and done17:
                    done17_1 = True
                    scroll_offset = 0
                elif button17_2.check_click(mouse_pos) and done17 :
                    done17_2 = True
                    scroll_offset = 0
                elif button17_3.check_click(mouse_pos) and done17_1 :
                    done17_3 = True
                    scroll_offset = 0
                elif button17_4.check_click(mouse_pos) and done17_2 :
                    done17_4 = True
                    scroll_offset = 0
                elif button17_5.check_click(mouse_pos) and done17_3 :
                    done17_5 = True
                    scroll_offset = 0
                elif button18_1.check_click(mouse_pos) and done17_5 :
                    done18_1 = True
                    scroll_offset = 0
                elif button18_2.check_click(mouse_pos) and done17_5 :
                    done18_2 = True
                    scroll_offset = 0
                elif button19.check_click(mouse_pos) and done18_1 :
                    done19 = True
                    scroll_offset = 0
                elif button19_1.check_click(mouse_pos) and done19 or done18_2 :
                    done19_1 = True
                    scroll_offset = 0
                elif button19_2.check_click(mouse_pos) and done19_1 :
                    done19_2 = True
                    scroll_offset = 0
                elif button19_3.check_click(mouse_pos) and done19_2 :
                    done19_3 = True
                    scroll_offset = 0
                elif button19_4.check_click(mouse_pos) and done19_2 :
                    done19_4 = True
                    scroll_offset = 0
                elif button19_5.check_click(mouse_pos) and done19_3 :
                    done19_5 = True
                    scroll_offset = 0
                elif button19_6.check_click(mouse_pos) and done19_4 :
                    done19_6 = True
                    scroll_offset = 0
                elif button19_7.check_click(mouse_pos) and done19_5 or done19_6:
                    done19_7 = True
                    scroll_offset = 0
                elif button19_8.check_click(mouse_pos) and done19_7:
                    done19_8 = True
                    scroll_offset = 0
                elif button19_9.check_click(mouse_pos) and done19_8:
                    done19_9 = True
                    scroll_offset = 0
                elif button20.check_click(mouse_pos) and done19_9:
                    done20 = True
                    scroll_offset = 0
                elif button20_1.check_click(mouse_pos) and done20:
                    done20_1 = True
                    scroll_offset = 0
                elif button20_2.check_click(mouse_pos) and done20:
                    done20_2 = True
                    scroll_offset = 0
                elif button20_3.check_click(mouse_pos) and done20_1:
                    done20_3 = True
                    scroll_offset = 0
                elif button20_4.check_click(mouse_pos) and done20_2:
                    done20_4 = True
                    scroll_offset = 0
                elif button20_5.check_click(mouse_pos) and done20_4 or done20_3:
                    done20_5 = True
                    scroll_offset = 0
                elif button20_6.check_click(mouse_pos) and done20_5:
                    done20_6 = True
                    scroll_offset = 0
                elif button20_7.check_click(mouse_pos) and done20_6:
                    done20_7 = True
                    scroll_offset = 0
                elif button20_8.check_click(mouse_pos) and done20_7:
                    done20_8 = True
                    scroll_offset = 0
                elif button20_9.check_click(mouse_pos) and done20_8:
                    done20_9 = True
                    scroll_offset = 0
                elif button21.check_click(mouse_pos) and done20_9:
                    done21 = True
                    scroll_offset = 0
                elif button21_1.check_click(mouse_pos) and done21:
                    done21_1 = True
                    scroll_offset = 0
                elif button21_2.check_click(mouse_pos) and done21_1:
                    done21_2 = True
                    scroll_offset = 0
                elif button21_3.check_click(mouse_pos) and done21_2:
                    done21_3 = True
                    scroll_offset = 0
                elif button21_4.check_click(mouse_pos) and done21_2:
                    done21_4 = True
                    scroll_offset = 0
                elif Beth.check_click(mouse_pos):
                    Beth.clicked = False  # Reset the clicked flag
                    Beth.visible = True  # Make the button visible again
                elif Script.check_click(mouse_pos):
                    Script.clicked = False  # Reset the clicked flag
                    Script.visible = True  # Make the button visible again
                elif Royal.check_click(mouse_pos):
                    Royal.clicked = False  # Reset the clicked flag
                    Royal.visible = True  # Make the button visible again
                elif button22_1.check_click(mouse_pos) and done21_4 :
                    done22_1 = True
                    scroll_offset = 0
                elif button24.check_click(mouse_pos) and done21_3:
                    done24 = True
                    scroll_offset = 0
                elif button23.check_click(mouse_pos) and done24:
                    done23 = True
                    scroll_offset = 0
                elif button25.check_click(mouse_pos) and done23:
                    done25 = True
                    scroll_offset = 0
                elif button26.check_click(mouse_pos) and done25:
                    done26 = True
                    scroll_offset = 0
                elif button27_1.check_click(mouse_pos) and done26:
                    done27_1 = True
                    scroll_offset = 0
                elif button27_2.check_click(mouse_pos) and done26:
                    done27_2 = True
                    scroll_offset = 0
                elif button27_3.check_click(mouse_pos) and done27_1:
                    done27_3 = True
                    scroll_offset = 0
                elif button28.check_click(mouse_pos) and done27_2:
                    done28 = True
                    scroll_offset = 0
                elif button29.check_click(mouse_pos) and done28:
                    done29 = True
                    scroll_offset = 0
                elif button30_1.check_click(mouse_pos) and done29:
                    done30_1 = True
                    scroll_offset = 0
                elif button30_2.check_click(mouse_pos) and done29:
                    done30_2 = True
                    scroll_offset = 0
                elif button31_1.check_click(mouse_pos) and done30_2:
                    done31_1 = True
                    scroll_offset = 0
                elif button31.check_click(mouse_pos) and done30_1:
                    done31 = True
                    scroll_offset = 0
                elif button32.check_click(mouse_pos) and done31:
                    done32 = True
                    scroll_offset = 0
                elif button33_1.check_click(mouse_pos) and done32:
                    done33_1 = True
                    scroll_offset = 0
                elif button33_2.check_click(mouse_pos) and done32:
                    done33_2 = True
                    scroll_offset = 0
                elif button34_1.check_click(mouse_pos) and done33_1 :
                    done34_1 = True
                    scroll_offset = 0
                elif button34_2.check_click(mouse_pos) and done33_2 or done34_1:
                    done34_2 = True
                    scroll_offset = 0
                elif button35_1.check_click(mouse_pos) and done34_2:
                    done35_1 = True
                    scroll_offset = 0
                elif button35_2.check_click(mouse_pos) and done34_2:
                    done35_2 = True
                    scroll_offset = 0
                elif button37.check_click(mouse_pos) and done35_1 or done42_1:
                    done37 = True
                    scroll_offset = 0

                elif button37_2.check_click(mouse_pos) and done42_1:
                    done37_2 = True
                    scroll_offset = 0
                elif button38.check_click(mouse_pos) and done35_2:
                    done38 = True
                    scroll_offset = 0
                elif button39_1.check_click(mouse_pos) and done38:
                    done39_1 = True
                    scroll_offset = 0
                elif button39_2.check_click(mouse_pos) and done38:
                    done39_2 = True
                    scroll_offset = 0
                elif button39_3.check_click(mouse_pos) and done39_1:
                    done39_3 = True
                    scroll_offset = 0
                elif button39_4.check_click(mouse_pos) and done39_2:
                    done39_4 = True
                    scroll_offset = 0
                elif button40_1.check_click(mouse_pos) and done39_4 or done40_2:
                    done40_1 = True
                    scroll_offset = 0
                elif button40_2.check_click(mouse_pos) and done39_4:
                    done40_2 = True
                    scroll_offset = 0
                elif button40_3.check_click(mouse_pos) and done40_1:
                    done40_3 = True
                    scroll_offset = 0
                elif button40_4.check_click(mouse_pos) and done40_2:
                    done40_4 = True
                    scroll_offset = 0
                elif button41_1.check_click(mouse_pos) and done40_3:
                    done41_1= True
                    scroll_offset = 0
                elif button41_2.check_click(mouse_pos) and done40_3:
                    done41_2= True
                    scroll_offset = 0
                elif button42.check_click(mouse_pos) and done41_1:
                    done42= True
                    scroll_offset = 0
                elif button42_1.check_click(mouse_pos) and done41_2:
                    done42_1= True
                    scroll_offset = 0
                elif button42_2.check_click(mouse_pos) and done41_2:
                    done42_2= True
                    scroll_offset = 0
                elif button44.check_click(mouse_pos) and done42_2:
                    done44 = True
                    scroll_offset = 0
                elif button45.check_click(mouse_pos) and done44:
                    done45 = True
                    scroll_offset = 0
                elif button46.check_click(mouse_pos) and done45:
                    done46 = True
                    scroll_offset = 0
                elif button49.check_click(mouse_pos) :
                    done49 = True
                    scroll_offset = 0
                elif button37_3.check_click(mouse_pos) and dn1:
                    done37_3 = True
                    scroll_offset = 0


        button16_5.check_hover(mouse_pos)
        button17.check_hover(mouse_pos)
        button17_1.check_hover(mouse_pos)
        button17_2.check_hover(mouse_pos)
        button17_3.check_hover(mouse_pos)
        button17_4.check_hover(mouse_pos)
        button17_5.check_hover(mouse_pos)
        button18_1.check_hover(mouse_pos)
        button18_2.check_hover(mouse_pos)
        button19.check_hover(mouse_pos)
        button19_1.check_hover(mouse_pos)
        button19_2.check_hover(mouse_pos)
        button19_3.check_hover(mouse_pos)
        button19_4.check_hover(mouse_pos)
        button19_5.check_hover(mouse_pos)
        button19_6.check_hover(mouse_pos)
        button19_7.check_hover(mouse_pos)
        button19_8.check_hover(mouse_pos)
        button19_9.check_hover(mouse_pos)
        button20.check_hover(mouse_pos)
        button20_1.check_hover(mouse_pos)
        button20_2.check_hover(mouse_pos)
        button20_3.check_hover(mouse_pos)
        button20_4.check_hover(mouse_pos)
        button20_5.check_hover(mouse_pos)
        button20_6.check_hover(mouse_pos)
        button20_7.check_hover(mouse_pos)
        button20_8.check_hover(mouse_pos)
        button20_9.check_hover(mouse_pos)
        button21.check_hover(mouse_pos)
        button21_1.check_hover(mouse_pos)
        button21_2.check_hover(mouse_pos)
        button21_3.check_hover(mouse_pos)
        button21_4.check_hover(mouse_pos)
        Beth.check_hover(mouse_pos)
        Script.check_hover(mouse_pos)
        Royal.check_hover(mouse_pos)
        button22_1.check_hover(mouse_pos)
        button23.check_hover(mouse_pos)
        button24.check_hover(mouse_pos)
        button25.check_hover(mouse_pos)
        button26.check_hover(mouse_pos)
        button27_1.check_hover(mouse_pos)
        button27_2.check_hover(mouse_pos)
        button27_3.check_hover(mouse_pos)
        button28.check_hover(mouse_pos)
        button29.check_hover(mouse_pos)
        button30_1.check_hover(mouse_pos)
        button30_2.check_hover(mouse_pos)
        button31_1.check_hover(mouse_pos)
        button31.check_hover(mouse_pos)
        button32.check_hover(mouse_pos)
        button33_2.check_hover(mouse_pos)
        button33_1.check_hover(mouse_pos)
        button34_2.check_hover(mouse_pos)
        button34_1.check_hover(mouse_pos)
        button35_2.check_hover(mouse_pos)
        button35_1.check_hover(mouse_pos)
        button37.check_hover(mouse_pos)
        button37_1.check_hover(mouse_pos)
        button37_3.check_hover(mouse_pos)
        button38.check_hover(mouse_pos)
        button39_1.check_hover(mouse_pos)
        button39_2.check_hover(mouse_pos)
        button39_3.check_hover(mouse_pos)
        button39_4.check_hover(mouse_pos)
        button40_1.check_hover(mouse_pos)
        button40_2.check_hover(mouse_pos)
        button40_3.check_hover(mouse_pos)
        button40_4.check_hover(mouse_pos)
        button41_1.check_hover(mouse_pos)
        button41_2.check_hover(mouse_pos)
        button42.check_hover(mouse_pos)
        button42_1.check_hover(mouse_pos)
        button42_2.check_hover(mouse_pos)
        button44.check_hover(mouse_pos)
        button45.check_hover(mouse_pos)
        button46.check_hover(mouse_pos)
        button49.check_hover(mouse_pos)

        if done16_4:

            draw_text_box(screen, (90, 60), (1060, 700), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "The Riddle:", (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 120, HEIGHT - 575, WIDTH - 995, HEIGHT - 575, 1, (255, 255, 255), scroll_offset,
                      line_visible)
            display_text(screen, text16_5, (350, 165), font0, (255, 255, 255), scroll_offset)
            display_text(screen, text16_6, (120, 430), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 150, WIDTH - 130, HEIGHT - 150, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            display_text(screen, "Type your answer", (160, 650), font0, (255, 255, 255), scroll_offset)
            button16_5.draw(screen, scroll_offset)
            Wisdom.update_cursor(dt)
            Wisdom.draw(screen, scroll_offset)

        if done16_5:
            import typingRacer
            typingRacer.typing_racer_game()
        if dn:
            done16_4 = False
            draw_text_box(screen, (90, 60), (1060, 590), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 190, WIDTH - 130, HEIGHT - 190, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button17.draw(screen, scroll_offset)
        if dn1:
            scroll_offset = 0
            screen.fill((0, 0, 0))
            display_text(screen, "GAME OVER", (410, 200), font3, (255, 0, 0), scroll_offset)
            button37_3.draw(screen, scroll_offset)
        if done37_3:
            import my_game
            my_game.main_menu()

        if done17:
            dn = False
            done15_4 = False
            draw_text_box(screen, (90, 60), (1060, 640), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17_1, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 160, WIDTH - 130, HEIGHT - 160, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button17_1.draw(screen, scroll_offset)
            button17_2.draw(screen, scroll_offset)
        if done17_1:
            done17 = False
            dn = False
            done15_4 = False
            draw_text_box(screen, (90, 90), (1060, 570), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17_1_1, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 160, WIDTH - 130, HEIGHT - 160, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button17_3.draw(screen, scroll_offset)
        if done17_3:
            done17_1 = False
            done17 = False
            dn = False
            done15_4 = False
            draw_text_box(screen, (90, 120), (1060, 500), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17_3, (120, 150), font, (255, 255, 255), scroll_offset)
            display_text(screen, "To know more about The old lady Press on Beth", (140, 450), font0, (205, 210, 155),
                         scroll_offset)
            draw_line(screen, 130, HEIGHT - 190, WIDTH - 130, HEIGHT - 190, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button17_5.draw(screen, scroll_offset)
            Beth.draw(screen, scroll_offset)

        if done17_2:
            done17 = False
            dn = False
            draw_text_box(screen, (90, 90), (1060, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17_2, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 260, WIDTH - 130, HEIGHT - 260, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button17_4.draw(screen, scroll_offset)
        if done17_4:
            done17_2 = False
            done17_3 = True
            dn = False

        if done17_5:
            done17_3 = False
            dn = False
            draw_text_box(screen, (90, 120), (1060, 410), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text17_5, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 350, WIDTH - 130, HEIGHT - 350, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button18_1.draw(screen, scroll_offset)
            button18_2.draw(screen, scroll_offset)
        if done18_1:
            done17_5 = False
            done17_3 = False

            draw_text_box(screen, (90, 150), (1060, 350), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text18_1, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 320, WIDTH - 130, HEIGHT - 320, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19.draw(screen, scroll_offset)

        if done18_2:
            done17_5 = False
            done17_3 = False
            done19 = True

        if done19:
            done18_1 = False
            done17_3 = False


            draw_text_box(screen, (90, 60), (1060, 1000), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text18_2, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 250, WIDTH - 130, HEIGHT + 250, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_1.draw(screen, scroll_offset)
        if done19_1:
            done19 = False
            done18_2 = False
            done17_3 = False

            draw_text_box(screen, (90, 190), (1060, 320), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19, (120, 220), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_2.draw(screen, scroll_offset)
        if done19_2:
            done19_1 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 1650), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_1, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 850, WIDTH - 130, HEIGHT + 850, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_3.draw(screen, scroll_offset)
            button19_4.draw(screen, scroll_offset)
        if done19_3:
            done18_2 = False
            done17_3 = False
            done19_1 = False
            done19 = False
            done19_2 = False
            draw_text_box(screen, (90, 120), (1060, 410), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_2, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_5.draw(screen, scroll_offset)

        if done19_4:
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            draw_text_box(screen, (90, 60), (1060, 570), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_3, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 170, WIDTH - 130, HEIGHT - 170, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_6.draw(screen, scroll_offset)

        if done19_5 or done19_6:
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False
            draw_text_box(screen, (90, 60), (1060, 680), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_4, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 60, WIDTH - 130, HEIGHT - 60, 1, (109, 69, 38), scroll_offset, line_visible)
            button19_7.draw(screen, scroll_offset)
        if done19_7:
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_5 = False
            done19_6 = False
            draw_text_box(screen, (90, 90), (1060, 530), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_5, (120, 120), font, (255, 255, 255), scroll_offset)
            display_text(screen, "Press read to keep reading the story ", (150, 440), font0, (255, 255, 255),
                         scroll_offset)
            draw_line(screen, 130, HEIGHT - 190, WIDTH - 130, HEIGHT - 190, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_8.draw(screen, scroll_offset)
        if done19_8:
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_7 = False
            draw_text_box(screen, (90, 90), (1060, 480), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text19_6, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 250, WIDTH - 130, HEIGHT - 250, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button19_9.draw(screen, scroll_offset)
        if done19_9:
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_8 = False
            draw_text_box(screen, (90, 90), (1060, 480), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 250, WIDTH - 130, HEIGHT - 250, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button20.draw(screen, scroll_offset)
        if done20:
            done19_9 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 900), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_1, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 110, WIDTH - 130, HEIGHT + 110, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button20_1.draw(screen, scroll_offset)
            button20_2.draw(screen, scroll_offset)
        if done20_1:
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 180), (1060, 260), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_2, (120, 220), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 390, WIDTH - 130, HEIGHT - 390, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button20_3.draw(screen, scroll_offset)
        if done20_3:
            done20_1 = False
            done20_2 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 90), (1060, 600), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_5, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 90, WIDTH - 130, HEIGHT - 90, 1, (109, 69, 38), scroll_offset, line_visible)
            button20_5.draw(screen, scroll_offset)

        if done20_2:
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 90), (1060, 750), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_3, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 40, WIDTH - 130, HEIGHT + 40, 1, (109, 69, 38), scroll_offset, line_visible)
            button20_4.draw(screen, scroll_offset)
        if done20_4:
            done20_2 = False
            done20_3 = True
            done17_3 = False
        if done20_5:
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 850), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_6, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 100, WIDTH - 130, HEIGHT + 100, 1, (109, 69, 38), scroll_offset, line_visible)
            button20_6.draw(screen, scroll_offset)
        if done20_6:
            done20_5 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 90), (1060, 650), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_7, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 90, WIDTH - 130, HEIGHT - 90, 1, (109, 69, 38), scroll_offset, line_visible)
            button20_7.draw(screen, scroll_offset)
        if done20_7:
            done20_6 = False
            done20_5 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 1120), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_8, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 350, WIDTH - 130, HEIGHT + 350, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button20_8.draw(screen, scroll_offset)
        if done20_8:
            done20_7 = False
            done20_6 = False
            done20_5 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 860), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text20_9, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 95, WIDTH - 130, HEIGHT + 95, 1, (109, 69, 38), scroll_offset, line_visible)
            button20_9.draw(screen, scroll_offset)
        if done20_9:
            done20_8 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 1000), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "FEW WEEKS LATER..", (330, 90), font2, (168, 127, 71), scroll_offset)
            display_text(screen, text21, (120, 200), font, (255, 255, 255), scroll_offset)
            display_text(screen, "Press  royal ceremony to know more about the royal ceremony", (160, 910), font0, (205, 210, 155), scroll_offset)
            draw_line(screen, 130, HEIGHT + 260, WIDTH - 130, HEIGHT + 260, 1, (109, 69, 38), scroll_offset, line_visible)
            button21.draw(screen, scroll_offset)
            Royal.draw(screen, scroll_offset)
        if done21:
            done20_9 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 1180), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text21_1, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 420, WIDTH - 130, HEIGHT + 420, 1, (109, 69, 38), scroll_offset, line_visible)
            button21_1.draw(screen, scroll_offset)
        if done21_1:
            done21 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            draw_text_box(screen, (90, 60), (1060, 1060), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text21_2, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 300, WIDTH - 130, HEIGHT + 300, 1, (109, 69, 38), scroll_offset,  line_visible)
            button21_2.draw(screen, scroll_offset)
        if done21_2:
            done21_1 = False
            done20_3 = False
            done20 = False
            done18_2 = False
            done17_3 = False
            done19 = False

            done20_5 = False

            draw_text_box(screen, (90, 60), (1060, 960), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text21_3, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 170, WIDTH - 130, HEIGHT + 170, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button21_3.draw(screen, scroll_offset)
            button21_4.draw(screen, scroll_offset)
        if done21_3:
            done21_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 450), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text22_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 250, WIDTH - 130, HEIGHT - 250, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button24.draw(screen, scroll_offset)

        if done21_4:
            done21_2 = False
            done20_3 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False

            draw_text_box(screen, (90, 180), (1060, 250), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text22_2, (120, 230), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 380, WIDTH - 130, HEIGHT - 380, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button22_1.draw(screen, scroll_offset)
        if done22_1:
            done21_4 = False
            done21_3 = True
            done21_2 = False
            done20_3 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False
        if done24:
            done21_3 = False
            done21_2 = False
            done20_3 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False

            draw_text_box(screen, (90, 60), (1060, 1380), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text23, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 630, WIDTH - 130, HEIGHT + 630, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button23.draw(screen, scroll_offset)
        if done23:
            done24 = False
            done21_3 = False
            done21_2 = False
            done20_3 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False
            draw_text_box(screen, (90, 60), (1060, 800), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text24, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 50, WIDTH - 130, HEIGHT + 50, 1, (109, 69, 38), scroll_offset, line_visible)
            button25.draw(screen, scroll_offset)
        if done25:
            done23 = False
            done24 = False
            done21_3 = False
            done21_2 = False
            done20_3 = False
            done18_2 = False
            done17_3 = False
            done19 = False
            done19_1 = False
            done19_2 = False
            done19_4 = False
            done19_3 = False
            done20_5 = False
            done20_7 = False
            draw_text_box(screen, (90, 60), (1060, 1350), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text25, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 590, WIDTH - 130, HEIGHT + 590, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button26.draw(screen, scroll_offset)
        if done26:
            done23 = False
            done24 = False
            done21_3 = False
            done25 = False
            done20_3 = False
            done17_3 = False

            draw_text_box(screen, (90, 90), (1060, 510), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text26, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button27_1.draw(screen, scroll_offset)
            button27_2.draw(screen, scroll_offset)

        if done27_1:
            done21_3 = False
            done26 = False
            done17_3 = False
            done20_3 = False
            draw_text_box(screen, (90, 200), (1060, 270), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "Wrong try again", (150, 240), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 370, WIDTH - 130, HEIGHT - 370, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button27_3.draw(screen, scroll_offset)

        if done27_3:
            done27_2 = True
            done27_1 = False
            done17_3 = False
            done20_3 = False

        if done27_2:
            done21_3 = False
            done26 = False
            done17_3 = False
            done20_5 = False
            done20_3 = False
            draw_text_box(screen, (90, 90), (1060, 600), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text28, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 140, WIDTH - 130, HEIGHT - 140, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button28.draw(screen, scroll_offset)
        if done28:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done17_3 = False
            done20_5 = False
            done20_3 = False
            draw_text_box(screen, (90, 90), (1060, 460), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text29, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 280, WIDTH - 130, HEIGHT - 280, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button29.draw(screen, scroll_offset)
        if done29:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done28 = False
            done17_3 = False
            done20_3 = False
            draw_text_box(screen, (90, 60), (1060, 1100), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text30, (120, 90), font, (255, 255, 255), scroll_offset)
            display_text(screen, text30_1, (120, 320), font, (255, 255, 255), scroll_offset)
            display_text(screen, "the veroccusom extract and the shivereana extract ", (255, 326), font0,
                         (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 280, WIDTH - 130, HEIGHT + 280, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button30_1.draw(screen, scroll_offset)
            button30_2.draw(screen, scroll_offset)
        if done30_1:
            done21_3 = False
            done20_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done17_3 = False
            draw_text_box(screen, (90, 200), (1060, 240), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "Great idea! It’ll keep you close to thalos.", (120, 250), font, (255, 255, 255),
                         scroll_offset)
            draw_line(screen, 130, HEIGHT - 380, WIDTH - 130, HEIGHT - 380, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button31.draw(screen, scroll_offset)
        if done30_2:
            done21_3 = False
            done20_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done17_3 = False
            draw_text_box(screen, (90, 200), (1060, 250), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, "the tree is too far away, you have to stay close to thalos ", (150, 250), font,
                         (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 380, WIDTH - 130, HEIGHT - 380, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button31_1.draw(screen, scroll_offset)

        if done31:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 770), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text32, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 40, WIDTH - 130, HEIGHT + 40, 1, (109, 69, 38), scroll_offset, line_visible)
            button32.draw(screen, scroll_offset)

        if done32:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 690), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text33, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 110, WIDTH - 130, HEIGHT - 110, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button33_1.draw(screen, scroll_offset)
            button33_2.draw(screen, scroll_offset)

        elif done31_1:
            done30_2 = False
            done31 = True
            done20_3 = False
            done17_3 = False
        if done33_1:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 350), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text33_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 350, WIDTH - 130, HEIGHT - 350, 1, (109, 69, 38), scroll_offset,  line_visible)
            button34_1.draw(screen, scroll_offset)

        if done34_1:
            done33_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 690), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text33, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 110, WIDTH - 130, HEIGHT - 110, 1, (109, 69, 38), scroll_offset,  line_visible)
            button33_2.draw(screen, scroll_offset)
        if done33_2:
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 90), (1060, 550), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text33_2, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 170, WIDTH - 130, HEIGHT - 170, 1, (109, 69, 38), scroll_offset, line_visible)
            button34_2.draw(screen, scroll_offset)
        if done34_2:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 490), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text34, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 290, WIDTH - 130, HEIGHT - 290, 1, (109, 69, 38), scroll_offset,  line_visible)
            button35_1.draw(screen, scroll_offset)
            button35_2.draw(screen, scroll_offset)
        if done35_1:
            screen.fill((0, 0, 0))
            display_text(screen, "GAME OVER", (430, 50), font3, (255, 0, 0), scroll_offset)
            display_text(screen, text36, (160, 180), font, (255, 255, 255), scroll_offset)
            button37.draw(screen, scroll_offset)

        if done37:
            import my_game
            my_game.main_menu()

        if done35_2:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 90), (1060, 530), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text38, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 220, WIDTH - 130, HEIGHT - 220, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button38.draw(screen, scroll_offset)
        if done38:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 910), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text39, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 110, WIDTH - 130, HEIGHT + 110, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button39_1.draw(screen, scroll_offset)
            button39_2.draw(screen, scroll_offset)
        if done39_1:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 380), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text39_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 340, WIDTH - 130, HEIGHT - 340, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button39_3.draw(screen, scroll_offset)

        if done39_2:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 90), (1060, 505), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text39_2, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 230, WIDTH - 130, HEIGHT - 230, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button39_4.draw(screen, scroll_offset)

        if done39_4:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 1230), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text40, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 430, WIDTH - 130, HEIGHT + 430, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button40_1.draw(screen, scroll_offset)
            button40_2.draw(screen, scroll_offset)

        elif done39_3:
            done39_1 = False
            done39_2 = True
            done20_3 = False
            done17_3 = False

        if done40_1:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done39_4 = False
            done40_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 300), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text40_1, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 380, WIDTH - 130, HEIGHT - 380, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button40_3.draw(screen, scroll_offset)

        if done40_2:
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done39_4 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 300), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text40_2, (120, 180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 430, WIDTH - 130, HEIGHT - 430, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button40_4.draw(screen, scroll_offset)
        if done40_4:
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 1230), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text40, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 430, WIDTH - 130, HEIGHT + 430, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button40_1.draw(screen, scroll_offset)
        if done40_3:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 760), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text41, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 20, WIDTH - 130, HEIGHT - 20, 1, (109, 69, 38), scroll_offset, line_visible)
            button41_1.draw(screen, scroll_offset)
            button41_2.draw(screen, scroll_offset)
        if done41_1:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 90), (1060, 460), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text42, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 230, WIDTH - 130, HEIGHT - 230, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button42.draw(screen, scroll_offset)
        if done42:
            done41_1 = False
            done41_2 = True
            done20_3 = False
            done17_3 = False
        if done41_2:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 1420), (0, 0, 0), (109, 69, 38), 200, scroll_offset)
            display_text(screen, "The king says to him: ", (120, 90), font, (255, 255, 255), scroll_offset)
            display_text(screen, text43, (140, 150), font0_0, (128, 0, 0), scroll_offset)
            display_text(screen, "Shocked, you could not move. The king added that he would do the same to Thalos and all the remaining humans. ",(120, 1180), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 580, WIDTH - 130, HEIGHT + 580, 1, (109, 69, 38), scroll_offset, line_visible)
            button42_1.draw(screen, scroll_offset)
            button42_2.draw(screen, scroll_offset)
        if done42_1:
            screen.fill((0, 0, 0))
            display_text(screen, "GAME OVER", (420, 180), font3, (255, 0, 0), scroll_offset)
            display_text(screen, "You give up, we thought you were stronger than that aiden.. game overwhelms", (240, 350), font, (255, 255, 255), scroll_offset)
            button37_2.draw(screen, scroll_offset)

        if done37_2:
            import my_game
            my_game.main_menu()
        if done42_2:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done41_2 = False
            done42 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 120), (1060, 400), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text44, (120, 150), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 315, WIDTH - 130, HEIGHT - 315, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button44.draw(screen, scroll_offset)
        if done44:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done41_2 = False
            done42_2 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 90), (1060, 560), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text45, (120, 120), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT - 180, WIDTH - 130, HEIGHT - 180, 1, (109, 69, 38), scroll_offset, line_visible)
            button45.draw(screen, scroll_offset)
        if done45:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done41_2 = False
            done42_2 = False
            done44 = False
            done20_3 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 970), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text46, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 200, WIDTH - 130, HEIGHT + 200, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button46.draw(screen, scroll_offset)
        if done46:
            done40_1 = False
            done40_2 = False
            done34_1 = False
            done21_3 = False
            done27_2 = False
            done27_3 = False
            done29 = False
            done30_1 = False
            done31 = False
            done32 = False
            done33_2 = False
            done34_2 = False
            done35_2 = False
            done38 = False
            done39_2 = False
            done40_3 = False
            done41_2 = False
            done42_2 = False
            done44 = False
            done45 = False
            done17_3 = False
            draw_text_box(screen, (90, 60), (1060, 860), (50, 50, 50), (109, 69, 38), 130, scroll_offset)
            display_text(screen, text47, (120, 90), font, (255, 255, 255), scroll_offset)
            draw_line(screen, 130, HEIGHT + 120, WIDTH - 130, HEIGHT + 120, 1, (109, 69, 38), scroll_offset,
                      line_visible)
            button49.draw(screen, scroll_offset)
        if done49:
            CharactersDetails.EndScreen()


        # Draw the cursor
        cursor_img = pygame.image.load('Sans titre.png')
        cursor_img = pygame.transform.scale(cursor_img, (40, 40))  # Resize cursor image
        cursor_pos = pygame.mouse.get_pos()
        screen.blit(cursor_img, cursor_pos)

        pygame.display.update()
        pygame.display.flip()

        # Scrolling functionality
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Check if scrolling up goes beyond the beginning of the text
            if scroll_offset + scroll_speed <= 0:
                scroll_offset += scroll_speed
        if keys[pygame.K_DOWN]:
            scroll_offset -= scroll_speed



