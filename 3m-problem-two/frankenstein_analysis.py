#!/usr/bin/env python
# coding: utf-8

import nltk
import pandas

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def most_common(textfile,n):
    from nltk import word_tokenize, pos_tag, ne_chunk
    from nltk.corpus import stopwords
    from collections import Counter
    from pandas import DataFrame
    
    # Open file into variable, read contents and convert to lowercase, close file
    f=open(textfile)
    filecontents=f.read().lower()
    f.close()
    
    # Tokenize by lowercase words only, no numbers or non-alphabetic characters like punctuation
    tokenizer=nltk.RegexpTokenizer('[a-z]\w+')
    word_processed=tokenizer.tokenize(filecontents)
    
    # Using NLTK pre-built stopwords list containing most common english stop words like "the", "an", "a", etc. which are not useful for this analysis
    stop_words=set(stopwords.words('english'))
    
    # If words in the text are not in the list of stop words then only include those words in the list of meaningful words, going word by word through the entire text
    words_filtered=[word for word in word_processed if word not in stop_words]
    
    # Build a set based on the filtered words list above so that we can know which meaningful words are in the text and separate that feature from frequency of the words occuring in the text
    unique_words=set(words_filtered)

    # Use counter function to create a dictionary of each word in the filtered list and the count of the number of times those words appeared in the text
    count=Counter(words_filtered)
    out=count.most_common(n)
    text_length=len(words_filtered) # only meaningful words needed for frequency analysis
        
    # Calculate percentage that the most common words occur among the entire text after the text has been processed to remove stop words, numbers, and punctuation in order to only include meaningful words in the analysis
    freq=[]
    i=0
    while i<n:
        calc=100 * (out[i][1]) / text_length
        out[i]=out[i] + (str(round(calc,2)),)
        i+=1    

    # Output neat table of results
    df=DataFrame(out,columns=['Word','Count','Percentage of text (%)'],index=[list(range(1,n+1))])
    
    return {'df':df, "unique words":unique_words}

# Return (1) count of most common words and (2) breakdown of part of speech tags for unique words in the processed set of words from the text (which includes only meaningful words)
from nltk import pos_tag, ne_chunk

output=most_common("84-0.txt",5)
print(f'{output.get("df")}')

unique_words=output.get("unique words")
pos_tag(unique_words)

