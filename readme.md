## Dependencies

1. pip install --upgrade google-api-python-client
2. pip install BeautifulSoup
3. pip install simplejson
4. pip install nltk
    - **NOTE**: this won't download stop words, to get them you need to
        go into the python shell and run the following commands
        </br> `import nltk` </br>
        `nltk.download()` </br>
        This will open a new prompt window (the *NLTK Downloader*), in that window, go to the
        *Corpora* tab, and scroll down to stopwords (the identifier is *stopwords*, the corpus name is *Stopwords Corpus*), that's the one you want to download.
5. pip install --upgrade gensim
6. pip install cPickle
7. Download and untar Stanford Parser `http://nlp.stanford.edu/software/lex-parser.shtml`


## Usage
```
search-google.py QUERY [FOLDER_NAME]
```
* saves search results to json file: {url: "", content: ""}

```
categorize-results.py FOLDER_NAME
```
* takes all results in folder and opens URL in browser for you to categorize website (note: folder must have been create by search-google.py)

```
categorize-stats.py FOLDER_NAME
```
* takes all results in folder and prints out stats in the form of Expected V W; Got X Accredit, Y False, Z Unrelated

```
parser.py -method [INPUT_FOLDER_NAME] [OUTPUT_FOLDER_NAME]
```
* Iterates over all of the result files in the input folder, parses them to extract the text contents, and saves the results in the output folder. Note that a new folder is created within the output folder for each query. method can either be tag or regex.The format of the output files is: {'title': '', 'query': '', 'paragraphs': [], 'links': [], 'authors': []}

```
preprocessor.py [INPUT_FOLDER_NAME] [OUTPUT_FOLDER_NAME]
```
* This program will iterate over the JSON files produced by parser.py in the specified
input directory, and will process the paragraphs in the JSON files. The new processed
JSON data will get written to the specified output folder in the same format
as parser.py

```
Dependency.py 
```
* #USAGE:

 compare_pages(txt1,txt2)
     txt1: string of sentences seperated by newline characters.
     txt2: string of sentences sperated by new line characters

---------
   
RETURNS:
	For every conflicting sentence (in the other document):

  

CONFLICT!:
  		
<b>Sentence 1: </b> `furthermore, there are literally hundreds of independent studies that prove vaccines cause autism.`

<b>Sentence 2: </b> `vaccines do not cause autism.`

CONFLICT!:

<b>Sentence 1: </b> `there is absolutely undeniable scientific proof that vaccines cause autism.`

<b>Sentence 2: </b> `vaccines do not cause autism.`

---------


