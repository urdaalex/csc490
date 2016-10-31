import sys
import os
import cPickle as pickle
import simplejson
from gensim.models import Word2Vec as w2v

'''
Notes on the implementation
    - This program will take as input the directory with the
    preprocessed JSON files (generated by preprocessor.py)
    and will create a new directory with the feature vectors
    generated from the paragraphs in each JSON file (each article
    will have its own feature vector). The feature vectors
    are constructed using the feature extraction method specified
    by the input flag -method, where
        -method in {-word2vec, -doc2vec, -customfeatures}
    The -word2vec option will give a word2vec factoring of the
    paragraphs of each JSON file, the -doc2vec factoring will give a
    doc2vec factoring of the entire JSON document file (the paragraphs
    concatenated), and -customfeatures will generate a feature vector
    with features we've determined would be relevant a priori.

    - NOTE: If we have time, I would suggest that for the -customfeatures
    option, we generate more features than we think are relevant, then use
    mRMR to keep the important ones.
'''

def getWord2Vec(JSON_files):
    '''
    Given a list of JSON files that have been parsed and preprocessed, this
    function returns a list of each document (the concatenation
    of all the paragraphs in each JSON files) converted to word2vec.
    '''
    # Get a list of all the documents
    all_documents = []
    for json in JSON_files:
        paragraphs = json['paragraphs']
        document = ''
        for i in paragraphs[:-1]:
            document += i + "\n\n"
        document += paragraphs[-1]
        all_documents.append(document)


    # Generate the model, the number of words/characters in the vocabulary
    # will be the number of unique words in the txt_list.
    model = w2v(all_documents,
                min_count = len(set([i for i in [j for j in txt_list]])),
                size = 100,
                workers = 4)
    return model

def isValid(input_args):
    '''
    Given the list of input arguments, this function will return a boolean
    indicating whether or not the inputs are valid
    '''
    proper_usage = "Input Error: One or more of the following is causing an issue\n" +\
                "\t 1) Too few or too many inputs \n" +\
                "\t 2) The input directory doesn't exist\n" +\
                "\t 3) The output directory already exists\n" +\
                "\t 4) The specified method is not one of: \n" +\
                "\t\t '-word2vec' or '-doc2vec' or '-customfeatures'\n" +\
                "\t Correct usage: \n" +\
                "\t\t python generate-featurevectors.py 'input_dir_name' 'output_dir_name' -method"

    if len(input_args) != 3 or os.path.exists(input_args[1]) \
                or not os.path.exists(input_args[0]) or \
                input_args[2] not in ['-word2vec', '-doc2vec', '-customfeatures']:
        print proper_usage
        return False

    return True

def main(argv):
    '''
    Given the array of arguments to the program, the main method will ensure
    that the inputs are valid, if they are, the JSON files in the input
    directory will be loaded, and transformed to feature vectors
    using the method specified by the -method flag . The feature vectors of the
    JSON files will then be saved to the output directory specified by the
    input arguments as .pickle files.
    '''
    # Check that the input arguments are valid
    if not isValid(argv):
        sys.exit(1)

    # Load a list of the JSON files in the input dir
    JSON_files = []
    for filename in os.listdir(argv[0]):
        with open(os.path.join(argv[0], filename) 'r') as json_file:
            JSON_files.append(simplejson.load(json_file))

    # Get the feature vectors of the JSON files using the method
    # specified in the input
    if (argv[2] == '-word2vec'):
        model = getWord2Vec(JSON_files)



if __name__ == "__main__":
    main(sys.argv[1:])
