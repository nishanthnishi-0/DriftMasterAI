import json
import os

knowledge = []

data_folder = "data"

for filename in os.listdir(data_folder):

    if filename.endswith(".json"):

        print(f"Loading: {filename}")

        try:

            with open(
                os.path.join(data_folder, filename),
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                knowledge.extend(data)

                print(f"SUCCESS: {filename}")

        except Exception as e:

            print(f"ERROR IN {filename}")
            print(e)


from rapidfuzz import fuzz

def get_response(user_message):

    user_message = user_message.lower().strip()

    # Greetings
    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    if user_message in greetings:
        return """
Hello! 👋

I'm DriftMaster AI.

I can help with:
• Drifting techniques
• Car setup
• Tire pressure
• Suspension
• Differential tuning
• Drift troubleshooting

Ask me anything about drifting.
"""

    best_match = None
    best_score = 0

    for item in knowledge:

        score = fuzz.partial_ratio(
            user_message,
            item["question"].lower()
        )

        if score > best_score:
            best_score = score
            best_match = item

    if best_score >= 85:
        return best_match["answer"]

    return diagnose_problem(user_message)
def diagnose_problem(user_message):

    user_message = user_message.lower()

    if "spin out" in user_message:

        return """
Possible reasons:

• Too much throttle
• Late counter steering
• Excessive steering angle
• High entry speed

Check:
- Tire pressure
- Differential
- Suspension setup
"""

    if "cant drift" in user_message:

        return """
Possible causes:

• Low speed
• Insufficient power
• Excessive rear grip
• Poor weight transfer

Tell me:
- Car model
- Horsepower
- Tire pressure
"""

    if "too much grip" in user_message:

        return """
Suggestions:

• Increase rear tire pressure
• Use harder rear tires
• Reduce rear downforce
• Increase power
"""

    return """
I don't know that yet.

Try asking:
• Why do I spin out?
• Why can't I drift?
• Best drift car?
• Tire pressure?
"""