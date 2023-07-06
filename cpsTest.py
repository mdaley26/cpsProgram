from tkinter import *
from threading import Timer

class cpsTest:
    #initialize the variables
    def __init__(self, time):
        self.time = time
        self.window = Tk()
        self.window.geometry("800x600")
        self.clicks, self.turn, self.attempt = 0, 0, 0
        self.clickerButton = Button(self.window, text="<-- Click Here To Start -->", padx=200, pady=100, command=self.run)
        self.clock = Timer(self.time, self.cps)
        self.clickerButton.pack()

    # start the test and add clicks
    def run(self):
        if self.turn == 1:
            self.clicks += 1
            self.clickerButton["text"] = str(self.clicks)
        if self.turn == 0:
            self.clock.start()
            self.turn = 1
            self.clicks += 1
            self.clickerButton["text"] = str(self.clicks)

    # once the time is up, display the CPS
    def cps(self):
        self.output = Entry(self.window)
        self.attempt += 1
        self.clickerButton["text"] = "<-- Click Here To Start -->"
        self.output.insert(END, str(self.attempt) + ". ""CPS: " + str(self.clicks/self.time))
        self.turn, self.clicks = 0, 0
        self.clock.cancel()
        self.clock = Timer(self.time, self.cps)
        self.output.pack()

# run the program
app = cpsTest(10)
app.window.mainloop()
