from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize,pos_tag
stopwords = stopwords.words('english')
import math
import re

def remove_punctuation(words):
    new_list= []
    for w in words:
        if w.isalnum():
            new_list.append( w )
    return new_list


def remove_punctuation_and_stopwords(words):
    new_list= []
    for w in words:
        if w.isalnum() and w not in stopwords:
            new_list.append( w )
    return new_list


# +
def concordance_word( text, regex , width = 10 ):

    concordance = []
    distance = math.floor( width /2 )

    segment_length = 0

    words = word_tokenize( text )
    words = remove_punctuation( words )
    i = 0
    for w in words:
        if re.search( regex , w , re.IGNORECASE ):
            match = ''
            for x in range( i - distance , ( i + distance ) + 1 ):
                if x >= 0 and x < len(words):
                    if len(words[x]) >= 0:
                        match += words[x] + ' '
            concordance.append( match )

        i += 1

    return concordance





def collocation( text , regex , width ):

    freq_c = dict()
    distance = math.floor(width/2)

    sentences = sent_tokenize( text )

    for sentence in sentences:

        words = word_tokenize( sentence )
        words = remove_punctuation_and_stopwords(words)

        for i,w in enumerate(words):
            if re.search( regex , w , re.IGNORECASE ):

                index_regex = i 

                for x in range( i - distance , i + distance ):
                    if x >= 0 and x < len(words) and words[x].lower() != words[index_regex].lower():
                        if len(words[x]) > 0:
                            word = words[x].lower()
                            freq_c[ word ] = freq_c.get( word , 0 ) + 1
            
    return freq_c


def sorted_by_value( dict , ascending = True ):
    if ascending: 
        return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    else:
        return {k: v for k, v in reversed( sorted(dict.items(), key=lambda item: item[1]))}




def cooccurrence( text , word1 , word2 , width ):
    
    relevant_sentences = []
    
    text = re.sub( '\s+' , ' ' , text )
    sentences = sent_tokenize( text )

    for s in sentences:
        if re.search( r'\b' + word1 + r'\b' , s , re.IGNORECASE ) and re.search( r'\b' + word2 + r'\b' , s , re.IGNORECASE ):

            words = word_tokenize(s)
            word1_indexes = []
            word2_indexes = []
            
            for i,w in enumerate(words):
                if re.search( r'\b' + word1 + r'\b' , w , re.IGNORECASE ):
                    word1_indexes.append(i)
                elif re.search( r'\b' + word2 + r'\b' , w , re.IGNORECASE ):
                    word2_indexes.append(i)

            if word1_indexes[0] > word2_indexes[0]:
                difference = word1_indexes[0] - word2_indexes[0]
            else:
                difference = word2_indexes[0] - word1_indexes[0]

            if difference <= width:
                relevant_sentences.append(s)
    return relevant_sentences



def ptb_to_wordnet(PTT):

    if PTT.startswith('J'):
        ## Adjective
        return 'a'
    elif PTT.startswith('V'):
        ## Verb
        return 'v'
    elif PTT.startswith('N'):
        ## Noune
        return 'n'
    elif PTT.startswith('R'):
        ## Adverb
        return 'r'
    else:
        return ''    


upenn_code = { "CC":"conjunction, coordinating",
"CD":"numeral, cardinal",
"DT":"determiner",
"EX":"existential there",
"FW":"foreign word",
"IN":"preposition or conjunction, subordinating",
"JJ":"adjective or numeral, ordinal",
"JJR":"adjective, comparative",
"JJS":"adjective, superlative",
"LS":"list item marker",
"MD":"modal auxiliary",
"NN":"noun, common, singular or mass",
"NNP":"noun, proper, singular",
"NNPS":"noun, proper, plural",
"NNS":"noun, common, plural",
"PDT":"pre-determiner",
"POS":"genitive marker",
"PRP":"pronoun, personal",
"PRP$":"pronoun, possessive",
"RB":"adverb",
"RBR":"adverb, comparative",
"RBS":"adverb, superlative",
"RP":"particle",
"SYM":"symbol",
"TO":"to as preposition or infinitive marker",
"UH":"interjection",
"VB":"verb, base form",
"VBD":"verb, past tense",
"VBG":"verb, present participle or gerund",
"VBN":"verb, past participle",
"VBP":"verb, present tense, not 3rd person singular",
"VBZ":"verb, present tense, 3rd person singular",
"WDT":"WH-determiner",
"WP":"WH-pronoun",
"WP$":"WH-pronoun, possessive",
"WRB":"Wh-adverb" }





