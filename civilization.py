from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import json

with open('achievements.json', "r",encoding='utf-8') as json_file:
    achievements = json.load(json_file)

app = QApplication([])
window = QWidget()
layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
model = QStandardItemModel()
image = QLabel()
labelImage = QPixmap('qt.png')
image.setPixmap(labelImage)
for achievement in achievements:                   
    item = QStandardItem(achievement)
    check = Qt.CheckState.Checked if achievements[achievement] == True else Qt.CheckState.Unchecked
    item.setCheckState(check)
    item.setCheckable(True)
    model.appendRow(item)

#Center
qr = window.frameGeometry()
cp = window.screen().availableGeometry().center()
cp.setY(0)
qr.moveCenter(cp)
window.move(qr.x(), 100)

listView = QListView()
listView.setModel(model)
listView.setMinimumWidth(400)
layout.addWidget(image)
layout.addWidget(listView)
window.setLayout(layout)
window.setWindowTitle("Civilization: list of completed civ achievements")
window.setWindowIcon(QIcon('civ.png'))
window.show()
app.exec()

newStates = []
model = listView.model()
for r in range(model.rowCount()):
    objeto = model.takeItem(r, 0)
    if objeto.checkState() == Qt.CheckState.Checked:
        newStates.append(1)
    else:
        newStates.append(0)

i = 0
for achievement in achievements:
    achievements[achievement] = newStates[i]
    i = i + 1

with open("achievements.json", "w") as jsonFile:
    json.dump(achievements, jsonFile)