#!/usr/bin/python3
# encoding: utf-8
#———————————————————————————————————————————————————————IMPORTS—————————————————————————————————————————————————————————

from tkinter import *
from threading import Thread
import gd

#———————————————————————————————————————————————————————GLOBAL VARS—————————————————————————————————————————————————————————

global lvlEditEnabled, InfJumpEnabled, LvlCopyEnabled, NoclipEnabled, CustObjBypassEnabled, ObjBypassEnabled, percAccurateEnabled

lvlEditEnabled = False
InfJumpEnabled = False
LvlCopyEnabled = True
NoclipEnabled = False
CustObjBypassEnabled = False
ObjBypassEnabled = False
percAccurateEnabled = False

#———————————————————————————————————————————————————————FUNCTIONS—————————————————————————————————————————————————————————

def WaitGD():
    global memory

    memory = None

    while True:
        try:
            memory = gd.memory.get_memory()
            break
        except:
            pass

    opengd.config(text="Now you can enable/disable hacks", font=("Trebuchet MS", 14))

    anticheatEnabled.pack(side=TOP, pady=5)
    accuratePercBtn.pack(side=TOP, pady=5)
    lvlEdit.pack(side=TOP, pady=5)
    InfJumpBtn.pack(side=TOP, pady=5)
    LvlCopyBtn.pack(side=TOP, pady=5)
    NoclipBtn.pack(side=TOP, pady=5)

    memory.enable_anticheat()
    memory.enable_level_copy()
    memory.enable_object_limit()
    memory.enable_custom_object_limit()
    memory.enable_practice_song()

def AccuratePerc():
    memory.enable_accurate_percent()

def LvlEdit():
    global lvlEditEnabled

    if lvlEditEnabled:
        memory.disable_level_edit()
        lvlEditEnabled = False
        lvlEdit.config(text="Enable Level Edit")
    else:
        memory.enable_level_edit()
        lvlEditEnabled = True
        lvlEdit.config(text="Disable Level Edit")

def InfJump():
    global InfJumpEnabled

    if InfJumpEnabled:
        memory.disable_inf_jump()
        InfJumpEnabled = False
        InfJumpBtn.config(text="Enable Infinite Jump")
    else:
        memory.enable_inf_jump()
        InfJumpEnabled = True
        InfJumpBtn.config(text="Disable Infinite Jump")

def LvlCopy():
    global LvlCopyEnabled

    if LvlCopyEnabled:
        memory.disable_level_copy()
        LvlCopyEnabled = False
        LvlCopyBtn.config(text="Enable Level Copy")
    else:
        memory.enable_level_copy()
        LvlCopyEnabled = True
        LvlCopyBtn.config(text="Disable Level Copy")

def Noclip():
    global NoclipEnabled

    if NoclipEnabled:
        memory.disable_noclip()
        NoclipEnabled = False
        NoclipBtn.config(text="Enable NoClip(safe)")
    else:
        memory.enable_noclip()
        NoclipEnabled = True
        NoclipBtn.config(text="Disable NoClip")

#disable acc perc

#———————————————————————————————————————————————————————MAIN PART—————————————————————————————————————————————————————————

root = Tk()

root.title('Geometry Dash Mod Menu v1.0')
root.geometry('300x600')

opengd = Label(root, text="Please open Geometry Dash!", font=("Trebuchet MS", 17))
opengd.pack(side=TOP)

anticheatEnabled = Label(root, text="Anticheat,\nLevel Copy,\nObject Bypass,\nCustom Object Bypass,\nPractice Music Hack\nare enabled by default", font=("Trebuchet MS", 12))
anticheatEnabled.pack(side=TOP)

accuratePercBtn = Button(text="Enable Accurate Percentage", command=AccuratePerc, height=1, width=40)
accuratePercBtn.pack(side=TOP, pady=5)

lvlEdit = Button(text="Enable Level Edit", command=LvlEdit, height=1, width=40)
lvlEdit.pack(side=TOP, pady=5)

InfJumpBtn = Button(text="Enable Infinite Jump", command=InfJump, height=1, width=40)
InfJumpBtn.pack(side=TOP, pady=5)

LvlCopyBtn = Button(text="Disable Level Copy", command=LvlCopy, height=1, width=40)
LvlCopyBtn.pack(side=TOP, pady=5)

NoclipBtn = Button(text="Enable NoClip(safe)", command=Noclip, height=1, width=40)
NoclipBtn.pack(side=TOP, pady=5)

#Hiding all the elements
anticheatEnabled.pack_forget()
accuratePercBtn.pack_forget()
lvlEdit.pack_forget()
InfJumpBtn.pack_forget()
LvlCopyBtn.pack_forget()
NoclipBtn.pack_forget()

Thread(target=WaitGD).start()

root.mainloop()
