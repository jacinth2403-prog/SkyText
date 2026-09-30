import json

with open("data/poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)

print("Number of poems:", len(poems))

required_fields = [
    "id",
    "title",
    "author",
    "language",
    "text",
    "moods",
    "weather",
    "themes",
    "source",
    "license"
]

errors = []

for i, poem in enumerate(poems):
    for field in required_fields:
        if field not in poem:
            errors.append(f"Poem {i + 1}: missing '{field}'")

    for field in ["moods", "weather", "themes"]:
        if field in poem and not isinstance(poem[field], list):
            errors.append(
                f"Poem {i + 1}: '{field}' should be a list"
            )

print("\nValidation results:")

if errors:
    print(f"Found {len(errors)} errors:")
    for error in errors:
        print(error)
else:
    print("All poems have the correct schema.")

print("\nLanguages:")
languages = {}

for poem in poems:
    language = poem["language"]
    languages[language] = languages.get(language, 0) + 1

for language, count in languages.items():
    print(f"- {language}: {count}")