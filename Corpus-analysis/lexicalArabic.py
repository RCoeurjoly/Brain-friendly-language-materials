#!/usr/bin/env
# -*- coding: utf-8 -*-
# import uno
# import random
import os
import nltk
import nltk.tokenize
# import re
import codecs
# import regex
# import string
# import os.path
import numpy as np
# import math
import simpleWestern
# import uno
# import ebooklib
import scipy
from ebooklib import epub
from scipy.optimize import curve_fit


def fillDataBook(*args):
    i = 0
    minimalLength = 80000
    thisComponent = XSCRIPTCONTEXT.getDocument()
    oSheet = thisComponent.getCurrentController().getActiveSheet()
    path = "/home/rcl/Downloads/Arabic"
    for dirpath, dirnames, files in os.walk(path):
        for filename in files:
            if filename.endswith('.txt'):
                print("Analizing:     " + filename)
                stripedText = codecs.open(
                    str("//" + dirpath + "/" + filename),
                    'r',
                    'utf-8-sig',
                    'ignore').read()
                tokens = nltk.tokenize.word_tokenize(stripedText)
                filesize = len(tokens)
                lexicalVariety = len(set(tokens))
                # Fitting log-log regression
                x = np.array([])
                y = np.array([])
                x = np.append(x, minimalLength)
                y = np.append(y, np.log(len(set(tokens[0:minimalLength]))))
                x = np.append(x, filesize)
                y = np.append(y, np.log(len(set(tokens[0:filesize]))))
                print(simpleWestern.__file__)
                print(scipy.__file__)
                params = curve_fit(simpleWestern.fit_log, x, y)
                [a, b] = params[0]
                fullfilename = str("//" + dirpath + "/" + filename)
                # Sometimes epub are badly formatted
                try:
                    book = epub.read_epub(fullfilename.split('.')[0] + '.epub')
                    oSheet.getCellByPosition(0, i).setString(
                        book.metadata[
                            'http://purl.org/dc/elements/1.1/'][
                                'creator'][0][0])
                    oSheet.getCellByPosition(1, i).setString(
                        book.title)
                    print(book.title + " analized")
                except:
                    print ("Epub error")
                oSheet.getCellByPosition(2, i).setValue(
                    a)
                oSheet.getCellByPosition(3, i).setValue(
                    b)
                oSheet.getCellByPosition(4, i).setValue(
                    filesize)
                oSheet.getCellByPosition(5, i).setValue(
                    lexicalVariety)
                oSheet.getCellByPosition(6, i).setString(
                    fullfilename)
                i += 1
