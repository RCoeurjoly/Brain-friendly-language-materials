# Brain-friendly-language-materials

**_This is a work in progress._**

## PURPOSE
The purpose of this project is to make learning a new language easier by applying the Comprehension Hypothesis, introduced by Stephen Krashen. 

## STRUCTURE
The project is going to be divided in two parts:
* Narrated stories
* List of books ranked by readability

## ADDITIONAL MATERIALS
Supporting those two parts, a range of materials will be available.
For the narrated stories:
* Techniques and strategies that are conducive to comprehensible and compelling language materials.

Some of these are:

* Strict control of vocabulary (introduction of new words),
* Use of pictures,
* Circling questioning, etc

For the list of books: 
* theory, readability measures implemented in Python and some graphs

The scripts have been used as LibreOffice macros. Also, as of now, they can only process txt files. 

## INSPIRATION
The inspiration for this project come from books like Lingua Latina per se illustrata, a book for learning Latin that doesn't contain a single word in any other language.
One extremely important feature of that kind of book is that it is suitable for native-speakers of whatever language.
Other projects from which we draw inspiration are:

* TPR (Total Physical Response)
* TPRS (Total Physical Response Storytelling or alternatively Teaching Proficiency through Reading and Storytelling)
* ALG (Automatic Language Growth)

## STATUS
At the moment, to analyze a corpus, you have to follow a cumbersome process:
* Download a bunch of books, preferably in epub format
* Convert them to plain text (using scripts found in this repo)
** This can take up to one week (tested in 4G RAM laptop)
* Open a LibreOffice spreadsheet
* Execute macros (found in this repo)


## TODO

* Find public domain stories, better if they are written in several languages (parallel texts)
** https://www.grimmstories.com/
* Find the minimum amount of words needed to begin reading the easiest books in the corpus
* Modify the scripts to work with epub files. Find a library to do so.
* Create the plots with gnuplot.
* Create the scripts to download the corpora.
··* Torify them to protect the users.
* Add links to inspiring projects.
* Maybe separate the language materials from the corpus analysis?
** Possible name for corpus: Metatron
