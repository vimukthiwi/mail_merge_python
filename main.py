# Load the content of the starting letter template
with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

# Load the list of invited names
with open("Input/Names/invited_names.txt") as invited_names_file:
    invited_names = invited_names_file.read().splitlines()

# Process each name and create a personalized invitation letter
for name in invited_names:
    final_letter = starting_letter.replace("[name]", name)
    filename = f"Output/ReadyToSend/{name}_invitation.txt"
    # Write the invitation letter to the corresponding file
    with open(filename, "w") as invitation_file:
        invitation_file.write(final_letter)
