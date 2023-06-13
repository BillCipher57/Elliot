import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.font as tkFont
import os

Version = "YOURMum"
class App:
    def __init__(self, root):
        #setting title
        root.title(f"Hacksir - Elliot - Release {Version}")
        #setting window size
        width=1000
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        StartIPBox = Text(root, bd=1, bg="black", fg="#01aaed")#, text="Starting IP")
        StartIPBox.place(x=30,y=60,width=124,height=60)

        SnifferBox=tk.Button(root)
        SnifferBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        SnifferBox["font"] = ft
        SnifferBox["fg"] = "#000000"
        SnifferBox["justify"] = "center"
        SnifferBox["text"] = "Hostname Sniffer"
        SnifferBox.place(x=30,y=20,width=124,height=30)
        SnifferBox["command"] = self.SnifferBox_command

        FloodBox=tk.Button(root)
        FloodBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        FloodBox["font"] = ft
        FloodBox["fg"] = "#000000"
        FloodBox["justify"] = "center"
        FloodBox["text"] = "Syn Flood"
        FloodBox.place(x=180,y=20,width=124,height=30)
        FloodBox["command"] = self.FloodBox_command

        TargetIP=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Target IP")
        TargetIP.place(x=180,y=60,width=124,height=60)

        ChromeButton=tk.Button(root)
        ChromeButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        ChromeButton["font"] = ft
        ChromeButton["fg"] = "#000000"
        ChromeButton["justify"] = "center"
        ChromeButton["text"] = "Chrome Password Detector"
        ChromeButton.place(x=620,y=20,width=124,height=30)
        ChromeButton["command"] = self.ChromeButton_command

        EndingIPBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Ending IP")
        EndingIPBox.place(x=30,y=130,width=124,height=60)

        TargetPortBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Target Port")
        TargetPortBox.place(x=180,y=130,width=123,height=60)

        PasswordStrengthBox=tk.Button(root)
        PasswordStrengthBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        PasswordStrengthBox["font"] = ft
        PasswordStrengthBox["fg"] = "#000000"
        PasswordStrengthBox["justify"] = "center"
        PasswordStrengthBox["text"] = "Password Strength"
        PasswordStrengthBox.place(x=330,y=20,width=124,height=30)
        PasswordStrengthBox["command"] = self.PasswordStrengthBox_command

        UserPasswordBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Your password")
        UserPasswordBox.place(x=330,y=60,width=124,height=60)

        PasswordStrengthOutput=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Password Strength")
        PasswordStrengthOutput.place(x=330,y=130,width=126,height=60)

        IPLookupBox=tk.Button(root)
        IPLookupBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        IPLookupBox["font"] = ft
        IPLookupBox["fg"] = "#000000"
        IPLookupBox["justify"] = "center"
        IPLookupBox["text"] = "IP Lookup"
        IPLookupBox.place(x=480,y=20,width=124,height=30)
        IPLookupBox["command"] = self.IPLookupBox_command

        IPInputBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="The IP")
        IPInputBox.place(x=480,y=60,width=124,height=60)

        DetailsBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Details")
        DetailsBox.place(x=480,y=130,width=124,height=252)

        AIChatBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="AI Chatlog")
        AIChatBox.place(x=770,y=60,width=217,height=269)

        SpeechInputBox=tk.Button(root)
        SpeechInputBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        SpeechInputBox["font"] = ft
        SpeechInputBox["fg"] = "#000000"
        SpeechInputBox["justify"] = "center"
        SpeechInputBox["text"] = "Speech Input"
        SpeechInputBox.place(x=770,y=340,width=100,height=40)
        SpeechInputBox["command"] = self.SpeechInputBox_command

        TextInputBox=tk.Button(root)
        TextInputBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        TextInputBox["font"] = ft
        TextInputBox["fg"] = "#000000"
        TextInputBox["justify"] = "center"
        TextInputBox["text"] = "Text Input"
        TextInputBox.place(x=890,y=340,width=100,height=40)
        TextInputBox["command"] = self.TextInputBox_command

        OutputBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Output")
        OutputBox.place(x=620,y=60,width=120,height=323)

        AnotherOutputBox=Text(root, bd=1, bg="black", fg="#01aaed")#, text="Output")
        AnotherOutputBox.place(x=30,y=220,width=423,height=56)

        InstallDependenciesBox=tk.Button(root)
        InstallDependenciesBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        InstallDependenciesBox["font"] = ft
        InstallDependenciesBox["fg"] = "#000000"
        InstallDependenciesBox["justify"] = "center"
        InstallDependenciesBox["text"] = "Install Dependencies"
        InstallDependenciesBox.place(x=30,y=310,width=124,height=30)
        InstallDependenciesBox["command"] = self.InstallDependenciesBox_command

        RebootBox=tk.Button(root)
        RebootBox["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        RebootBox["font"] = ft
        RebootBox["fg"] = "#000000"
        RebootBox["justify"] = "center"
        RebootBox["text"] = "Reboot"
        RebootBox.place(x=180,y=310,width=124,height=30)
        RebootBox["command"] = self.RebootBox_command

        GithubButton=tk.Button(root)
        GithubButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=14)
        GithubButton["font"] = ft
        GithubButton["fg"] = "#000000"
        GithubButton["justify"] = "center"
        GithubButton["text"] = "Visit Github"
        GithubButton.place(x=330,y=310,width=124,height=30)
        GithubButton["command"] = self.GithubButton_command

        GLabel_221=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=14)
        GLabel_221["font"] = ft
        GLabel_221["fg"] = "#333333"
        GLabel_221["justify"] = "center"
        GLabel_221["text"] = "Hacksir created by DKZhifty - please visit the original repository. This is a downgraded version created by Sanware."
        GLabel_221.place(x=30,y=350,width=421,height=30)

    def SnifferBox_command(self):
        print("command")
        os.system("python3 HostnameSniffer.py")


    def FloodBox_command(self):
        print("command")
        os.system("python3 SynFlooding.py")


    def ChromeButton_command(self):
        print("command")
        os.system("python3 ChromePassExtractor.py")


    def PasswordStrengthBox_command(self):
        print("command")
        os.system("python3 PasswordStrength.py")


    def IPLookupBox_command(self):
        print("command")
        os.system("python3 Iplookup.py")


    def SpeechInputBox_command(self):
        print("command")
        VoiceCommand()



    def TextInputBox_command(self):
        print("command")
        SendCommand()


    def InstallDependenciesBox_command(self):
        print("command")
        os.system("python3 -m pip install -r requirements")


    def RebootBox_command(self):
        print("command")
        sys.exit()


    def GithubButton_command(self):
        print("command")
        webbrowser.open("")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
