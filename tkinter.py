from datetime import datetime
from Tkinter import *
from ttk import *


class Init():
    def __init__(self, Main, GameLogic):
        Main()
        GameLogic()
    
    
    
class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.gamelogic = GameLogic()
        
        self.buildingsListbox = Listbox(self, height = 13, listvariable = self.gamelogic.buildingsStringVar)
        self.saved_nameLabel = Label(self, textvariable = self.gamelogic.saved_playernameStringVar)
        self.error_playernameLabel = Label(self, foreground = "red", text = "Invalid name!")
        
        self.UI_configuration()
    
        
    def initUI(self):
        self.parent.title("Gametest")
        self.pack(fill = BOTH, expand = True)
        self.centerWindow()
        
        
    def centerWindow(self):
        w = 640
        h = 480
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        
    
    def add_buildings(self, buildingsListbox):
        self.gamelogic.add_buildings(self.buildingsListbox)
        
        
    def save_playername(self, saved_nameLabel, error_playernameLabel):
        self.gamelogic.save_playername(self.saved_nameLabel, self.error_playernameLabel)
        
        
    def UI_configuration(self):
        #time_leftMethod = time_left
        
        
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
        
        self.rowconfigure(0, pad = 3)
        self.rowconfigure(1, pad = 3)
        self.rowconfigure(2, pad = 20)
        self.rowconfigure(3, pad = 3)
        self.rowconfigure(4, pad = 3)
        self.rowconfigure(5, pad = 3)
        self.rowconfigure(6, pad = 3)

        
        #Creating UI elements and setting their parameters.
        self.style = Style()
        self.style.theme_use("default")
        Style().configure("TButton", padding = (0, 2, 0, 0), font = "TkFixedFont")
        
        add_buildingsLabel = Label(self, text = "Add building")
        nameentry = Entry(self, textvariable = self.gamelogic.playernameStringVar)
        nameentry.focus()
        button1 = Button(self, text = "Save name", command = self.gamelogic.save_playername)
        button2 = Button(self, text = "Button 2")
        button3 = Button(self, text = "Build house", command = self.gamelogic.add_buildings)
        button4 = Button(self, text = "End turn", command = self.gamelogic.run_simulation)
        button5 = Button(self, text = "time_left")
        button5.grid(row = 9, column = 7)
        quitButton = Button(self, text = "Quit", command = self.quit)
        
        
        resources = Labelframe(self, text = "Resources", labelanchor = "nw", width = 150, height = 100)
        buildingsLabelframe = Labelframe(self, text = "Buildings", width = 100, height = 200)
        #time_leftLabel = Label(self, textvariable = time_leftStringVar)
        turns_leftLabel = Label(self, textvariable = self.gamelogic.turns_leftStringVar)
        
        housesLabel = Label(self, textvariable = self.gamelogic.houses_numberStringVar)
        turnLabel = Label(self, textvariable = self.gamelogic.turn_numberStringVar)
        building_queueListbox = Listbox(self, height = 5, listvariable = self.gamelogic.building_queueStringVar)
        #building_queueStringVar.set(self.building_queue)
        
        #Binding actions to elements.
        #Double-1 means double left click.
        self.buildingsListbox.bind("<Double-1>", self.add_buildings)
        
        #Placement of UI elements on the grid.
        self.grid(sticky = N + S + W + E)
        
        add_buildingsLabel.grid(row = 0, column = 0, sticky = S)
        nameentry.grid(row = 9, column = 0, sticky = W)
        button1.grid(row = 9, column = 1)
        button2.grid(row = 9, column = 2)
        button3.grid(row = 9, column = 3)
        button4.grid(row = 9, column = 4)
        quitButton.grid(row = 9, column = 8, sticky = E)
        
        self.buildingsListbox.grid(row = 1, column = 0, sticky = W)
        #resources.grid(row = 0, column = 8, sticky = W)
        buildingsLabelframe.grid(row = 1, column = 8, sticky = W)
        housesLabel.grid(row = 1, column = 8, sticky = W)
        turnLabel.grid(row = 0, column = 8, sticky = E)
        self.saved_nameLabel.grid(row = 8, column = 0, sticky = W)
        self.error_playernameLabel.grid(row = 8, column = 0, sticky = W)
        self.error_playernameLabel.grid_remove()
        building_queueListbox.grid(row = 2, column = 0, sticky = W)
        #time_leftLabel.grid(row = 2, column = 1, sticky = W)
        turns_leftLabel.grid(row = 3, column = 0, sticky = W)
        emptylabel = Label(self, text = "")
        emptylabel.grid(row = 2, column = 8)
   
        

class GameLogic():
    def __init__(self):
        #self.parent = parent
        self.turn = 0
        self.turns_left = 0
        self.houses = 0
        self.House = 0
        self.buildings_names = ""
        self.building_queue = ""
        self.currently_building = ["Placeholder building", 0]
        self.buildings_list = sorted(["Air purifier", "Water purifier", "House", "Robot factory"])
        
        self.saved_playernameStringVar = StringVar()
        self.playernameStringVar = StringVar()
        self.turn_numberStringVar = StringVar()
        self.turn_numberStringVar.set("Turn %s" % self.turn)
        
        self.houses_numberStringVar = StringVar()
        self.buildingsStringVar = StringVar()
        self.building_queueStringVar = StringVar()
        self.time_leftStringVar = StringVar()
        self.turns_leftStringVar = StringVar()
        
        self.set_buildings()
        
    
    
    #buildings_names = self.buildings_names
    

    #buildings_dict = {}
    def set_houses(self):
        self.houses_numberStringVar.set("Houses: %s" % self.houses)
    
    
    def set_buildings(self):
        for name in self.buildings_list:
            #buildings_dict[buildings_list.index(name)] = name
            self.buildings_names += "{%s}\n" % name
        self.buildingsStringVar.set(self.buildings_names)

        
    def run_simulation(self):
        if self.turn < 50:
            self.turn += 1
            self.turn_numberStringVar.set("Turn %s" % self.turn)
            print "Turn", self.turn
            if self.turns_left > 1:
                self.turns_left -= 1
                print "Turns left: ", self.turns_left
                self.turns_leftStringVar.set(self.turns_left)
                print "Set turns left to", self.turns_leftStringVar.get()
            elif self.turns_left == 1:
                self.turns_left = 0
                self.turns_leftStringVar.set("Built %s" % self.currently_building[0])
                #print "%s" % type(self[self.currently_building])
                #self[self.currently_building[1]] = 1
                self.currently_building[1] += 1
                self.houses_numberStringVar.set("%ss: %s" % (self.currently_building[0], self.currently_building[1]))
                print "No more turns left!"
        
    def save_playername(self, saved_nameLabel, error_playernameLabel):
        saving_name = str(self.playernameStringVar.get())
        if saving_name != "":
            saved_nameLabel.grid()
            self.saved_playernameStringVar.set(saving_name)
            error_playernameLabel.grid_remove()
        else:
            error_playername.grid()
            saved_name.grid_remove()
                
    def set_turns_left(self, turn_amount = 0):
        self.turns_left = turn_amount
        current_turn = self.turn
        if self.turns_left != 0:
            self.turns_leftStringVar.set(self.turns_left)
            print "Turns left: ", self.turns_leftStringVar.get()

    def add_buildings(self, buildingsListbox):
        selection = buildingsListbox.curselection()
        selection_id = int(selection[0])
        if len(selection) == 1:
            #print buildings_list[selection_id]
            #print "buildings_list index: %s" % buildings_list.index(buildings_list[selection_id])
            self.building_queue += "{%s}\n" % (self.buildings_list[selection_id])
            self.currently_building[0] = self.buildings_list[selection_id]
            if self.buildings_list[selection_id] == "House":
                #self.building_queue += "{%s}\n" % (buildings_list[selection_id])
                self.building_queueStringVar.set(self.building_queue)
                self.set_turns_left(5)
                #saved_playername.set("Building %s" % buildings_list[selection_id])
            elif self.buildings_list[selection_id] == "Air purifier":
                #self.building_queue += "{%s}\n" % (buildings_list[selection_id])
                self.building_queueStringVar.set(self.building_queue)
                self.set_turns_left(6)
            #print self.building_queue


   
def main():
    root = Tk()
    app = GUI(root)
    root.mainloop()
    


if __name__ == "__main__":
    main()
