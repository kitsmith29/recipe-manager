import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PostgreSQL

class RecipeWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(qtw.QWidget, self).__init__(*args, **kwargs)
        
        self.createWidgets()
        self.configureLayout()
        
    def createWidgets(self):

        self.background_label = qtw.QLabel()
        self.background_label.setStyleSheet("""QWidget {background-color: rgba(254,174,0,20)}""")

        self.main_title = qtw.QLabel()
        self.main_title.setStyleSheet("""QWidget {font: 55pt 'Avenir'; 
                                                    font-weight: bold}""")

        self.recipe_info = InfoWidget()

        self.ingredients_title = qtw.QLabel()
        self.ingredients_title.setText("Ingredients")
        self.ingredients_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; 
                                                    font-weight: bold}""")
        self.ingredients_body = qtw.QLabel()
        self.ingredients_body.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")

        self.instructions_title = qtw.QLabel()
        self.instructions_title.setText("Instructions")
        self.instructions_title.setStyleSheet("""QWidget {font: 25pt 'Avenir'; 
                                                    font-weight: bold}""")
        self.instructions_body = qtw.QLabel()
        self.instructions_body.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")
        self.instructions_body.setWordWrap(True)

        self.picture = qtw.QLabel()
        self.picture_data = None
        
        self.spacer = qtw.QLabel()
        
    def configureLayout(self):

        layout = qtw.QGridLayout()
        layout.addWidget(self.main_title, 0, 1, 1, 3)
        layout.addWidget(self.recipe_info, 2, 1, 1, 3)
        layout.addWidget(self.spacer, 3, 1, 1, 1)
        layout.addWidget(self.ingredients_title, 4, 1, 1, 1)
        layout.addWidget(self.ingredients_body, 6, 1, 1, 1)
        layout.addWidget(self.instructions_title, 8, 1, 1, 1)
        layout.addWidget(self.instructions_body, 10, 1, 1, 3)
        layout.addWidget(self.picture, 4, 2, 5, 2)

        cols = [1, 6, 6, 6, 6]
        for n in range(len(cols)):
            layout.setColumnStretch(n, cols[n])
        layout.setContentsMargins(60,30,80,0)

        self.setLayout(layout)

    def getRecipe(self, id_num):
        # Pull data for recipe id number from database and add to widget
        psql = PostgreSQL.PostgreSQL()
        psql.openConnection()
        title, feeds, calories, prep, cook, instructions, image = psql.extractRecipe(id_num)
        psql.closeConnection()
        recipe_info = [str(feeds), str(calories), str(prep), str(cook)]

        ingredient_list = ["4 sweet potatoes", "1 brown onion", "2 peppers", "2 red chillis",
                            "1 bunch of spring onions", "400g black beans", "3 limes", 
                            "2 large avocados", "2 garlic cloves", "2 tsp ground cumin", 
                            "2 tsp paprika", "2 tsp chilli flakes", "1 handful of coriander"]

        self.addTitle(title)
        for ingredient in ingredient_list:
            self.addIngredient(ingredient)
        self.addInstruction(instructions)
        self.addInfo(recipe_info)
        self.addPicture(image)
        return(self)

    def addTitle(self, title_string):
        # Configure title label with title text
        
        self.main_title.setText(title_string)

    def addIngredient(self, ingredient_string):
        # Configure ingredients label with list of ingredients
        
        self.ingredients_body.setText(self.ingredients_body.text() + "- " + ingredient_string + "\n")

    def addInstruction(self, instruction_string):
        # Configure instructions label with instructions text
        
        self.instructions_body.setText(instruction_string)

    def addInfo(self, input_info):
        # Configure info widget with recipe info
        
        for n, info in enumerate(input_info):
            self.recipe_info.info_body[n].setText(self.recipe_info.info_body[n].text() + info)

    def addPicture(self, picture_data):
        # Draw recipe image with rounded border
        
        self.picture_data = picture_data
        image = qtg.QImage()
        image.loadFromData(self.picture_data)
        pixmap = qtg.QPixmap.fromImage(image.scaled(350,350, qtc.Qt.KeepAspectRatio, qtc.Qt.SmoothTransformation))
        
        radius = 50
        rounded = qtg.QPixmap(pixmap.size())
        rounded.fill(qtg.QColor("transparent"))
        painter = qtg.QPainter(rounded)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        painter.setBrush(qtg.QBrush(pixmap))
        painter.setPen(qtg.QPen(qtc.Qt.black, 5))
        path = qtg.QPainterPath()
        rect = qtc.QRectF(pixmap.rect())
        path.addRoundedRect(rect, radius, radius)
        painter.setClipPath(path)
        painter.fillPath(path, painter.brush())
        painter.strokePath(path, painter.pen())
        painter.end()
        
        self.picture.setPixmap(rounded)
        self.picture.setAlignment(qtc.Qt.AlignCenter)


class InfoWidget(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super(qtw.QWidget, self).__init__(*args, **kwargs)

        self.createWidgets()
        self.configureLayout()

    def createWidgets(self):
        
        self.feeds_title = qtw.QLabel()
        self.feeds_title.setText("Feeds:")
        self.calories_title = qtw.QLabel()
        self.calories_title.setText("Calories:")
        self.prep_title = qtw.QLabel()
        self.prep_title.setText("Prep time:")
        self.cook_title = qtw.QLabel()
        self.cook_title.setText("Cook time:")

        self.feeds_info = qtw.QLabel()
        self.calories_info = qtw.QLabel()
        self.prep_info = qtw.QLabel()
        self.cook_info = qtw.QLabel()

        self.info_title = [self.feeds_title, self.calories_title, self.prep_title, self.cook_title]
        self.info_body = [self.feeds_info, self.calories_info, self.prep_info, self.cook_info]

        for info in self.info_title:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'; 
                                            font-weight: bold}""")

        for info in self.info_body:
            info.setStyleSheet("""QWidget {font: 16pt 'Avenir'}""")
            
    def configureLayout(self):

        layout = qtw.QGridLayout()
        layout.addWidget(self.feeds_title, 0, 0, 1, 1)
        layout.addWidget(self.feeds_info, 0, 1, 1, 1)
        layout.addWidget(self.calories_title, 0, 2, 1, 1)
        layout.addWidget(self.calories_info, 0, 3, 1, 1)
        layout.addWidget(self.prep_title, 0, 4, 1, 1)
        layout.addWidget(self.prep_info, 0, 5, 1, 1)
        layout.addWidget(self.cook_title, 0, 6, 1, 1)
        layout.addWidget(self.cook_info, 0, 7, 1, 1)
        
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        cols = [1, 6, 1, 7, 1, 8, 1, 25]
        for n in range(8):
            layout.setColumnStretch(n, cols[n])