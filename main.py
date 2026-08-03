from pathlib import Path

BASE_DIR = Path(__file__).parent
names_path = BASE_DIR / "Input" / "Names" / "invited_names.txt"
letters_path = BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
output_dir = BASE_DIR / "Output" / "ReadyToSend"

PLACEHOLDER = "[name]"

with open(names_path) as invited_names:
    names = invited_names.readlines()

with open(letters_path) as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(output_dir / f"letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
