# ep_rename
## Renames all episodes in a TV series folder according to name, season and episode number.

**WHAT IT DOES**
This script (with GUI) will rename all the episodes within a folder by using the folder name, which must be the name of a TV show. The name format the episodes are renamed to is

> [season no.]x[episode no.]-[name of episode]

example: 2x07-City on the Edge of Forever

**REQUIREMENTS FOR IT TO WORK**
1. If the old episode filenames consist of numbers for episode, season etc., ensure that the episode number comes AFTER the season number, and that it should be the second number in the filename.
2. The only number season folder names should contain is the season number. Any characters other than that is alright.

**Example accepted episode filename:**

s02e07 :white_check_mark:

2009-s02e07 :negative_squared_cross_mark: (since episode number is the third no. in the name)

**HOW TO USE**
1. Install Python (obvious)
2. Run the program using `python epRename.py`
3. Browse to the folder containing your TV Series folders.
4. Select the folder of the TV Series you want to rename the episodes of.
5. Hit 'Rename'

**DEV"S NOTE**

Since this version is the first, there are many requirements concerning the filenames. Sorry about that, and I'll do my best (or even you can contribute) to lower these requirements and make the script a lot smarter.
