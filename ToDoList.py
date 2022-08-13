from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QPushButton, QLabel, QComboBox, QLineEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5 import uic
import numpy as np

class CHINCHO(QMainWindow):
    def __init__(self):
        super(CHINCHO, self).__init__()

        # load ui file:
        uic.loadUi("BOOM.ui", self)
    

        # define content: Button
        self.add_button = self.findChild(QPushButton, "add_button")
        self.delete_button = self.findChild(QPushButton, "delete_button")
        self.complete_button = self.findChild(QPushButton, "complete_button")
        self.search_button = self.findChild(QPushButton, "search_button")
        self.index_button = self.findChild(QPushButton, "index_button")
        self.slice_button = self.findChild(QPushButton, "slice_button")
        self.filter_button = self.findChild(QPushButton, "filter_button")
        self.sort_button = self.findChild(QPushButton, "sort_button")
        self.restart_button = self.findChild(QPushButton, "restart_button")
        self.close_button = self.findChild(QPushButton, "close_button")

        # define content: LineEdit
        self.first_line = self.findChild(QLineEdit, "first_line")
        self.second_line = self.findChild(QLineEdit, "second_line")
        self.third_line = self.findChild(QLineEdit, "third_line")
        self.fourth_line = self.findChild(QLineEdit, "fourth_line")
        self.fifth_line = self.findChild(QLineEdit, "fifth_line")
        self.sixth_line = self.findChild(QLineEdit, "sixth_line")
        self.seventh_line = self.findChild(QLineEdit, "seventh_line")
        self.eigth_line = self.findChild(QLineEdit, "eigth_line")

        # define content: Just Lines
        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.line_3 = self.findChild(QFrame, "line_3")

        # define content: ComboBox
        self.combo_box = self.findChild(QComboBox, "combo_box")
        self.combo_operator = self.findChild(QComboBox, "combo_operator")

        # define content: Labels
        self.welcome_label = self.findChild(QLabel, "welcome_label")
        self.all_label = self.findChild(QLabel, "all_label")
        self.wanted_label = self.findChild(QLabel, "wanted_label")
        self.done_label = self.findChild(QLabel, "done_label")
        self.answer_label = self.findChild(QLabel, "answer_label")

        # define content: QListWidget
        self.ALL_items = self.findChild(QListWidget, "ALL_items")
        self.Wanted_items = self.findChild(QListWidget, "Wanted_items")
        self.Done_items = self.findChild(QListWidget, "Done_items")

        # create array for ALL Items:
        self.Plan_all_array = np.array([])
        self.Completed_tasks = np.array([])

        # call methods from here:
        self.add_button.clicked.connect(self.Fill_ALL_items)
        self.delete_button.clicked.connect(self.DELETE_from_ALL_items)
        self.complete_button.clicked.connect(self.COMPLETED_item)
        self.search_button.clicked.connect(self.SEARCH_ITEM)
        self.index_button.clicked.connect(self.SEARCH_INDEX)
        self.slice_button.clicked.connect(self.SEARCH_SLICE)
        self.filter_button.clicked.connect(self.FILTER)
        self.sort_button.clicked.connect(self.Sort_Items)

        self.restart_button.clicked.connect(self.Restart_method)
        self.close_button.clicked.connect(lambda: self.close())
        
        # show application
        self.show()
    
# ------------------------------------------- LOGIC -------------------------------------------------- # 
    # define colora for label:
    def GREEN(self):
        self.answer_label.setStyleSheet("background-color: rgb(85, 255, 127);")
    
    def RED(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 84, 115);")

    # define method to fill ALL_items QListWidget: WORKS FINE!
    def Fill_ALL_items(self):
        Entered = self.first_line.text()

        if len(Entered) > 0:
            self.Plan_all_array = np.append(self.Plan_all_array, [Entered])
            self.INDEX = len(self.Plan_all_array)
            self.ALL_items.addItem(f"{self.INDEX}) {self.Plan_all_array[-1]}")
            
            self.answer_label.setText(f"'{Entered}' - was added Successfully!")
            self.GREEN()
            self.first_line.setText("")
        else:
            self.answer_label.setText("Edit Line is Empty, Please Enter The Value!")
            self.RED()

    
    # define method to delete concrete item from QListWidget: WORKS FINE!
    def DELETE_from_ALL_items(self):
        Valuess = self.second_line.text()
        if len(Valuess) > 0:
            try:
                Entered = int(Valuess)
                if Entered >= 1 and Entered <= len(self.Plan_all_array):
                    self.Plan_all_array = np.delete(self.Plan_all_array, Entered - 1)
                    self.ALL_items.clear()

                    j = 1
                    for i in self.Plan_all_array:
                        self.ALL_items.addItem(f"{j}) {i}")
                        j += 1
                    
                    self.answer_label.setText("Item was Deleted Successfully!")
                    self.GREEN()
                    self.second_line.setText("")
                else:
                    self.answer_label.setText(f"Entered Number Should Between 1 and {len(self.Plan_all_array)}")
                    self.RED()    
                    
            except ValueError:
                self.answer_label.setText("Please Enter Only Numbers!")
                self.RED()
        else:
            self.answer_label.setText("Edit Line is Empty, Please Enter The Value!")
            self.RED()
    
    # define method for Completed Item Button: WORKS FINE!
    def COMPLETED_item(self):
        Entered = self.third_line.text()
        if len(Entered) > 0:
            try:
                task_index = int(Entered)
                if task_index >= 1 and task_index <= len(self.Plan_all_array):
                    self.Completed_tasks = np.append(self.Completed_tasks, [self.Plan_all_array[task_index - 1]])

                    self.LENGTH = len(self.Completed_tasks)
                    self.Done_items.addItem(f"{self.LENGTH}) {self.Completed_tasks[-1]}")

                    self.answer_label.setText("Congratulations, One More Task has been completed, Keep Going!")
                    self.GREEN()
                    self.third_line.setText("")

                    # delete this item from ALL items:
                    self.Plan_all_array = np.delete(self.Plan_all_array, task_index - 1)
                    self.ALL_items.clear()

                    j = 1
                    for i in self.Plan_all_array:
                        self.ALL_items.addItem(f"{j}) {i}")
                        j += 1
                else:
                    self.answer_label.setText(f"Entered Number Should be Between 1 and {len(self.Plan_all_array)}")
                    self.RED() 
            
            except ValueError:
                self.answer_label.setText("Please Enter Only Numbers!")
                self.RED()
        else:
            self.answer_label.setText("Edit Line is Empty, Please Enter The Value!")
            self.RED()

    # define method to clear ALL_items QListWidget: WORKS FINE!
    def Restart_method(self):
        self.ALL_items.clear()
        self.Wanted_items.clear()
        self.Done_items.clear()
        self.Plan_all_array = np.array([])
        self.Completed_tasks = np.array([])
        self.answer_label.setText("Lists Are Cleaned!")
        self.GREEN()

    # define method to sort elements inside QlistWidget: WORKS FINE!
    def Sort_Items(self):
        chosen = self.combo_box.currentText()
        if chosen == "ASC":
            order = Qt.SortOrder.AscendingOrder
        elif chosen == "DESC":
            order = Qt.SortOrder.DescendingOrder
        self.ALL_items.sortItems(order)
        self.answer_label.setText(f"Items are Sorted in {chosen}ENDING way!")
        self.GREEN()
    
    # define method for Search Item Button:
    def SEARCH_ITEM(self):
        self.Wanted_items.clear()
        Local_array = np.array([])
        Entered = self.fourth_line.text()
        if len(Entered) > 0:
            try:
                found_index = np.where(self.Plan_all_array == Entered)

                Local_array = np.append(Local_array, self.Plan_all_array[found_index])
                self.Wanted_items.addItem(Local_array[-1])

                self.fourth_line.setText("")
                self.answer_label.setText(f"{Entered} was found Successfully!")
                self.GREEN()
            except IndexError:
                self.answer_label.setText(f"{Entered} is not in the To-Do List!")
                self.RED()
        else:
            self.answer_label.setText("Edit Line is Empty, Please Enter The Value!")
            self.RED()

    # define method for Search With Index Button:
    def SEARCH_INDEX(self):
        self.Wanted_items.clear()
        Local_array = np.array([])
        Valuess = self.fifth_line.text()

        if len(Valuess) > 0:
            try:
                Entered = int(Valuess)
                
                if Entered >= 1 and Entered <= len(self.Plan_all_array):
                    Local_array = np.append(Local_array, self.Plan_all_array[Entered - 1])
                    self.Wanted_items.addItem(Local_array[-1])
                    
                    self.fifth_line.setText("")
                    self.answer_label.setText(f"Item was found Successfully!")
                    self.GREEN()
                else:
                    self.answer_label.setText(f"Entered Number Should be Between 1 and {len(self.Plan_all_array)}")
                    self.RED()

            except ValueError:
                self.answer_label.setText("Please Enter Only Numbers!")
                self.RED()
        else:
            self.answer_label.setText("Edit Line is Empty, Please Enter The Value!")
            self.RED()

    # define method for Search With Slice Button: WORKS FINE!
    def SEARCH_SLICE(self):
        self.Wanted_items.clear()
        Local_array = np.array([])
        starting = self.sixth_line.text()
        ending = self.seventh_line.text()
        if len(starting) > 0 and len(ending) > 0:
            try:
                start_point = int(starting) - 1
                end_point = int(ending)

                if  start_point != (end_point-1) and start_point >= 0 and start_point < end_point and start_point < len(self.Plan_all_array) and end_point <= len(self.Plan_all_array):
                    Local_array = self.Plan_all_array[start_point : end_point]

                    for i in Local_array:
                        self.Wanted_items.addItem(i)
                    
                    self.sixth_line.setText("")
                    self.seventh_line.setText("")
                    self.answer_label.setText(f"Items were found Successfully!")
                    self.GREEN()
                else:
                    self.answer_label.setText(f"Define Start and End points Correctly! Range is from 1 to {len(self.Plan_all_array)}")
                    self.RED()
            
            except ValueError:
                self.answer_label.setText("Please Enter Only Numbers!")
                self.RED()
        else:
            self.answer_label.setText("Please, Fill Both Edit Lines with Numbers!")
            self.RED()
    
    # define method for Filter Items Button:
    def FILTER(self):
        self.Wanted_items.clear()
        Local_array = np.array([])
        chosen_sign = self.combo_operator.currentText()
        Entered = self.eigth_line.text()

        if len(Entered) == 1:
            if chosen_sign == "==":
                for i in self.Plan_all_array:
                    if i[0] == Entered:
                        Local_array = np.append(Local_array, i)
            elif chosen_sign == ">":
                for i in self.Plan_all_array:
                    if i[0] > Entered:
                        Local_array = np.append(Local_array, i)
            elif chosen_sign == "<":
                for i in self.Plan_all_array:
                    if i[0] < Entered:
                        Local_array = np.append(Local_array, i)
            elif chosen_sign == ">=":
                for i in self.Plan_all_array:
                    if i[0] >= Entered:
                        Local_array = np.append(Local_array, i)
            elif chosen_sign == "<=":
                for i in self.Plan_all_array:
                    if i[0] <= Entered:
                        Local_array = np.append(Local_array, i)
            
            for i in Local_array:
                self.Wanted_items.addItem(i)
            
            self.eigth_line.setText("")
            self.answer_label.setText("Items Filtered Successfully!")
            self.GREEN()
        elif len(Entered) == 0:
            self.answer_label.setText("Edit Line is Empty, Please Enter One Letter!")
            self.RED()
        else:
            self.answer_label.setText("Please Enter Only One Letter!")
            self.RED()

    
# ----------------------------------------------- END -------------------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = CHINCHO()
    sys.exit(app.exec_())
