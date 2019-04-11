import os

# Read LINE-input.txt.
def ReadDialogues():
    Dialogues = []
    with open('LINE-input.txt', 'r', encoding='utf-8-sig') as D:
        for line in D:
            Dialogues.append(line.strip())
        return Dialogues

# Dialogues analystics.
def DialoguesAnalystics(Dialogues):

    AllenPicSum = 0
    AllenStickerSum = 0
    AllenWordSum = 0
    VikiPicSum = 0
    VikiStickerSum = 0
    VikiWordSum = 0
    for line in Dialogues:
        line = line.split(' ')
        if line[1] == 'Allen':
            if line[2] == '圖片':
                AllenPicSum += 1
            elif line[2] == '貼圖':
                AllenStickerSum += 1
            else:
                for w in line[2:]:
                    AllenWordSum += len(w)
        else:
            if line[2] == '圖片':
                VikiPicSum += 1
            elif line[2] == '貼圖':
                VikiStickerSum += 1
            else:
                for w in line[2:]:
                    VikiWordSum += len(w)
    print('AllenPicSum: ', AllenPicSum)
    print('AllenStickerSum: ', AllenStickerSum)
    print('AllenWordSum: ', AllenWordSum)
    print('VikiPicSum: ', VikiPicSum)
    print('VikiStickerSum: ', VikiStickerSum)
    print('VikiWordSum: ', VikiWordSum)

# Write in LINE-output.txt.
def Write_txt(newDialogues):
    with open('LINE-output.txt', 'w', encoding='utf-8') as txt:
        for line in newDialogues:
            txt.write(line + '\n')

if __name__ == '__main__':
    if os.path.isfile('LINE-input.txt'):
        Dialogues = ReadDialogues()
        DialoguesAnalystics(Dialogues)
    else:
        print('Dialogues not exist.')