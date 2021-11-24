import copy  
from typing import Dict, List, TextIO

from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END, 
                       NameType, ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '031': {
        ID: '031',
        TITLE: 'Calculus is the Best Course Ever',
        CREATED: '',
        MODIFIED: '2021-09-02',
        AUTHORS: [('Breuss', 'Nataliya')],
        ABSTRACT: 'We discuss the reasons why Calculus is the best course.'},
    '067': {
        ID: '067',
        TITLE: 'Discrete Mathematics is the Best Course Ever',
        CREATED: '2021-09-02',
        MODIFIED: '2021-10-01',
        AUTHORS: [('Pancer', 'Richard'), ('Bretscher', 'Anna')],
        ABSTRACT: ('We explain why Discrete Mathematics is the best ' +
                   'course of all times.')},
    '827': {
        ID: '827',
        TITLE: 'University of Toronto is the Best University',
        CREATED: '2021-08-20',
        MODIFIED: '2021-10-02',
        AUTHORS: [('Ponce', 'Marcelo'), ('Bretscher', 'Anna'), 
                  ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We show a formal proof that the University of\n' +
        'Toronto is the best university.'},
    '008': {
        ID: '008',
        TITLE: 'Intro to CS is the Best Course Ever',
        CREATED: '2021-09-01',
        MODIFIED: '',
        AUTHORS: [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Science is the best course.'},    
    '042': {
        ID: '042',
        TITLE: '',
        CREATED: '2021-05-04',
        MODIFIED: '2021-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}
################################## DONT TOUCH ####################

def clean_word(word: str) -> str:
    """Return word with all non-alphabetic characters removed and converted to 
    lowercase.
    
    Precondition: word contains no whitespace
    
    >>> clean_word('Hello!!!')
    'hello'
    >>> clean_word('12cat.dog?')
    'catdog'
    >>> clean_word("DON'T")
    'dont'
    """
    new_word = ''
    for ch in word:
        if ch.isalpha():
            new_word = new_word + ch.lower()
    return new_word

def created_in_year(ArxivType, art_id, art_year) -> bool:
    """Return True if and only if an article with the id art_id occurs in the 
    metadata ArxivType and was published in the year art_year. 
    """

def contains_keyword(ArxivType, word_to_search) -> List[str]:
    """Return a list of the IDs of articles that contain the keyword 
    word_to_search in their title and/or abstract. 
    """
    search_word = clean_word(word_to_search)
    return_list = []
    for ids in ArxivType:
        for keys in ArxivType[ids]:
            if word_to_search in ArxivType[ids][keys] and\
                keys == 'title'or keys == 'abstarct'and ids not in return_list: 
                    return_list.append(ids)
        return_list.sort()
    return return_list