import os

# Read FB-input.txt.
def ReadDialogues():
    Dialogues = []
    with open('FB-input.txt', 'r', encoding='utf-8-sig') as D:
        for line in D:
            Dialogues.append(line.strip())
        return Dialogues

# Optimization dialogues.
def DialoguesProccessing(Dialogues):
    # Set speakers.
    speaker1 = 'Allen'
    speaker2 = 'Tom'
    nowspeaker = speaker1

    newDialogues = []
    # Outer loop determines speaker.
    for line in Dialogues:
        if line == speaker1:
            if nowspeaker == speaker1:
                continue
            else:
                nowspeaker = speaker1
        elif line == speaker2:
            if nowspeaker == speaker2:
                continue
            else:
                nowspeaker = speaker2
        else:
            newDialogues.append(nowspeaker + ': ' + line)
    return newDialogues

# Write in FB-output.txt.
def Write_txt(newDialogues):
    with open('FB-output.txt', 'w', encoding='utf-8') as txt:
        for line in newDialogues:
            txt.write(line + '\n')

if __name__ == '__main__':
    if os.path.isfile('FB-input.txt'):
        Dialogues = ReadDialogues()
        newDialogues = DialoguesProccessing(Dialogues)
        Write_txt(newDialogues)
    else:
        print('Dialogues not exist.')




