import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg

class SidebarContent(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super(qtw.QWidget, self).__init__(*args, **kwargs)

        self.layout = qtw.QGridLayout()
        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgb(254,174,0); border-right: 3px solid black}""")

        spacer_label1 = qtw.QLabel()
        self.featured_label = qtw.QLabel()
        self.browse_label = qtw.QLabel()
        self.list_label = qtw.QLabel()
        self.timetable_label = qtw.QLabel()
        self.nutrition_label = qtw.QLabel()
        self.add_label = qtw.QLabel()
        spacer_label2 = qtw.QLabel()
        self.pageLabel_list = [self.featured_label, self.browse_label, self.list_label, self.timetable_label, self.nutrition_label, self.add_label]
        self.generateIcons()

        self.layout.addWidget(self.background_label, 0, 0, 10, 3)
        self.layout.addWidget(spacer_label1, 1, 1, 1, 1)
        self.layout.addWidget(self.featured_label, 2, 1, 1, 1)
        self.layout.addWidget(self.browse_label, 3, 1, 1, 1)
        self.layout.addWidget(self.list_label, 4, 1, 1, 1)
        self.layout.addWidget(self.timetable_label, 5, 1, 1, 1)
        self.layout.addWidget(self.nutrition_label, 6, 1, 1, 1)
        self.layout.addWidget(spacer_label2, 7, 1, 1, 1)
        self.layout.addWidget(self.add_label, 8, 1, 1, 1)

        self.featured_button = qtw.QPushButton()
        self.browse_button = qtw.QPushButton()
        self.list_button = qtw.QPushButton()
        self.timetable_button = qtw.QPushButton()
        self.nutrition_button = qtw.QPushButton()
        self.add_button = qtw.QPushButton()
        self.pageButton_list = [self.featured_button, self.browse_button, self.list_button, self.timetable_button, self.nutrition_button, self.add_button]
        for button in self.pageButton_list:
            button.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
            button.setStyleSheet("""QWidget {background-color: rgba(254,255,255,0); margin: 15px}""")
            button.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))

        self.layout.addWidget(self.featured_button, 2, 1, 1, 1)
        self.layout.addWidget(self.browse_button, 3, 1, 1, 1)
        self.layout.addWidget(self.list_button, 4, 1, 1, 1)
        self.layout.addWidget(self.timetable_button, 5, 1, 1, 1)
        self.layout.addWidget(self.nutrition_button, 6, 1, 1, 1)
        self.layout.addWidget(self.add_button, 8, 1, 1, 1)

        rows = [1, 1, 1, 1, 1, 1, 1, 2, 1]
        for i, r in enumerate(rows):
            self.layout.setRowStretch(i, r)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)


    def generateIcons(self):
        image_list = ["/Users/josephsmith/Documents/recipe-manager/icons/featured_black.tiff",
                    "/Users/josephsmith/Documents/recipe-manager/icons/browse_black.tiff",
                    "/Users/josephsmith/Documents/recipe-manager/icons/shopping_black.tiff",
                    "/Users/josephsmith/Documents/recipe-manager/icons/calendar_black.tiff",
                    "/Users/josephsmith/Documents/recipe-manager/icons/nutrition_black.tiff",
                    "/Users/josephsmith/Documents/recipe-manager/icons/add_black.tiff"]
        for n, image in enumerate(image_list):
            icon = qtg.QIcon()
            icon.addFile(image)
            pixmap = icon.pixmap(qtc.QSize(35,35))
            label = self.pageLabel_list[n]
            label.setPixmap(pixmap)
            label.setAlignment(qtc.Qt.AlignCenter)


    def generateText(self):
        text_list = ["Featured",
                    "Browse",
                    "Shopping",
                    "Timetable",
                    "Nutrition"]
        for n, text in enumerate(text_list):
            label = self.pageLabel_list[n]
            label.setText(text_list[n])
            label.setStyleSheet("""QWidget {font: 30pt 'Avenir'; font-weight: bold}""")


class SidebarWidget(qtw.QWidget):
    def __init__(self, parent=None):

        super(SidebarWidget, self).__init__(parent=parent)

        self.sidebarContent = SidebarContent()

        self.animationDuration = 300
        self.expandAnimation = qtc.QParallelAnimationGroup()
        self.contractAnimation = qtc.QParallelAnimationGroup()
        self.contentArea = qtw.QScrollArea()
        self.toggleButton = qtw.QToolButton()
        self.mainLayout = qtw.QGridLayout()

        rm_label = qtw.QLabel()
        rm_label.setText("RM")
        rm_label.setStyleSheet("""QWidget {font: 30pt 'Avenir'; font-weight: bold; margin: 10 px}""")
        rm_label.setAlignment(qtc.Qt.AlignCenter)
        toggleButton = self.toggleButton
        toggleButton.setFixedSize(60,60)
        toggleButton.setStyleSheet("""QWidget {border: 'none'; margin: 10 px}""")
        toggleButton.setCheckable(True)
        toggleButton.setChecked(False)

        self.contentArea.setLayout(self.sidebarContent.layout)
        self.contentArea.setFrameShape(qtw.QFrame.NoFrame)
        self.contentArea.setWidgetResizable(True)

        expandAnimation = self.expandAnimation
        expandAnimation.addAnimation(qtc.QPropertyAnimation(self, b"maximumWidth"))
        expandAnimation.addAnimation(qtc.QPropertyAnimation(self.contentArea, b"maximumWidth"))

        contractAnimation = self.contractAnimation
        contractAnimation.addAnimation(qtc.QPropertyAnimation(self, b"maximumWidth"))
        contractAnimation.addAnimation(qtc.QPropertyAnimation(self.contentArea, b"maximumWidth"))

        mainLayout = self.mainLayout
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.contentArea, 0, 0, 1, 1)
        mainLayout.addWidget(rm_label, 0, 0, 1, 1, qtc.Qt.AlignTop | qtc.Qt.AlignHCenter)
        mainLayout.addWidget(self.toggleButton, 0, 0, 1, 1, qtc.Qt.AlignTop | qtc.Qt.AlignHCenter)
        self.setLayout(self.mainLayout)

        def clickedAnimation(checked):
            self.contentArea.setSizePolicy(qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)

            def setAnimation(animation, start_width, final_width):
                for i in range(animation.animationCount()):
                    a = animation.animationAt(i)
                    a.setDuration(self.animationDuration)
                    a.setStartValue(start_width)
                    a.setEndValue(final_width)

            if checked: 
                collapsedWidth = self.sidebarContent.layout.sizeHint().width() + 30
                self.sidebarContent.generateText()
                self.contentArea.setLayout(self.sidebarContent.layout)
                contentWidth = self.sidebarContent.layout.sizeHint().width() + 80
                setAnimation(self.expandAnimation, collapsedWidth, contentWidth)
                self.expandAnimation.start()

            else:
                contentWidth = self.sidebarContent.layout.sizeHint().width() + 80
                self.sidebarContent.generateIcons()
                self.contentArea.setLayout(self.sidebarContent.layout)
                collapsedWidth = self.sidebarContent.layout.sizeHint().width() + 30
                setAnimation(self.contractAnimation, contentWidth, collapsedWidth)
                self.contractAnimation.start()

        self.toggleButton.clicked.connect(clickedAnimation)