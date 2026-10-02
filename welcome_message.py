import time
import random

# --- Short Form Creation ---
def short_form(idx, *names, **addons):
    final = ''
    try:
        # Build short form from names
        for name in names:
            final += name[idx]

        # Add prefix/suffix if provided
        for keys in addons:
            if keys == 'prefix':
                final = addons[keys] + final
            elif keys == 'suffix':
                final = final + addons[keys]
            else:
                print('You are not good at typing, are you ...')

        # --- Time Validation ---
        current_second = int(time.time()) % 60
        if current_second % 2 == 0:
            print(" The clock favors you...")
        else:
            raise Exception(" The sands of time resist you...")

        # --- Luck Validation ---
        roll = random.randint(1, 10)
        if roll > 5:
            print(" Fortune smiles upon you...")
        else:
            raise Exception(" Luck has abandoned you...")

    except TypeError as e:
        print('Wrong data type: ', e)
    except IndexError as e:
        print('Indexing is going wrong:', e)
    except Exception as e:
        print('Validation failed:', e)
    else:
        return final
    finally:
        print("Hope you managed to pass this stage ...")

# --- Name Strength Calculation ---
strength = {'name':10, 'surname':20, 'nickname':30, 'alias':40, 'aka':50}

def name_strength(**fullname):
    result = 0
    try:
        for key, value in fullname.items():
            result += strength[key] * len(value)
    except KeyError as e:
        print(" You invoked forbidden fields:", e)
    else:
        return result

# --- Validation Trials ---
def validate(**prelimdata):
    try:
        assert prelimdata['sc'] is not None
        assert prelimdata['ns'] is not None
    except KeyError as e:
        print(" You dropped the scrolls of data...")
        print("Validation failed due to", e)
    except AssertionError:
        print(" One of the earlier steps has gone wrong.")
        print("Validation failed.")
    else:
        print(" Looking good so far...")
        print("Sending for deeper validation...")
        print(" Opening connection to the Oracle server...")
        try:
            deep_validate(prelimdata)
            luck_validate()
            time_validate()
            final_boss()
        except ValueError as e:
            print(" The Oracle rejects you:", e)
            print("Validation failed.")
        else:
            print(" Congrats, hero! Validation Successful.")
            print("Welcome to the Den of Coders!")
        finally:
            print(" Closing connection to the Oracle server")

def deep_validate(prelimdata):
    print("📜 The Oracle studies your scrolls:", prelimdata)
    threshold_ns = random.randint(1, 200)
    threshold_sc = random.randint(10, 20)
    print(f" Thresholds: ns={threshold_ns}, sc={threshold_sc}")
    if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc:
        raise ValueError("Your power is unstable...")



# --- Final Boss Stage ---
def final_boss():
    riddles = {
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "echo",
        "The more you take, the more you leave behind. What am I?": "footsteps",
        "I’m always running but never move. You can’t see me but you can feel me. What am I?": "time"
    }
    riddle, answer = random.choice(list(riddles.items()))
    print(" The Final Boss appears!")
    print(" Riddle of the Oracle:")
    print(riddle)
    user_answer = input("Your answer, adventurer: ").strip().lower()
    if user_answer != answer:
        raise ValueError("The riddle defeated you...")
    else:
        print(" You solved the riddle! The Oracle bows to your wisdom.")

# --- Storyline Intro ---
print(" Welcome, brave coder, to the Programmers' Den!")
print("Your quest: forge your identity, prove your strength, and survive the trials of validation...")
print()
print(" Step 1: Create a short code → sc = short_form(idx, words..., prefix= , suffix= )")
print(" Step 2: Measure your name strength → ns = name_strength(name= , surname= , aka= , alias= )")
print(" Step 3: Face the Oracle → validate(sc=sc, ns=ns)")
print()
print("Good luck, adventurer...")



