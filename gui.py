from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        """Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()

    def playFood(self):
        top = Toplevel()
        top.title("Restaurant Menu")
        Label(top, text = "WELCOME TO CHEYRENNE'S BAKERY!"
              ).grid(row=0,column=0,columnspan =5, sticky = W)
        Label(top,text = "Cake Flavors (24 cupcakes or 1/4 sheet cake):          Qty."
              ).grid(row=2,column=0,columnspan=4,sticky = W)
        
        # vanilla flavor checkbutton
        top.is_vanilla = BooleanVar()
        Checkbutton(top,
                    text = "Vanilla",
                    variable = top.is_vanilla
                    ).grid(row = 3, column = 1, sticky = W)
        van = Label(top, text="$12.00").grid(row=3,column=2)
        top.van_ent = Entry(top,width=3)
        top.van_ent.grid(row = 3, column = 3)
        
        # chocolate flavor
        top.is_choc = BooleanVar()
        Checkbutton(top,
                    text = "Chocolate",
                    variable = top.is_choc
                    ).grid(row = 4, column = 1, sticky = W)
        choc = Label(top, text="$14.00").grid(row=4,column=2)
        top.choc_ent = Entry(top,width=3)
        top.choc_ent.grid(row = 4, column = 3)
        
        # marble flavor
        top.is_marble = BooleanVar()
        Checkbutton(top,
                    text = "Marble",
                    variable = top.is_marble
                    ).grid(row = 5, column = 1, sticky = W)
        marb = Label(top, text="$14.00").grid(row=5,column=2)
        top.marb_ent = Entry(top,width=3)
        top.marb_ent.grid(row = 5, column = 3)

        # fudge flavor
        top.is_fudge = BooleanVar()
        Checkbutton(top,
                    text = "Fudge",
                    variable = top.is_fudge
                    ).grid(row = 6, column = 1, sticky = W)
        fudge = Label(top, text="$16.00").grid(row=6,column=2)
        top.fudge_ent = Entry(top,width=3)
        top.fudge_ent.grid(row = 6, column = 3)

        #Fillings and Frostings
        Label(top,text = "Fillings").grid(row=8,column=0,sticky = W)
        fillings = ["strawberry", "fudge", "raspberry","lemon","none"]
        column = 0
        top.filling = StringVar()
        top.filling.set(None)
        for fill in fillings:
            Radiobutton(top,
                        text = fill,
                        variable = top.filling,
                        value = fill
                        ).grid(row = 9, column = column, sticky = W)
            column += 1

        Label(top,text = "Frostings").grid(row =10,column=0,sticky = W)
        top.frosting = StringVar()
        top.frosting.set(None)
        frostings = ["Strawberry","Mint","Vanilla","Cream cheese","Ganache"]
        column = 0
        for frost in frostings:
            Radiobutton(top,text = frost,variable = top.frosting,
                        value = frost
                        ).grid(row=11,column = column,sticky = W)
            column +=1
        Button(top, text = "Calculate Cost",
               command = lambda: self.Calc(top)).grid(row=13,column=0)
        Button(top, text = "Quit", command = top.destroy).grid(row=13,column=5)

    def Calc(self,top):
        cost =0
        # cost of cake flavor
        if top.is_fudge.get():
            try:        #in case user leaves Qty box empty
                cost += 8*int(top.fudge_ent.get())
            except ValueError:
                cost +=8
        if top.is_vanilla.get():
            try:
                cost += 8*int(top.van_ent.get())
            except ValueError:
                cost +=8
        if top.is_choc.get():
            try:
                cost += 8 *int(top.choc_ent.get())
            except ValueError:
                cost +=8
        if top.is_marble.get():
            try:
                cost += 8* int(top.marb_ent.get())
            except ValueError:
                cost+=8
                
        # cost of filling choice
        filling = top.filling.get()
        if filling == "strawberry":
            cost += 10
        elif filling == "fudge":
            cost +=3
        elif filling == "rasperry":
            cost += 10
        elif filling == "lemon":
            cost +=7
        elif filling == "none":
            cost +=0
            
        # cost of frosting choice
        frosting = top.frosting.get()
        if top.frosting == "Strawberry" or top.frosting =="Mint":
            cost +=4
        elif top.frosting == "Cream cheese":
            cost +=6
        elif top.frosting == "Ganache":
            cost+=8
        Label(top, text="Cost: " + str(cost)).grid(row=13,column=1)

    def playWord(self):
       # self.grid()
        top = Toplevel()
        top.title("Number Guess")
        label = Label(top, text = "I'm thinking of a number between 1 and 100.")
        label.grid(row=0,column=0,columnspan = 3,sticky = W)
        label1 = Label(top, text ="Try to guess it in as few attempts as possible.")
        label1.grid(row=1,column=0,columnspan =3,sticky = W)
        
        top.rand_Num = random.randint(1,100)
        top.guess = Entry(top,text = "Take a guess:",width=20)
        top.guess.grid(row=2,column=0)
        Button(top, text = "Guess",
               command = lambda: self.is_correct(top)
               ).grid(row=2,column=1, sticky = W)

        Button(top, text = "Quit",command = top.destroy).grid(row = 3,column = 3,sticky=W)



    def is_correct(self,top):
        guess = top.guess.get()
        correct = int(guess)
        label_2 = Label(top, text = "Lower...")
        label_3 = Label(top,text = "Higher...")
        if correct == top.rand_Num:
            label_2.grid_forget()
            label_3.grid_forget()
            label_1 = Label(top, text = "CORRECT! " +top.guess.get()+" was the number!")
            label_1.grid(row=4,column=0, columnspan = 2)
        if correct > top.rand_Num:
            label_2.grid(row=3,column=0)
        elif correct < top.rand_Num:
            label_3.grid(row=3,column=0)
            
        
    def playLib(self):
        top = Toplevel()
        top.title("Mad Lib")
       # self.grid()
        Label(top,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name of a person
        Label(top,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)
        top.person_ent = Entry(top)
        top.person_ent.grid(row = 1, column = 1, sticky = W)

        # create a label and text entry for a plural noun
        Label(top,
              text = "Plural Noun:"
              ).grid(row = 2, column = 0, sticky = W)
        top.noun_ent = Entry(top)
        top.noun_ent.grid(row = 2, column = 1, sticky = W)

        # create a label and text entry for a verb
        Label(top,
              text = "Verb:"
              ).grid(row = 3, column = 0, sticky = W)
        top.verb_ent = Entry(top)
        top.verb_ent.grid(row = 3, column = 1, sticky = W)
     
        # create a label for adjectives check buttons
        Label(top,
              text = "Adjective(s):"
              ).grid(row = 4, column = 0, sticky = W)

        # create itchy check button
        top.is_itchy = BooleanVar()
        Checkbutton(top,
                    text = "itchy",
                    variable = top.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        # create joyous check button
        top.is_joyous = BooleanVar()
        Checkbutton(top,
                    text = "joyous",
                    variable = top.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)

        # create electric check button
        top.is_electric = BooleanVar()
        Checkbutton(top,
                    text = "electric",
                    variable = top.is_electric
                    ).grid(row = 4, column = 3, sticky = W)

        # create a label for body parts radio buttons
        Label(top,
              text = "Body Part:"
              ).grid(row = 5, column = 0, sticky = W)

        # create variable for single, body part
        top.body_part = StringVar()
        top.body_part.set(None)
  
        # create body part radio buttons
        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            Radiobutton(top,
                        text = part,
                        variable = top.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        # create a submit button
        Button(top,
               text = "Click for story",
               command = lambda: self.tell_story(top)
               ).grid(row = 6, column = 0, sticky = W)

        top.story_txt = Text(top, width = 75, height = 10, wrap = WORD)
        top.story_txt.grid(row = 7, column = 0, columnspan = 4)
        Button(top,
               text = "Quit",
               command =  top.destroy
               ).grid(row =8,column=0,sticky = W)

    def tell_story(self,top):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = top.person_ent.get()
        noun = top.noun_ent.get()
        verb = top.verb_ent.get()
        adjectives = ""
        if top.is_itchy.get():
            adjectives += "itchy, "
        if top.is_joyous.get():
            adjectives += "joyous, "
        if top.is_electric.get():
            adjectives += "electric, "
        body_part = top.body_part.get()

        # create the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
        
        # display the story                                
        top.story_txt.delete(0.0, END)
        top.story_txt.insert(0.0, story)

                

#create root window
root = Tk()
root.title("Which Game?")
root.geometry("500x500+200+200")
app = Application(root)
label = Label(root, text = "Which game would you like to play?"
                ).grid(row = 0, column = 0)
b = Button(root, text = "MadLib", command = app.playLib)
b.grid(row=1,column=0,sticky = W)
b4 = Button(root,text = "Restaurant", command = app.playFood)
b4.grid(row=1,column=0)
b2 = Button(root,text = "Guess My Number", command = app.playWord)
b2.grid(row=1,column = 1)
b3 = Button(root, text = "Quit", command = root.destroy).grid(row=1,column=2)



# start root window event loop
root.mainloop()
