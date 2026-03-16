# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looked simple. It used up very little space on the screen. The develope debug info was very helpful to guess what the number was.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The new game button was not working.
Everytime i guess a number it always said "lower"
You cannot press enter to "press enter to apply"

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Gemini, Chatgpt and copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One of the AI's suggestions was fixing the attempts you get for each mode. It never occured to me that the modes have different attempts. I had spoted bugs before AI pointed out the ones i did not notice.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

AI did not give me any misleading suggestions. However it did give me tests which i did not want, The tests are helpful to prove the application works, but it was never asked to produce any.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Since this is a small application I would manually test the bug I had spoted to make sure it was successufully debuged.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I did manual boundary tests by entering decimal values into the input field. Originally the code would crash, but after using ai to refactor parse_guess, the function will convert the number into an integer.

- Did AI help you design or understand any tests? How?

yes, AI helped me understand different types of tests, and also how to structure them. It also let me know that good tests should run without needing to run the web interface.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The number kept being generated because the app would rerun whenever a user interacts with the widget.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Steamlit reruns are like restarting a movie. 
Session state is like using a notebook that keeps track of details, as long as you dont rerun the application it will not forget the details.

- What change did you make that finally gave the game a stable secret number?
I wrapped the number generation in an if statement. The application will only generate a new number at the start of a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

I will use different AI models, since they give different ideas of how to fix things. Copilot would just give the fix, Gemini would give the fix and explanation, and chatgpt would give an explanation but it was difficult to understand.

- This could be a testing habit, a prompting strategy, or a way you used Git.
I will use more targeted prompts instead of just giving AI the whole file. I can prevent it from try to to fix what is not an error.

- What is one thing you would do differently next time you work with AI on a coding task?
I could use AI to generate boilerplate, but it starts to hallucinate whenever projects get large, I would need to inspect it code first.

- In one or two sentences, describe how this project changed the
way you think about AI generated code.
I used to think AI code was slop, and I still do to an extent. However, it is really useful as long as you keep the prompts short and precise. If i feed it lots of info it seems to get caught up in its own "fixes".