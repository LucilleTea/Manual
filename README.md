# Manual archipelago world for Harry Potter and the Chamber of Secrets (PC) by LucilleTea.
Relies on an open world mod, originally developed by MaxG and Myelin_SR, customized for Archipelago by LucilleTea, using tools developed by Metallicafan212. Also bundling an FPS cap mod by EmilyPloszaj, because the game needs it.

This randomizer starts you right at the end of a standard HP2 game, with all levels accessible. But wait! You need to collect all of Dobby's socks, so you can free him! Such a daunting task saps all your energy, you'll have to regain your abilities along the way.
All of the game's non-repeatable adventures are modded to be accessible - usually in the location they already existed in. Willow, the starting level, is up that wall you usually drop down on the first night. The secret Gryffindor challenge is also accessible, by Percy in the Gryffindor Commonroom, and the AOL Demo level is accessible in the door that usually leads to the Bean Bonus Room. The Gold Wizard Card Challenge is available from the start in-game, though you still need the access item.

The Bean Bonus Room is not accessible :(

**Items include:**
Access to each level
Access to each spell (don't cast them if you don't know them!)
Access to jumping, and perhaps glitched boosting
Access to quidditch and duelling minigames
Gifts of beans and potions
Traps of increased difficulty
Dobby's 7 socks of course, (configurable count), all required for victory

**Other Info:**
There is an option to expect/remove most glitched progression, but even with it disabled you are sometimes expected to quidditch warp to leave levels you can no longer progress in, when the standard exits are inaccessible to you. You should have this option available to you even if you haven't unlocked any progressive quidditch items - just don't win the match in this case. Quidditch warping is a fairly simple glitch to execute: Press ESC for menu. Open the quidditch menu. Press F4 on your keyboard to instantly close all menus. Press Tab to open the map. Press ESC to back out of the map, into the Quidditch menu, where you can now select a match to start playing it, regardless of your current location.
If you do not want to quidditch warp, you should unstuck by loading the hub map with debug mode as explained below.

**Modded Game Setup:**

Please already have the original 2002 game installed on your computer, from a CD. Any language should work. I will note that these aren't for retail sale any more, so if you don't have one you'll have to get it second hand. Make a copy of your game install, so we're not modding the original (though config files will be shared).
Extract the mod zip into the copy of your game, making sure the maps and system files land in their respective folders.
The game poorly supports widescreen resolutions, and you need to click your manual client anyway, so create a shortcut to your `Game.exe` (located in the system folder), and edit the shortcut to add a `-window` flag to the end of the path. This will launch the game in a window, which you can resize as necessary.
There's probably a lot of other config that can go wrong, but that should cover the general cases. If you want to brightness boost that needs more precise setup.

You will need some custom keybinds to give yourself bean/potion gifts, and enter debug mode to change difficulty and load the hub. Technically debug mode is the only necessary bind, since the other commands could be typed into the console manually (press ~ while debug is enabled).
In your documents folder go to `Harry Potter II`, and edit User.ini. You can set these binds to any keys listed, here is example syntax:
```
F11=set hgame.HPConsole bdebugmode true | hgame.baseconsole bdebugmode true
F12=set hgame.HPConsole bdebugmode false | hgame.baseconsole bdebugmode false
```
To enable and disable debug.
```
Comma=addpotions 1
Period=addbeans 50
```
To bind gifts.
To change difficulty, have debug mode enabled and go to the input settings menu.
To load the hub map, have debug mode enabled and press F4 to open the level selector, choosing Entryhall_hub.unr.


I am honestly not sure how playable this will be for a wider audience? Feedback welcome.