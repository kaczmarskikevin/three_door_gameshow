# three_door_gameshow_gameshow

To execute this program

git clone https://github.com/kaczmarskikevin/three_door_gameshow.git
cd three_door_gameshow

#Windows
python3.exe ./main.py
python.exe ./main.py

#Linux
python3 ./main.py
python ./main.py

This is based on the following statistics problem

A contestant of a gameshow is presente with three doors. The contestant gets to keep whatever is behind the door he/she chooses.  Behind one door is a car. Behind the remaining doors are goats, one per.  The contestant chooses a door at random. The host then reveals a goat behind one of the doors the contestant did not choose and asks if the contestant would like to switch. 

This program proves in practice the theory of a 66% chance of success if the contestant always switches.

Scenario 1 -> Contestant chooses door 1 and doesn't switch
CGG Win
GCG Lose
GGC Lose

Scenario 2 -> Contestant chooses door 2 and doesn't switch
CGG Lose
GCG Win
GGC Lose

Scenario 3 -> Contestant chooses door 3 and doesn't switch
CGG Lose
GCG Lose
GGC Win

If we add all scenarios up we get 3 wins and 6 losses, a 33% chance of winning.

Given the same scenarios and a guaranteed switch when asked, the following is true.

Scenario 1 -> Contestant chooses door 1 and does switch
CGG Lose
GCG Win
GGC Win

Scenario 2 -> Contestant chooses door 2 and does switch
CGG Win
GCG Lose
GGC Win

Scenario 3 -> Contestant chooses door 3 and does switch
CGG Win
GCG Win
GGC Lose

Here we have 6 wins and 3 loses, a 66% chance of winning.