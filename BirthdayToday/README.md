# Birthday Today

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
For Windows Steam Stardew Valley players. Checks whether the in-game day is an NPC's birthday. If NPC birthday, an icon will appear in the GUI. The NPC's name will appear on hover. The NPC's gift tastes will also be logged in the SMAPI console.

Icon displayed in GUI on an NPC's birthday:
![Billboard100web](birthdaytoday.jpg)

NPC gift tastes logged in the console:
![Billboard100Spotify](smapi.PNG)

	
## Technologies
Project is created with:
* C#: 10
* .NET 6 framework
* SMAPI Mod Loader
	
## Setup
To run this mod, the BirthdayToday folder must be added to the Mods folder inside the Stardew Valley game folder.

Install SMAPI (instuctions from the [SDV Wiki](https://stardewvalleywiki.com/Modding:Installing_SMAPI_on_Windows)) :
1. Run the game without SMAPI at least once (so it can do first-time setup).
2. Download the latest version of [SMAPI](https://smapi.io/).
3. Extract the .zip file somewhere. (Your downloads folder is fine.)
4. Double-click install on Windows.bat, and follow the on-screen instructions.
5. Configure your game client: [Steam](https://stardewvalleywiki.com/Modding:Installing_SMAPI_on_Windows#Steam).

Once SMAPI is installed and the BirthdayToday folder is in the Mods folder, run the Stardew Valley game on Steam. SMAPI will automatically load the BirthdayToday mod.