# MiniProject_Frontend.py
from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

class Movie:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="black")

        Movie_Name = StringVar()
        Movie_ID = StringVar()
        Release_Date = StringVar()
        Director = StringVar()
        Cast = StringVar()
        Budget = StringVar()
        Duration = StringVar()
        Rating = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
            if iExit:
                root.destroy()

        def clcdata():
            self.txtMovie_ID.delete(0, END)
            self.txtMovie_Name.delete(0, END)
            self.txtRelease_Date.delete(0, END)
            self.txtDirector.delete(0, END)
            self.txtCast.delete(0, END)
            self.txtBudget.delete(0, END)
            self.txtRating.delete(0, END)
            self.txtDuration.delete(0, END)

        def adddata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get())
                MovieList.delete(0, END)
                MovieList.insert(END, (Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()))

        def disdata():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.ViewMovieData():
                MovieList.insert(END, row)

        def movierec(event):
            global sd
            index = MovieList.curselection()
            if not index:
                return
            searchmovie = index[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[1])
            self.txtMovie_Name.delete(0, END)
            self.txtMovie_Name.insert(END, sd[2])
            self.txtRelease_Date.delete(0, END)
            self.txtRelease_Date.insert(END, sd[3])
            self.txtDirector.delete(0, END)
            self.txtDirector.insert(END, sd[4])
            self.txtCast.delete(0, END)
            self.txtCast.insert(END, sd[5])
            self.txtBudget.delete(0, END)
            self.txtBudget.insert(END, sd[6])
            self.txtDuration.delete(0, END)
            self.txtDuration.insert(END, sd[7])
            self.txtRating.delete(0, END)
            self.txtRating.insert(END, sd[8])

        def deldata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.DeleteMovieRec(sd[0])
                clcdata()
                disdata()

        def searchdb():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.SearchMovieData(Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()):
                MovieList.insert(END, row)

        def updata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.UpdateMovieData(sd[0], Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get())
                disdata()

        # GUI Layout
        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        TFrame.pack(side=TOP)
        Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE MOVIE TICKET BOOKING SYSTEM", bg="black", fg="orange").grid()

        BFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Info", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Details", fg="white")
        DFrameR.pack(side=RIGHT)

        # Labels and Entry Boxes
        labels = ["Movie ID", "Movie Name", "Release Date", "Director", "Cast", "Budget (INR)", "Duration (hrs)", "Rating"]
        vars = [Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating]
        entries = []

        for i, (label, var) in enumerate(zip(labels, vars)):
            Label(DFrameL, font=('Arial', 18, 'bold'), text=label + ":", padx=2, pady=2, bg="black", fg="orange").grid(row=i, column=0, sticky=W)
            entry = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=var, width=39, bg="black", fg="white")
            entry.grid(row=i, column=1)
            entries.append(entry)

        (self.txtMovie_ID, self.txtMovie_Name, self.txtRelease_Date,
         self.txtDirector, self.txtCast, self.txtBudget, self.txtDuration,
         self.txtRating) = entries

        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        sb.config(command=MovieList.yview)

        # Buttons
        buttons = [
            ("Add New", adddata),
            ("Display", disdata),
            ("Clear", clcdata),
            ("Search", searchdb),
            ("Delete", deldata),
            ("Update", updata),
            ("Exit", iExit)
        ]
        for i, (text, cmd) in enumerate(buttons):
            Button(BFrame, text=text, font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=cmd).grid(row=0, column=i)

if __name__ == '__main__':
    root = Tk()
    database = Movie(root)
    root.mainloop()
