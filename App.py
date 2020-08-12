import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Desktop Ui")
        self.geometry("1920x1080+0+0")
        self.configure(background = "#2C2C2C" )
        taskBarFrame = tk.Frame(self,bg="#3A3E46",height=60,width=1920)
        taskBarFrame.pack(side=tk.TOP,fill='both')
        frameInBarFrame = tk.Frame(taskBarFrame,bg="#3A3E46",height=60)
        frameInBarFrame.place(in_=taskBarFrame, anchor="c", relx=.5, rely=.5)
        #the different labels on taskbar

        self.Dashboard = tk.Label(frameInBarFrame,text="Dashboard",font=('Roboto', 20, 'bold'),fg = '#FCB415' , bg = "#3A3E46")
        self.Dashboard.grid(row =0 , column =0,pady=10,sticky='news',padx=8)
        self.Dashboard.bind("<Button-1>",self.dashboard_labeld_cliked)
        
        self.Activity = tk.Label(frameInBarFrame,text="Activity",font=('Roboto', 20, 'bold'),fg = 'white' , bg = "#3A3E46")
        self.Activity.grid(row =0 , column =1,pady=10,sticky='news',padx=8)
        self.Activity.bind("<Button-1>",self.activity_labeld_cliked)
        
        self.Badges = tk.Label(frameInBarFrame,text="Badges",font=('Roboto', 20, 'bold'),fg = 'white' , bg = "#3A3E46")
        self.Badges.grid(row =0 , column =2,pady=10,sticky='news',padx=8)
        self.Badges.bind("<Button-1>",self.badges_labeld_cliked)
        
        self.Calender = tk.Label(frameInBarFrame,text="Calender",font=('Roboto', 20, 'bold'),fg = 'white' , bg = "#3A3E46")
        self.Calender.grid(row =0 , column =3,pady=10,sticky='news',padx=8)
        self.Calender.bind("<Button-1>",self.calender_labeld_cliked)
        
        self.Connection = tk.Label(frameInBarFrame,text="Connection",font=('Roboto', 20, 'bold'),fg = 'white' , bg = "#3A3E46")
        self.Connection.grid(row =0 , column =4,pady=10,sticky='news',padx=8)
        self.Connection.bind("<Button-1>",self.connection_labeld_cliked)
        
        self.Devices = tk.Label(frameInBarFrame,text="Devices",font=('Roboto', 20, 'bold'),fg = 'white' , bg = "#3A3E46")
        self.Devices.grid(row =0 , column =5,pady=10,sticky='news',padx=8)
        self.Devices.bind("<Button-1>",self.devices_labeld_cliked)

    
    def dashboard_labeld_cliked(self,event):
        self.Dashboard.config(fg="#FCB415")
        self.Activity.config(fg="white")
        self.Badges.config(fg="white")
        self.Calender.config(fg="white")
        self.Connection.config(fg="white")
        self.Devices.config(fg="white")
    
    def activity_labeld_cliked(self,event):
        self.Dashboard.config(fg="white")
        self.Activity.config(fg="#FCB415")
        self.Badges.config(fg="white")
        self.Calender.config(fg="white")
        self.Connection.config(fg="white")
        self.Devices.config(fg="white")
    
    def badges_labeld_cliked(self,event):
        self.Dashboard.config(fg="white")
        self.Activity.config(fg="white")
        self.Badges.config(fg="#FCB415")
        self.Calender.config(fg="white")
        self.Connection.config(fg="white")
        self.Devices.config(fg="white")
    
    def calender_labeld_cliked(self,event):
        self.Dashboard.config(fg="white")
        self.Activity.config(fg="white")
        self.Badges.config(fg="white")
        self.Calender.config(fg="#FCB415")
        self.Connection.config(fg="white")
        self.Devices.config(fg="white")
    
    def connection_labeld_cliked(self,event):
        self.Dashboard.config(fg="white")
        self.Activity.config(fg="white")
        self.Badges.config(fg="white")
        self.Calender.config(fg="white")
        self.Connection.config(fg="#FCB415")
        self.Devices.config(fg="white")
    
    def devices_labeld_cliked(self,event):
        self.Dashboard.config(fg="white")
        self.Activity.config(fg="white")
        self.Badges.config(fg="white")
        self.Calender.config(fg="white")
        self.Connection.config(fg="white")
        self.Devices.config(fg="#FCB415")









        

        







if __name__ == "__main__":
    app = App()
    app.mainloop()
        
    