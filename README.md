# Hangman

The word to guess is represented by a row of dashes representing each letter of the word. Rules may permit or forbid proper nouns, such as names, places, brands, or slang. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions. If the suggested letter does not occur in the word, the other player draws one element of a hanged stick figure as a tally mark.

The player guessing the word may, at any time, attempt to guess the whole word.[citation needed] If the word is correct, the game is over and the guesser wins. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. On the other hand, if the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed.



<img src="images/responsive.png" alt="image of app on different sized screens">

[Click here to go to the live website!](https://hangman19951014.herokuapp.com/) 

## Table of contents 

1. [Plans and structure](#plans-and-structure)
    - [Objectives](#objectives)
    - [Changes throughout the process](#changes-throughout-the-process)
2. [Features](#features)
    - [Welcome page](#welcome-page)
    - [Instructions](#instructions)
    - [Game](#game)
    - [Winning message](#winning-message) 
    - [Extra features](#extra-features)
3. [Testing](#testing)
    - [Python](#python)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
4. [Deployment](#deployment)
5. [Finished product](#finished-product)
6. [Credits](#credits)
    
## Plans and structure 

<img src="images/flow.png" alt="Screenshot of the hangman flow chart">  

### Objectives

- I want to create a game with clues and without clues. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - This was achieved by using a simple 1 for yes or 2 for no for each time the user needs to make a choice. 
                        
 - I want to create a special symbol that helps user to get a hint. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - If user type "*" symbol the list of array of words showed up, dependends how many letters are correct.

- To make it clear to the user how many tries they have left until the game is over.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong the number of tries left is printed and each round if they get the answer right or wrong it will print out the traditional hangman image that shows how many tries the user has left in the game.

- I want to give the user couple of warnings.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user type some symbol or number, he get a warning that explains a mistake.Also user can`t type two letters. 

### Changes throughout the process

Throughout the process of making this project I decided to change a couple of things to improve the game. 

- Originally, I had 2 different part of code for hints and without hints game.
- Also i decided to create an image of hangman.

For the first section I added another function and added an option at the end of the file to choose which game you want to play. Also I created an image of hangman, that`s took me a lot of effort and time, but hopely i done it.

<img src="images/hangman.png" alt="Screenshot of hangman">

Go back to [Table of contents](#table-of-contents) 



## Features 

### Instructions 
- The fist message is showing how much words we use in this game.There is an option to play with hints or without hints.

<img src="images/welcome.png" alt="Screenshot of instructions page">

### Game
- When the user starts the game, it shows the user the length of the word they are guessing and asks the user to enter a letter.There is also displayed how many warnings user have.

<img src="images/game.png" alt="Screenshot of game page">

- While the user is playing the game page also shows other things such as error if letter incorrect and showing that user have less guesses.

<img src="images/mistake.png" alt="Screenshot of game page whilst being played">

### Winning message
- If the user guesses all letter correctly it will take them to a page that congradulates user and shows your total score.

<img src="images/won.png" alt="Screenshot of the end of the game if the player has won">

### Extra features
- I decided to create an image of hangman to make it more nicely for the user to play this game.

1. The hangman image will change throughout the game, every time the user guesses a letter wrong, the image adds a section.

<img src="images/fail.png" alt="Screenshot of hangman image">

2. The user get a warning when input an intager.

<img src="images/symbol.png" alt="Screenshot of the question what level would the user like to play">

Go back to [Table of contents](#table-of-contents)

## Testing

### Python
The website pep8online.com is currently down.So I decided to add a PEP8 validator to my Gitpod Workspace directly.
Runned the command pip3 install pycodestyle.
PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

The Python results came back with the following:

1.run.py

<img src="images/error.png" alt="run.py errors">

2.show_hangman.py

<img src="images/error1.png" alt="show_hangman.py results">


- To fix this show_hangman.py file errors I edited my docstring like that:

    <img src="images/fixed_run.png" alt="Screenshot of a line before"> 


- To fix this run.py file errors I edited my docstring like that:
    
    <img src="images/run1.png" alt="pep8 after"> 
    <img src="images/run2.png" alt="pep8 after"> 
    <img src="images/run3.png" alt="pep8 after"> 


### Manual Testing 

1. Would the user like to see the instructions?
 the user is asked to input either 1 for yes or 2 for no. 

 - First, I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.

 <img src="images/see-inst-invalid.png" alt="Screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Shows instructions, results were as expected.

 <img src="images/see-inst-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: Game starts, results were as expected.

 <img src="images/see-inst-2.png" alt="image of what happens when user types 2"> 

2. After reading the instructions the user is asked if they are ready to play, 1 for yes and 2 for no.

 - First, I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.
 
 <img src="images/ready-invalid.png" alt="screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Game starts, results were as expected.

 <img src="images/ready-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: User us sent back to welcome page, results were as expected.

 <img src="images/ready-2.png" alt="image of what happens when user types 2"> 

3. Once game has started the user is asked to enter a letter.

 - First, I tested what would happen if the user typed anything other a letter: Error message shows, results were as expected.
 
 <img src="images/game-invalid.png" alt="screenshot of invalid input"> 

 - Next I tested what would happen if the user typed a valid yet incorrect guess: Try again message shows and tries are appended, results were as expected.

 <img src="images/game-incorrect.png" alt="image of what happens when users guess is incorrect">

 - Then I tested what would happen if the user typed a correct guess: correct letter is put into place in the word, results were as expected.

 <img src="images/game-correct.png" alt="image of what happens when users guess is correct"> 

 - Last I tested what would happen if the user typed a letter they had already guessed: You have already guessed that letter message shows, results were as expected.
 
 <img src="images/game-repeat.png" alt="image of what happens when users guess is repeated"> 

4. At the end of the game the user is asked if they want to play again, 1 for yes 2 for no.
 
 - First, I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.

 <img src="images/again-invalid.png" alt="Screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Game starts again, results were as expected.

 <img src="images/again-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: Goodbye message shows, results were as expected.

 <img src="images/again-2.png" alt="image of what happens when user types 2"> 

### Bugs 
1. I found that when a user guesses every letter in a word, the loop isn't ending meaning that if the user still has tries left even if they have guessed every letter, it will keep asking them to enter another letter until the user runs out of tries. 

<img src="images/bug.png" alt="Screenshot of the bug">  

- fixed? Yes

- what did I do to fix it?
 
The code I originally had for this was:

    guessed = False
    while tries > 0 and len(word_letters) > 0:
        reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
        if len(users_guess) == 1 and users_guess.isalpha():
            if users_guess in guessed_letters:
            
            elif users_guess not in word:
               
            else:
                if "_" not in word:
                    guessed = True
    else:
        
I Changed it to:

    word_letters = set(word)
    while tries > 0 and len(word_letters) > 0:
        reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
        if len(users_guess) == 1 and users_guess.isalpha():
            if users_guess in guessed_letters:
            
            elif users_guess not in word:
               
            else:
                if users_guess in word_letters:
                    word_letters.remove(users_guess)
    else:
            
This means that every time a user guesses a correct letter, that letter is removed from the word_letters list and when that list is 0 the computer knows that they have guessed the whole word correctly.

Go back to [Table of contents](#table-of-contents)

## Deployment 

There were many steps to deploying this project to Heroku:

1. If I had installed any packages to Gitpod, I would need to add then to a list of requirements. 
- To do this I would have typed pip3 freeze > requirements.txt and hit enter, this would update the requirements.txt file.
- I'd need to commit and push this to Github.
- Heroku will use this list to install the dependencies into the application before the project is run.
- However, I didn't need to do this as I had no packages installed.
2. I went over to my Heroku dashboard and clicked on 'create a new app'.
3. I chose a name for my app; every app must have a unique name so I couldn't call it hangman as this was already taken so I went for hang-the-guy.
4. Selected my region and clicked create app. 
5. I then went to the tab at the top of the page and clicked on settings. 
6. Some apps will include sensitive data in the gitpod workspace that isn't in the github repository because it has been deliberately protected in the gitnore.file. I didn't have any sensitive data to protect but if I had done, I would have needed to create a config var to allow Heroku access to this data. 
 - To do this, I would have clicked reveal config vars.
 - Filled in the key for example: CREDS
 - Then copy and pasted the contents of that 'CREDS' file into the value field and clicked add. 
7. I added the buildpacks needed by clicking on the buildpack button.
 - Here I selected python and pressed save changes.
 - Then repeated the same process but selected nodejs this time.
 - making sure it was done in that order with python at the top and nodejs under.
8. I scrolled back up to the tab at the top and clicked deploy.
9. I selected github as the deployment method and clicked connect to github.
10. Once this is selected, I then searched for my github repository name, and connected to the correct repository.
11. Then I scrolled down, here there were two options.
 - The first option being to enable automatic deployment, which means that Heroku will rebuild the app every time I pushed a change to github.
 - The other option being to manually deploy, which is the choice I went for with this project.
12. When all the code is received from github there is a view button that it a link to the running app, I clicked this to make sure everything was running as expected.

Go back to [Table of contents](#table-of-contents)

## Finished product

Welcome page 
<img src="images/finished-welcome.png" alt="Screenshot of the welcome page"> 

The instructions
<img src="images/finished-inst.png" alt="Screenshot of the instructions"> 

The game
<img src="images/finished-game.png" alt="Screenshot of the game"> 

User guesses correct
<img src="images/finished-correct.png" alt="Screenshot of the user guessing correct letter"> 

User guesses incorrect
<img src="images/finished-incorrect.png" alt="Screenshot of the user guessing incorrect letter"> 

Winning message
<img src="images/finished-win.png" alt="Screenshot of the winning message"> 

Losing message
<img src="images/finished-lose.png" alt="Screenshot of the losing message"> 

End of game
<img src="images/finished-end.png" alt="Screenshot of the end of the game"> 

Go back to [Table of contents](#table-of-contents)

## Credits 

- [Lucid chart](https://www.lucidchart.com/pages/) - This was used to create the flow chart in the planning process for this project. 
- [random word generator](https://randomwordgenerator.com/) - I used this site to generate a list of random words.
- [code beautifier](https://codebeautify.org/python-formatter-beautifier) - Helped make the code look neat.
- [PEP8 validator](http://pep8online.com/) - was used to check the code was valid.
- Youtube - I watched many different youtube videos on how to make hangman using python and learnt alot from many people.
- Marcel - My mentor Marcel was extreamly helpful as always helping me feel confident in what I have made.

Go back to [Table of contents](#table-of-contents)