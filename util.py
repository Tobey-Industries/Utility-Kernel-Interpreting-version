import                            colorama
import                            os
import                            platform
import                            socket
from   cryptography.fernet import Fernet
from   playsound           import playsound
from   tkinter             import *
import                            time
os.system("TITLE Utility Kernel 0.3.0")
original_print = print
mode = "gui"
if mode == "gui":
    applet_main = Tk()
    applet_main.config(background='white')
    applet_main.geometry("800x600")
    def print(self, fg):
        with open("hibernate.util", "ab")as f: f.write(bytes(self, encoding = "utf8"))
        Label(applet_main, text=self, bg="white", fg=fg).pack()
else:
      def print(self):
        with open("hibernate.util", "ab")as f: f.write(bytes(self, encoding = "utf8"))
        original_print(self)
def env(self): return os.environ[self]
if mode == "tui":
   print(f"""
{colorama.Fore.GREEN}UTILITY KERNEL is starting...
{colorama.Fore.YELLOW}
Info:
{colorama.Fore.WHITE}
[{colorama.Fore.YELLOW}INFO{colorama.Fore.WHITE}] Reporting {platform.platform()}""")
if mode == "gui": 
   print("UTILITY KERNEL is starting...", "green")
osutildir = env("APPDATA")+"\\..\\LocalLow\\osutil"
logfile = f"{osutildir}\\{socket.gethostname()}.txt"
logpl = logfile
clock = time.strftime('%B-%d-%Y %I:%M %p')



def error(desc, function):
  log(logpl, f"\n--Potted error--\nDescription: {desc}\nFunction: {function}\n")
  ws = Tk()
  ws.config(background="white")
  ws.title('Attention')
  img = PhotoImage(file="C:\\Users\\Omar Ismail\\AppData\\LocalLow\\osutil\\Error.png")
  Label(ws, image=img).pack(side = LEFT)
  Label(ws, text="The command done an illegal operation and was shut down.\nReinstalling this feature may help.", font="Cascadia 10", foreground="red", background="white").pack(side = RIGHT)
  Button(ws, text="OK",command=ws.destroy, font="Cascadia 5").pack(side=BOTTOM)
  root = ws
  root.geometry("1024x768")
  scrollbar = Scrollbar(root)
  scrollbar.pack( side = RIGHT, fill = Y )
  mylist = Listbox(root, yscrollcommand = scrollbar.set, width=70)
  mylist.insert(END, 'Debug Info: ')
  mylist.insert(END, 'Device: '+socket.gethostname())
  mylist.insert(END, 'Device IP: '+socket.gethostbyname(socket.gethostname()))
  mylist.insert(END, 'Kernel: '+os.name)
  mylist.insert(END, 'Function: '+function)
  mylist.insert(END, 'Error Description:hib '+desc)
  mylist.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = mylist.yview )
  ws.mainloop()
def log(logfile, info):
  try:
    with open(logfile, "a")as f: f.write("\n"+clock+"|"+info)
  except UnicodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(clock, encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except UnicodeEncodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(clock, encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except FileNotFoundError: 
    if mode == "gui":Label(applet_main, text= "--LogFile Error--\nThe system cannot find the path specified.").pack()
    else:print("--LogFile Error--\nThe system cannot find the path specified.")


os.chdir(osutildir)
import turtle
def execute(task):
  if mode == "tui":
     print(f"{colorama.Fore.YELLOW}---UTILITY KERNEL Ver. 0.3.0---\nPowered by Python{colorama.Fore.GREEN}")
     turt = False
     linen = 0
     file = open(task, "r").readlines()
     for line in file:
       linen = linen + 1
       if line[0:5] == "print": 
         if line[5:9] == "!tit": os.system("title Utility Kernel 0.3.0 - "+input(line[9:int(len(line))]))
         elif line[5:9] == "!col": os.system("color "+input(line[9:int(len(line))]))
         elif line[5:9] == "!ech": print("UTILITY Kernel: "+input(line[9:int(len(line))]))
         else: print("UTILITY Kernel: "+line[5:int(len(line))])
       elif line[0:5] == "color": os.system("color "+line[5:int(len(line))])
       elif line[0:3] == "red": print(colorama.Fore.RED)
       elif line[0:5] == "green": print(colorama.Fore.GREEN)
       elif line[0:4] == "blue": print(colorama.Fore.BLUE)
       elif line[0:5] == "white": print(colorama.Fore.WHITE)
       elif line[0:5] == "title": os.system("title Utility Kernel 0.3.0 - "+line[5:int(len(line))])
       elif line[0:8] == "turtlefd":
         if turt: turtle_obj.fd(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.fd(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlebk":
         if turt: turtle_obj.bk(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.bk(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlelt":
         if turt: turtle_obj.lt(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.lt(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlert":
         if turt: turtle_obj.rt(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.rt(int(line[8:int(len(line))])) 
       else: 
        print(f"[{colorama.Fore.MAGENTA}ERROR{colorama.Fore.GREEN}] in line {linen} in file {task}")
  if mode == "gui":
     Label(applet_main, text= "---UTILITY KERNEL Ver. 0.3.0---\nPowered by Python", fg="yellow")
     turt = False
     linen = 0
     file = open(task, "r").readlines()
     for line in file:
       linen = linen + 1
       if line[0:5] == "print": 
         Label(applet_main, text="UTILITY Kernel: "+line[5:int(len(line))], fg = "green").pack()
       elif line[0:5] == "color": os.system("color "+line[5:int(len(line))])
       elif line[0:5] == "title": applet_main.title("Utility Kernel 0.3.0 - "+line[5:int(len(line))])
       elif line[0:8] == "turtlefd":
         if turt: turtle_obj.fd(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.fd(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlebk":
         if turt: turtle_obj.bk(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.bk(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlelt":
         if turt: turtle_obj.lt(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.lt(int(line[8:int(len(line))]))
       elif line[0:8] == "turtlert":
         if turt: turtle_obj.rt(int(line[8:int(len(line))]))
         else:
           turt = True
           turtle_obj = turtle.Turtle()
           turtle_obj.rt(int(line[8:int(len(line))])) 
       else: 
        print(f"[ERROR] in line {linen} in file {task}","purple")
  
    
def checkfile(self, dir):
    for file in self:
        if os.path.exists(file): 
          if mode == "tui": print(f"[{colorama.Fore.GREEN}OK{colorama.Fore.WHITE}] {file} exists")
          if mode == "gui": print(f"[OK] {file} exists ", "green")
        else: 
           error(f"File {self} in directory {dir} doesn't exist", "UTILITY KERNEL")
           if mode == "tui": print(f"{colorama.Fore.RED}Killing Program...{colorama.Fore.WHITE}")
           if mode == "gui": print(f"Killing Program...", "red")
           exit()

if mode == "gui": print(f"[OK] Execute command and system base products initiation", "green")
else: print(f"[{colorama.Fore.GREEN}OK{colorama.Fore.WHITE}] Execute command and system base products initiation")
checkfile(["autoexec.util", "hibernate.util", "krnlfeed.util", "sysusers.txt", "bootsound.sys", "secbootsound.sys"], osutildir)
if mode != "gui": print(f"[{colorama.Fore.GREEN}OK{colorama.Fore.WHITE}] ALL files are put properly")
else: print(f"[OK] ALL files are put properly", "green")
if mode != "gui":print(f"[{colorama.Fore.GREEN}OK{colorama.Fore.WHITE}] The kernel is cleared to run")
else: print(f"[OK] The kernel is cleared to run", "green")
if mode != "gui":print(f"[{colorama.Fore.YELLOW}INFO{colorama.Fore.WHITE}] The autoexec and kernel feed are going to be ran. Starting <execute> and <os.system>...")
else: print(f"[INFO] The autoexec and kernel feed are going to be ran. Starting <execute> and <os.system>...", "yellow")
for line in open("autoexec.util").readlines(): 
   if mode != "gui":print(f"[{colorama.Fore.YELLOW}INFO{colorama.Fore.WHITE}] Running command: {line}")
   else: print(f"[INFO] Running command: {line}", "yellow")
   os.system(line)
for line in open("krnlfeed.util").readlines(): 
   if mode != "gui": print(f"[{colorama.Fore.YELLOW}INFO{colorama.Fore.WHITE}] Executing file: {line}")
   else: print(f"[INFO] Executing file: {line}", "yellow")
   execute(line)
if mode != "gui": print(colorama.Fore.WHITE)
if mode == "tui": os.system("pause")
if mode == "gui": applet_main.mainloop()