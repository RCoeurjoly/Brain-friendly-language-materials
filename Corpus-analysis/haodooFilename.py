#!/usr/bin/env
# -*- coding: utf-8 -*-
# import uno
# import random
import glob
# import nltk
# import re
# import codecs
# import regex
# import string
# import os.path
# import numpy as np
# import math
# import simple
# import uno
# import ebooklib
from ebooklib import epub
# from scipy.optimize import curve_fit
minimalLength = 2000


def fillDataBook(*args):
    i = 0
    thisComponent = XSCRIPTCONTEXT.getDocument()
    oSheet = thisComponent.getCurrentController().getActiveSheet()
    print ("Estoy aqui?")
    for filename in glob.glob('///home/rcl/Documents/Books/*.txt'):
        try:
            print ("O aqui?")
            book = epub.read_epub(filename.split('.')[0] + '.epub')
            oSheet.getCellByPosition(0, i).setString(
                book.metadata[
                    'http://purl.org/dc/elements/1.1/']['creator'][0][0])
            oSheet.getCellByPosition(1, i).setString(
                book.title)
        except:
            print ("llego aqui???")
            oSheet.getCellByPosition(1, i).setString(
                filename)
            print ("Epub error")
        oSheet.getCellByPosition(2, i).setString(
            filename.split('.')[0] + '.epub')
        i += 1
        print(book.title + "analized")
