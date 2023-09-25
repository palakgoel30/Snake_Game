# Snake_Game

<u><h3>About </h3></u>

This Game has a snake and an apple.
When snake touches the boundary of a screen or itself,the game will over.

Then game over screen shows the score and also ask you, if you want to exit or continue.

<u><h4> How to convert py to exe file</u></h4>
Step1 :- open cmd, install pyinstaller using following command.
        pip install pyinstaller

Step2 :- from file location open cmd,then write following command.
         pyinstaller --onefile -w 'Snake_Apple_Game.py'

Step3 :- go and check the directory, where the source is present. It should contain the
build folder, spec file and dist folder.

Step4 :- build folder and spec file both have no use, you can delete them.

Step 5 :- open the dist folder, this folder will contain an exe file.
if exe file shows that's your resource files are not present, then add all your resource files to dist folder.

Step6 :- zip the dist folder.

Step7:- using NSIS application,make exe file.
That's your final game application.

    ***********************************************************************
For colour Reference:-

RGB(256,256,256) : White
RGB(0,0,0): Black
