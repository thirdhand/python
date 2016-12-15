import time
from datetime import datetime
from Tkinter import *
from ttk import *
#from PIL import Image, ImageTk



class Main(Frame):
    turn = 0
    turns_left = 0
    houses = 0
    buildings_names = ""
    building_queue = ""
    currently_building = ["Placeholder building", 0]
    
    
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        #self.initVars()
        self.content()
        
        
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
        
        
    def content(self):
        saved_playername = StringVar()
        playername = StringVar()
        turn_number = StringVar()
        turn_number.set("Turn %s" % self.turn)
        
        houses_number = StringVar()
        buildings = StringVar()
        building_queueStringVar = StringVar()
        time_leftStringVar = StringVar()
        turns_leftStringVar = StringVar()
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
           
        
        #frame1 = Frame(self, bg = "red")
        #frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = N + S + W + E)
        
        
        buildings_names = self.buildings_names
        buildings_list = ["Air purifier", "Water purifier", "House", "Robot factory"]
        buildings_list = sorted(buildings_list)
        #buildings_dict = {}
        for name in buildings_list:
            #buildings_dict[buildings_list.index(name)] = name
            buildings_names += "{%s}\n" % name
        buildings.set(buildings_names)
        
        
        emptylabel = Label(self, text = "")
        emptylabel.grid(row = 2, column = 8)
        
        def run_simulation():
            if self.turn < 25:
                self.turn += 1
                turn_number.set("Turn %s" % self.turn)
                print "Turn", self.turn
                if self.turns_left > 1:
                    self.turns_left -= 1
                    print "Turns left: ", self.turns_left
                    turns_leftStringVar.set(self.turns_left)
                    print "Set turns left to", turns_leftStringVar.get()
                elif self.turns_left == 1:
                    self.turns_left = 0
                    turns_leftStringVar.set("Built %s" % self.currently_building[0])
                    self.currently_building[1] += 1
                    houses_number.set("%ss: %s" % (self.currently_building[0], self.currently_building[1]))
                    print "No more turns left!"
        
        def save_playername(*args):
            saving_name = str(playername.get())
            if saving_name != "":
                saved_name.grid()
                saved_playername.set(saving_name)
                error_playername.grid_remove()
            else:
                error_playername.grid()
                saved_name.grid_remove()
                
        #def time_left(seconds):
            #seconds_left = []
            #while seconds:
                ##time_leftStringVar.set(seconds)
                ##print time_leftStringVar.get()
                #building_queueStringVar.set(self.building_queue)
                ##time.sleep(1)
                #sec_from_epoch = int(round(time.time() * 1000000))
                #str_sec_from_epoch = str(sec_from_epoch)[8:10]
                #if str_sec_from_epoch not in seconds_left:
                    #seconds_left.append(str_sec_from_epoch)
            
                ##print sec_from_epoch
                #time_leftStringVar.set(str_sec_from_epoch)
                ##print str_sec_from_epoch
                ##print time.time()
                ##print seconds
                #seconds -= 1
            #print seconds_left
            ##time_leftStringVar.set(0)
            #print "Finished"
            #return str_sec_from_epoch

        def set_turns_left(turn_amount = 0):
            self.turns_left = turn_amount
            current_turn = self.turn
            if self.turns_left != 0:
                turns_leftStringVar.set(self.turns_left)
                print "Turns left: ", turns_leftStringVar.get()

        def add_buildings(*args):
            selection = buildingsListbox.curselection()
            selection_id = int(selection[0])
            if len(selection) == 1:
                #print buildings_list[selection_id]
                #print "buildings_list index: %s" % buildings_list.index(buildings_list[selection_id])
                self.building_queue += "{%s}\n" % (buildings_list[selection_id])
                self.currently_building[0] = buildings_list[selection_id]
                if buildings_list[selection_id] == "House":
                    #self.building_queue += "{%s}\n" % (buildings_list[selection_id])
                    building_queueStringVar.set(self.building_queue)
                    set_turns_left(5)
                    #saved_playername.set("Building %s" % buildings_list[selection_id])
                elif buildings_list[selection_id] == "Air purifier":
                    #self.building_queue += "{%s}\n" % (buildings_list[selection_id])
                    building_queueStringVar.set(self.building_queue)
                    set_turns_left(6)
                #print self.building_queue
                
        #def set_time_left():
            #time_leftStringVar.set(time_left(100))
            #print time_leftStringVar.get()
        
        #print time_left(3)
        
        #Creating UI elements and setting their parameters.
        self.style = Style()
        self.style.theme_use("default")
        Style().configure("TButton", padding = (0, 2, 0, 0), font = "TkFixedFont")
        
        add_buildingsLabel = Label(self, text = "Add building")
        nameentry = Entry(self, textvariable = playername)
        nameentry.focus()
        button1 = Button(self, text = "Save name", command = save_playername)
        button2 = Button(self, text = "Button 2")
        button3 = Button(self, text = "Build house", command = add_buildings)
        button4 = Button(self, text = "End turn", command = run_simulation)
        button5 = Button(self, text = "time_left", command = add_buildings)
        button5.grid(row = 9, column = 7)
        quitButton = Button(self, text = "Quit", command = self.quit)
        
        buildingsListbox = Listbox(self, height = 13, listvariable = buildings)
        resources = Labelframe(self, text = "Resources", labelanchor = "nw", width = 150, height = 100)
        buildingsLabelframe = Labelframe(self, text = "Buildings", width = 100, height = 200)
        #time_leftLabel = Label(self, textvariable = time_leftStringVar)
        turns_leftLabel = Label(self, textvariable = turns_leftStringVar)
        
        houses_number.set("Houses: %s" % self.houses)
        housesLabel = Label(self, textvariable = houses_number)
        turnLabel = Label(self, textvariable = turn_number)
        error_playername = Label(self, foreground = "red", text = "Invalid name!")
        saved_name = Label(self, textvariable = saved_playername)
        building_queueListbox = Listbox(self, height = 5, listvariable = building_queueStringVar)
        #building_queueStringVar.set(self.building_queue)
        
        #Binding actions to elements.
        #Double-1 means double left click.
        buildingsListbox.bind("<Double-1>", add_buildings)
        
        #Placement of UI elements on the grid.
        self.grid(sticky = N + S + W + E)
        
        add_buildingsLabel.grid(row = 0, column = 0, sticky = S)
        nameentry.grid(row = 9, column = 0, sticky = W)
        button1.grid(row = 9, column = 1)
        button2.grid(row = 9, column = 2)
        button3.grid(row = 9, column = 3)
        button4.grid(row = 9, column = 4)
        quitButton.grid(row = 9, column = 8, sticky = E)
        
        buildingsListbox.grid(row = 1, column = 0, sticky = W)
        #resources.grid(row = 0, column = 8, sticky = W)
        buildingsLabelframe.grid(row = 1, column = 8, sticky = W)
        housesLabel.grid(row = 1, column = 8, sticky = W)
        turnLabel.grid(row = 0, column = 8, sticky = E)
        error_playername.grid(row = 8, column = 0, sticky = W)
        error_playername.grid_remove()
        saved_name.grid(row = 8, column = 0, sticky = W)
        building_queueListbox.grid(row = 2, column = 0, sticky = W)
        #time_leftLabel.grid(row = 2, column = 1, sticky = W)
        turns_leftLabel.grid(row = 3, column = 0, sticky = W)
   
        
   
def main():
    root = Tk()
    app = Main(root)
    root.mainloop()
#def time_left(seconds):
    #seconds_left = []
    #while seconds:
        #Main.content.building_queueStringVar.set(self.building_queue)
        #sec_from_epoch = int(round(time.time() * 1000000))
        #str_sec_from_epoch = str(sec_from_epoch)[8:10]
        #if str_sec_from_epoch not in seconds_left:
            #seconds_left.append(str_sec_from_epoch)
            #time_leftStringVar.set(str_sec_from_epoch)
            #seconds -= 1
    


if __name__ == "__main__":
    main()
