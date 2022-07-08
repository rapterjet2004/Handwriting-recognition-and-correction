import tkinter as tk
from tkinter import *
from tkinter import filedialog
from turtle import bgcolor
from PIL import ImageTk, Image
from test_handwriting import Handwriting
from autocorrect import Speller
from wordsearcher import WordSearcher

class App(tk.Tk):
    
    def __init__(self) -> None:
        """
        sets up the window and frames that hold the image and text
        """
        super().__init__()
        frame = Frame(self)
        frame.pack(side = LEFT, fill="both")
        button = Button(frame, padx=20, pady=20, relief=FLAT, text="upload", command=self.tempFunc, bg="#47c462")
        button.pack()

        self.frame1 = tk.Frame(self)
        self.frame1.pack(side=LEFT, fill="both")

        self.frame2 = Frame(self)
        self.frame2.pack(side=LEFT, fill="both")


    def uploadButton(event) -> str:
        """
        Uploads the file for the model to run on. Returns a string made from
        the list of characters detected by the model

        Args:
            event : action event on the button

        Returns:
            str: string made up of characters detected in image
        """
        filepath = filedialog.askopenfilename()
        print(filepath)
        try:
            im = Image.open(filepath)
            im.save("images/myimage.png")
            handwriting_tested = Handwriting()
            word = "".join(handwriting_tested.predictedChars)
            return word
        except OSError:
            print(OSError)
    
    def tempFunc(self):
        """
        used as a temporary function to call the showImage() and showText() functions
        """
        word = self.uploadButton()
        self.showImage()
        self.showText(word)
    
    def showImage(self):
        """
        Shows the original image, overlayed with the bounding boxes and predicted characters
        """
        try:
            image1 = Image.open("images/edited.png")
            test = ImageTk.PhotoImage(image1)
        except IOError:
            print(IOError)

        label1 = tk.Label(self.frame1, image=test)
        label1.image = test
        label1.pack()
        
    
    def showText(self, word) -> None:
        """
        Shows the original string and it's corrected form

        Args:
            word (str): the string of characters detected in the model

        """
        labelTxt = ""
        search = WordSearcher()
        if search.binarySearchWords(word): # if word exists return true
            labelTxt = word + " -> " + word
        else:  # else, correct it using autocorrect
            spell = Speller()
            corrected = spell(word)
            labelTxt = word + " -> " + corrected
        
        label = tk.Label(self.frame2, text=labelTxt, font= ('Aerial', 17))
        label.pack()
    


    
