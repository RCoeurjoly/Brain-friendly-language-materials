#!/usr/bin/env
# -*- coding: utf-8 -*-
# import uno
# import random
import glob
# import nltk
# import re
import codecs
# import regex
# import string
# import os.path
import numpy as np
# import math
import simple
# import uno
# import ebooklib
from ebooklib import epub
from scipy.optimize import curve_fit
minimalLength = 2000


def fillDataBook(*args):
    i = 0
    thisComponent = XSCRIPTCONTEXT.getDocument()
    oSheet = thisComponent.getCurrentController().getActiveSheet()
    for filename in glob.glob('///home/rcl/Documents/Books/*.txt'):
        print("Analizing book " + filename)
        stripedText = ''.join(c for c in codecs.open(
            filename,
            'r',
            'utf-8-sig',
            'ignore').read() if u'\u4e00' <= c <= u'\u9fff')
        filesize = len(stripedText)
        lexicalVariety = len(set(stripedText))
        '''
        x = np.array([])
        y = np.array([])
        x = np.append(x, minimalLength)
        y = np.append(y, len(set(stripedText[0:minimalLength])))
        x = np.append(x, filesize)
        y = np.append(y, len(set(stripedText[0:filesize])))
        params = curve_fit(simple.fit_log, x, y)
        [a, b] = params[0]
        '''
        try:
            book = epub.read_epub(filename.split('.')[0] + '.epub')
            oSheet.getCellByPosition(0, i).setString(
                book.metadata[
                    'http://purl.org/dc/elements/1.1/']['creator'][0][0])
            oSheet.getCellByPosition(1, i).setString(
                book.title)
        except:
            oSheet.getCellByPosition(1, i).setString(
                filename)
            print ("Epub error")
        ''' oSheet.getCellByPosition(2, i).setValue(
            a)
        oSheet.getCellByPosition(3, i).setValue(
            b)
        '''
        oSheet.getCellByPosition(4, i).setValue(
            filesize)
        oSheet.getCellByPosition(5, i).setValue(
            lexicalVariety)
        oSheet.getCellByPosition(6, i).setString(
            filename)
        i += 1
        print(book.title + "analized")
