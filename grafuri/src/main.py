'''
Created on Mar 15, 2017

@author: Raul
'''

from define import DoubleDictGraph
from defineFile import defineFile
from UserInterface import UI

graf=defineFile()

uiCtrl=UI(graf)
uiCtrl.menu()