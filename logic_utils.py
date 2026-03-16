def get_range_for_difficulty(difficulty: str):
    """
    FIX: Corrected 'Hard' range. 
    Previously, Hard (1-50) was easier than Normal (1-100).
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500  
    return 1, 100

def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Handles empty strings and float-like strings (e.g., '10.0').
    """
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw))
        return True, value, None
    except (ValueError, TypeError):
        return False, None, "That is not a valid number."

def check_guess(guess: int, secret: int):
    """
    FIX: Corrected the hint direction.
    Previously, 'Too High' told the user to go HIGHER.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    FIX: Removed the 'participation trophy' points for wrong guesses.
    Previously, even-numbered failed attempts added 5 points.
    """
    if outcome == "Win":
        points = 100 - (10 * attempt_number)
        return current_score + max(points, 10)

    if outcome in ["Too High", "Too Low"]:
        return max(0, current_score - 5)

    return current_score
