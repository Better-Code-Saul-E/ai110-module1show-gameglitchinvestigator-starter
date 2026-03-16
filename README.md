# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

It was to help us realize that code that looks perfect can have errors.

- [ ] Detail which bugs you found.

The game told users to go higher regardless if it was high or not
The scaling for the modes seemed to be reversed
The updatescore function game +5 points for wrong guesses on even numbered attempts

- [ ] Explain what fixes you applied.

I applied all the fixes for the bugs that i had found.
I had AI rewrite the conditional staments, fix the sesson_state management as well as handling the parsing.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![Winning screenshot](./win.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
