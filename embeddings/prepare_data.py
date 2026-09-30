import json


# Load poem data
with open("data/poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)


print("Number of poems:", len(poems))


# Prepare text for embedding
prepared_poems = []

for poem in poems:
    embedding_text = f"""Title: {poem["title"]}
Author: {poem["author"]}
Mood: {", ".join(poem["moods"])}
Weather: {", ".join(poem["weather"])}
Themes: {", ".join(poem["themes"])}

{poem["text"]}"""

    prepared_poems.append({
        "id": poem["id"],
        "embedding_text": embedding_text
    })


# Display the first prepared poem
print("\nFirst prepared poem:")
print(prepared_poems[0]["embedding_text"])


print("\nPrepared poems:", len(prepared_poems))