import random

# Pick a word at random
word_list = [""aback", "abase", "abate", "abbey", "abbot", "abhor", "abide", "abled", "abode", "abort", "about", "above", "abuse", "abyss", "acorn", "acrid", "actor", "acute", "adage", "adapt", "adept", "admin", "admit", "adobe", "adopt", "adore", "adorn", "adult", "affix", "afire", "afoot", "afoul", "after", "again", "agape", "agate", "agent", "agile", "aging", "aglow", "agony", "agree", "ahead", "aider", "aisle", "alarm", "album", "alert", "algae", "alibi", "align", "alike", "alive", "allay", "allow", "alloy", "aloft", "alone", "along", "alter", "amber", "amend", "amiss", "among", "ample", "amuse", "angel", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "armor", "aroma", "array", "arrow", "aside", "asset", "atlas", "attic", "audio", "audit", "avert", "awake", "award", "aware", "awful", "bacon", "badge", "badly", "bagel", "baker", "balmy", "banal", "barge", "basic", "basil", "basis", "beach", "beady", "beard", "beast", "begun", "being", "belie", "below", "bench", "beret", "berry", "berth", "bible", "biker", "billy", "binge", "birth", "black", "blade", "blame", "bland", "blank", "blast", "blaze", "bleed", "bless", "blind", "block", "blood", "bloom", "blown", "bluey", "bluff", "blunt", "board", "boast", "bonus", "boost", "booth", "booty", "bored", "borne", "bosom", "bossy", "bound", "bowel", "boxer", "brain", "brake", "brand", "brave", "bread", "break", "breed", "brick", "brief", "bring", "broad", "broke", "brown", "brush", "buddy", "build", "built", "bully", "bunch", "burly", "burnt", "buyer", "cabin", "cable", "cacao", "cache", "caddy", "cadet", "camel", "cameo", "canal", "candy", "canny", "canoe", "canon", "caper", "cargo", "carve", "caste", "catch", "cater", "catty", "cause", "cedar", "chain", "chair", "chalk", "champ", "chaos", "charm", "chart", "chase", "cheap", "cheat", "check", "cheek", "cheer", "chess", "chest", "chief", "child", "chill", "china", "chirp", "choir", "choke", "chord", "civic", "civil", "claim", "clamp", "clan", "clap", "clash", "class", "clean", "clear", "cleat", "clerk", "click", "cliff", "climb", "clock", "close", "cloth", "cloud", "clout", "clove", "clown", "coach", "coast", "cocoa", "colon", "color", "comic", "comma", "corny", "count", "coupe", "court", "coven", "cover", "crack", "craft", "crash", "crave", "crawl", "crazy", "cream", "creep", "crime", "crisp", "crook", "cross", "crowd", "crown", "crude", "cruel", "crumb", "crush", "crust", "cubic", "curry", "curve", "cycle", "daily", "dairy", "daisy", "dance", "dated", "datum", "daunt", "dealt", "death", "debut", "delay", "delta", "demon", "denim", "dense", "depot", "depth", "derby", "deter", "devil", "diary", "dicey", "digit", "dilly", "diner", "dingo", "dirty", "disco", "ditch", "ditto", "ditzy", "dodge", "dogma", "doing", "dolly", "donor", "donut", "doom", "doubt", "dough", "dowel", "downy", "dozen", "draft", "drain", "drama", "drank", "drawl", "dread", "dream", "dress", "dried", "drink", "drive", "droop", "droll", "drunk", "dryer", "duchy", "dully", "dummy", "dumpy", "dunce", "dusty", "dutch", "duvet", "dwarf", "dwell", "dwelt", "eager", "eagle", "early", "earth", "easel", "eaten", "eater", "ebony", "eerie", "eight", "eject", "elate", "elbow", "elder", "elect", "elite", "empty", "enact", "enemy", "enjoy", "enter", "entry", "equal", "equip", "error", "essay", "ester", "ether", "ethic", "evade", "event", "every", "exact", "exalt", "excel", "exert", "exist", "expel", "extra", "facet", "faint", "fairy", "faith", "false", "fancy", "fanny", "farce", "fatal", "fatty", "fault", "favor", "feast", "fecal", "feign", "fella", "felon", "ferry", "fetal", "fetch", "fever", "fiber", "field", "fiend", "fiery", "fifth", "fifty", "fight", "filer", "final", "first", "fishy", "fixed", "fixer", "flame", "flank", "flare", "flash", "fleet", "flesh", "flick", "flint", "float", "flock", "flood", "floor", "flora", "flour", "flush", "flute", "flyer", "focus", "forge", "forth", "forty", "forum", "found", "foyer", "fraud", "freak", "fresh", "fried", "frill", "front", "frost", "frown", "fruit", "fudge", "fully", "funky", "funny", "furry", "gamma", "gauge", "gaunt", "genre", "ghost", "giant", "giddy", "girly", "given", "giver", "glaze", "gleam", "glide", "gloom", "glory", "glove", "glyph", "going", "goose", "gorge", "gouge", "grace", "grade", "graft", "grain", "grand", "grant", "grape", "graph", "grasp", "grass", "grave", "great", "green", "greet", "grief", "grill", "groan", "gross", "group", "grove", "grown", "grunt", "guard", "guess", "guest", "guide", "guilt", "gummy", "guppy"]
hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break
    
    if len(guess_word) == 5:
        print("yay good job knowing how wordle works")
    else:
        print("boooo have you never played wordle?")

print(f"You used {i+1} guesses")