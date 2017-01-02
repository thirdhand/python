from datetime import datetime
from tkinter import *
from tkinter import ttk



class Init():
    def __init__(self, Main, GameLogic):
        Main()
        GameLogic()
    
    
# Class containing the GUI definitions for tkinter and ttk.    
class GUI(Frame):
    def __init__(self, parent):
        # Creates the main frame and background color.
        Frame.__init__(self, parent, background = "#d9d9d9")
        self.parent = parent
        self.style = ttk.Style()
        self.style.theme_use("default")
        #self.style.configure("TButton", padding = (0, 2, 0, 0), font = "TkFixedFont")
        
        self.initUI()
        self.gamelogic = GameLogic()
        
        # List buildings you can build.
        self.buildingsListbox = Listbox(self, height = 13, background = "white", listvariable = self.gamelogic.buildingsStringVar)
        
        # A name entry widget which currently does not work correctly due to miscommunication between GUI and GameLogic.
        self.nameentry = ttk.Entry(self, textvariable = self.gamelogic.playernameStringVar)
        
        # Hidden label to display the name entered in self.nameentry.
        self.saved_nameLabel = ttk.Label(self, textvariable = self.gamelogic.saved_playernameStringVar)
        
        # Hidden label to display if an invalid name is entered in self.nameentry.
        self.error_playernameLabel = ttk.Label(self, foreground = "red", text = "Invalid name!")
        
        self.UI_configuration()
    
        
    def initUI(self):
        self.parent.title("Gametest")
        self.pack(fill = BOTH, expand = True)
        self.centerWindow()
        
    # Creates the window in which the main frame and the rest is displayed. self.parent.geometry takes width, height, and then centers the window by checking for display resolution and then halving it to find the coordinates.   
    def centerWindow(self):
        w = 640
        h = 480
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        
    # Communication function between this GUI class and the GameLogic class.
    def add_buildings(self, buildingsListbox):
        self.gamelogic.add_buildings(self.buildingsListbox)
        
    # Communication function between this GUI class and the GameLogic class. Does not currently work as intended (the saved name is not displayed).    
    def save_playername(self, saved_nameLabel, error_playernameLabel):
        self.gamelogic.save_playername(self.saved_nameLabel, self.error_playernameLabel)
        
    # Function with most of the widgets and their configuration.    
    def UI_configuration(self):
        #time_leftMethod = time_left
        
        # Adding columns and padding space.
        self.columnconfigure(0, pad = 2)
        self.columnconfigure(1, pad = 4)
        self.columnconfigure(2, pad = 4)
        self.columnconfigure(3, pad = 4)
        self.columnconfigure(4, pad = 4)
        self.columnconfigure(5, pad = 4)
        self.columnconfigure(6, pad = 4)
        self.columnconfigure(7, pad = 4)
        self.columnconfigure(8, pad = 0)
        self.columnconfigure(9, pad = 4)
        # Adding rows and padding space.
        self.rowconfigure(0, pad = 3)
        self.rowconfigure(1, pad = 3)
        self.rowconfigure(2, pad = 20)
        self.rowconfigure(3, pad = 3)
        self.rowconfigure(4, pad = 3)
        self.rowconfigure(5, pad = 3)
        self.rowconfigure(6, pad = 3)

        
        # Creating UI elements and setting their parameters.
        
        add_buildingsLabel = ttk.Label(self, text = "Add building")
        # Creating main buttons.
        button1 = ttk.Button(self, text = "Save name", command = self.save_playername)
        button2 = ttk.Button(self, text = "Button 2")
        button3 = ttk.Button(self, text = "Build house", command = self.add_buildings)
        button4 = ttk.Button(self, text = "End turn", command = self.gamelogic.run_simulation)
        quitButton = ttk.Button(self, text = "Quit", command = self.quit)
        
        
        resources = ttk.Labelframe(self, text = "Resources", labelanchor = "nw", width = 150, height = 100)
        buildingsLabelframe = ttk.Labelframe(self, text = "Buildings", labelanchor = "nw", width = 100, height = 200)
        #time_leftLabel = Label(self, textvariable = time_leftStringVar)
        turns_leftLabel = ttk.Label(self, textvariable = self.gamelogic.turns_leftStringVar)
        turns_left_current_buildingLabel = ttk.Label(self, textvariable = self.gamelogic.turns_left_current_buildingStringVar)
        
        housesLabel = ttk.Label(buildingsLabelframe, textvariable = self.gamelogic.houses_numberStringVar)
        air_purifierLabel = ttk.Label(buildingsLabelframe, textvariable = self.gamelogic.air_purifiers_numberStringVar)
        turnLabel = ttk.Label(self, textvariable = self.gamelogic.turn_numberStringVar)
        building_queueLabel = ttk.Label(self, text = "Building queue")
        building_queueListbox = Listbox(self, height = 5, background = "white", listvariable = self.gamelogic.building_queueStringVar)
        #building_queueStringVar.set(self.building_queue)
        
        # Binding actions to elements.
        # Double-1 means double left click.
        self.buildingsListbox.bind("<Double-1>", self.add_buildings)
        
        # Placement of UI elements on the grid.
        self.grid(sticky = N + S + W + E)
        
        add_buildingsLabel.grid(row = 0, column = 0, sticky = S)
        self.nameentry.grid(row = 9, column = 0, sticky = W)
        self.nameentry.focus()
        button1.grid(row = 9, column = 1)
        button2.grid(row = 9, column = 2)
        button3.grid(row = 9, column = 3)
        button4.grid(row = 9, column = 4)
        quitButton.grid(row = 9, column = 8, sticky = E)
        
        self.buildingsListbox.grid(row = 1, column = 0, sticky = W)
        #resources.grid(row = 0, column = 8, sticky = W)
        buildingsLabelframe.grid(row = 1, column = 8, sticky = W)
        housesLabel.grid(row = 2, column = 8, sticky = W)
        air_purifierLabel.grid(row = 1, column = 8, sticky = W)
        turnLabel.grid(row = 0, column = 8, sticky = E)
        self.saved_nameLabel.grid(row = 8, column = 0, sticky = W)
        self.error_playernameLabel.grid(row = 8, column = 0, sticky = W)
        self.error_playernameLabel.grid_remove()
        building_queueLabel.grid(row = 2, column = 0, sticky = S)
        building_queueListbox.grid(row = 3, column = 0, sticky = W)
        #time_leftLabel.grid(row = 2, column = 1, sticky = W)
        turns_leftLabel.grid(row = 4, column = 0, sticky = W)
        turns_left_current_buildingLabel.grid(row = 5, column = 0, sticky = W)
        emptylabel = ttk.Label(self, text = "")
        emptylabel.grid(row = 2, column = 8)
   
        
# Class containing the actual game logic.
class GameLogic():
    def __init__(self):
        self.turn = 0
        self.turns_left = 0
        self.turns_left_current_building = 0
        self.air_purifiers_number = 0
        self.houses_number = 0
        self.buildings_names = ""
        self.building_queue = []
        self.currently_building = ""
        self.buildings_list = sorted(["Air purifier", "Water purifier", "House", "Robot factory"])
        # Defining which buildings that can be built and how many turns they take to build.
        self.buildings_dict = {
            "Air purifier" : 4,
            "Water purifier" : 4,
            "House" : 5,
            "Robot factory" : 7
            }
        
        self.playernameStringVar = StringVar()
        self.saved_playernameStringVar = StringVar()
        self.turn_numberStringVar = StringVar()
        self.turn_numberStringVar.set("Turn %s" % self.turn)
        
        self.air_purifiers_numberStringVar = StringVar()
        self.houses_numberStringVar = StringVar()
        self.buildingsStringVar = StringVar()
        self.building_queueStringVar = StringVar()
        self.time_leftStringVar = StringVar()
        self.turns_leftStringVar = StringVar()
        self.turns_left_current_buildingStringVar = StringVar()
        
        self.set_buildings()

    
    # Populate the list of built buildings with building names in self.buildings_list.
    def set_buildings(self):
        for name in self.buildings_list:
            #self.buildings_dict[name] = 0
            self.buildings_names += "{%s}\n" % name
        self.buildingsStringVar.set(self.buildings_names)
        self.air_purifiers_numberStringVar.set("Air purifiers: %s" % self.air_purifiers_number)
        self.houses_numberStringVar.set("Houses: %s" % self.houses_number)
        #chars_to_remove = ["{", "'", "}"]
        #self.houses_numberStringVar.set(self.buildings_dict)
        #buildings_names_filtered = ''.join([char for char in self.houses_numberStringVar.get() if char not in chars_to_remove])
        #buildings_names_filtered = buildings_names_filtered.replace(",", "\n")
        #self.houses_numberStringVar.set(buildings_names_filtered)
            

    # This defines what happens when clicking End turn.    
    def run_simulation(self):
        if self.turn < 50:
            self.turn += 1
            self.turn_numberStringVar.set("Turn %s" % self.turn)
            print("Turn", self.turn)
            if self.turns_left_current_building > 1:
                self.turns_left_current_building -= 1
                #print("Turns left: ", self.turns_left)
                self.turns_left_current_buildingStringVar.set("Turns left for\ncurrent building: %s" % self.turns_left_current_building)
                print("Turns left for current building: ", self.turns_left_current_building)
            elif self.turns_left_current_building == 1:
                #self.turns_left_current_building = 0
                print(self.building_queue)
                self.turns_left_current_building = self.buildings_dict[self.building_queue[0]]
                self.building_queue.remove(self.currently_building)
                self.turns_left_current_buildingStringVar.set("Built %s" % self.currently_building)
                #self.turns_leftStringVar.set("Built %s" % self.currently_building)
                if self.currently_building == "House":
                    self.houses_number += 1
                    self.houses_numberStringVar.set("Houses: %s" % self.houses_number)
                elif self.currently_building == "Air purifier":
                    self.air_purifiers_number += 1
                    self.air_purifiers_numberStringVar.set("Air purifiers: %s" % self.air_purifiers_number)
                    print("No more turns left!")
                else:
                    print("Test")
                if len(self.building_queue) > 0:
                    self.currently_building = self.building_queue[0]
                    
                    #self.turns_left_current_building = self.buildings_dict[self.building_queue[0]]
                    self.building_queueStringVar.set(self.building_queue)
                else:
                    self.turns_left_current_building = 0
                    self.building_queueStringVar.set(self.building_queue)
                    print("Building queue empty")
            if self.turns_left > 1:
                self.turns_left -= 1
                self.turns_leftStringVar.set("Turns left: %s" % self.turns_left)
                print("Set turns left to", self.turns_left)
            else:
                self.turns_left = 0
                self.turns_leftStringVar.set("Queue empty")
                print("Set turns left to 0")

    # Logic for saving playername to labels in GUI.    
    def save_playername(self, saved_nameLabel, error_playernameLabel):
        saving_name = str(self.playernameStringVar.get())
        if saving_name != "":
            saved_nameLabel.grid()
            self.saved_playernameStringVar.set(saving_name)
            error_playernameLabel.grid_remove()
        else:
            error_playernameLabel.grid()
            saved_nameLabel.grid_remove()
            
    # Logic for displaying how many turns are left to build the whole building queue.
    def set_turns_left(self, turn_amount = 0):
        self.turns_left += turn_amount
        current_turn = self.turn
        if self.turns_left:
            self.turns_leftStringVar.set("Turns left: %s" % self.turns_left)
            print("Turns left: ", self.turns_left)
            
    # Logic for displaying how many turns are left building the foremost building in the queue.        
    def set_turns_left_current_building(self):
        print(self.building_queue)
        building_queue_index = len(self.building_queue)
        print("Index: %s" % building_queue_index)
        #print(self.building_queue[building_queue_index])
        #print(self.buildings_dict[self.building_queue[len(self.building_queue)]])
        #if len(self.building_queue) > 0:
            #self.turns_left_current_building = self.buildings_dict[self.building_queue[len(self.building_queue)]]
        if len(self.building_queue) > 0:
            self.turns_left_current_building = self.buildings_dict[self.building_queue[0]]
        #else:
            #self.turns_left_current_building = self.buildings_dict[self.buildings_list[0]]
        if self.turns_left_current_building > 0:
            self.turns_left_current_buildingStringVar.set("Turns left for\ncurrent building: %s" % self.turns_left_current_building)
            self.set_turns_left(self.turns_left_current_building)
            self.turns_leftStringVar.set("Turns left: %s" % self.turns_left)
        #else:
            #self.turns_left_current_buildingStringVar.set("Turns left for\ncurrent building: %s" % self.turns_left_current_building)
            
    # Controls what happens when double clicking an item in the building list.
    def add_buildings(self, buildingsListbox):
        selection = buildingsListbox.curselection()
        self.selection_id = int(selection[0])
        if len(selection) == 1:
            self.building_queue.insert(0, "%s" % (self.buildings_list[self.selection_id]))
            #self.currently_building = self.buildings_list[self.selection_id]
            self.currently_building = self.building_queue[0]
            #self.set_turns_left(self.turns_left_current_building)
            self.set_turns_left_current_building()
            self.building_queueStringVar.set(self.building_queue)


   
def main():
    root = Tk()
    app = GUI(root)
    root.mainloop()
    


if __name__ == "__main__":
    main()