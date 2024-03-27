from email.policy import default
import random

class MusicLibrary:
    def __init__(self):
        self.song=[]
        
    def addSong(self, song):
        self.song.append(song)
        print(f"{song} added to Music Library")
    
    def removeSong(self, song):
        if song in self.song:
            self.song.remove(song)
            print(f"{song} Removed Successfully")
        else:
            print(f"{song} Not found .... in Library")
    
    
    def playRandomSong(self):
        if self.song:
            random_song = random.choice(self.song)
            print(f"Now playing: ' {random_song} ' ")
        else:
            print("No Song in the Music Library")
    
    

library = MusicLibrary()
library.addSong("Tera Fittor")
library.addSong("Without Me")


while True:
    print("Select the Operation You want to Perform : ")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. Play Random Song")
    ch = int(input("Enter Your Choice : "))
    
    match ch:
        case 1:
            song = input("Enter the name of Song, You want to add : ")
            library.addSong(song)
        case 2:
            song = input("Enter the name of Song, You want to remove : ")
            library.removeSong(song)
        case 3:
            library.playRandomSong()
        case _:
            print("Invalid Input ......")
            
    print("")
    print("--------------------------------------------")
    print("")
    
    choice = input("Would You like to exit (y) : ")
    if(choice in ['y', 'Y']):
        break
    
    