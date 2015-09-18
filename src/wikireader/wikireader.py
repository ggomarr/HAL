'''
Created on Sep 12, 2015

@author: ggomarr
'''

import wikipedia
import random
import parameters.wikireader_conf as parameters

class wikireader:
    '''
    Provides modules to interact with wikipedia
    '''
    def __init__(self):
        random.seed()
            
    def retrieve_article(self, search_target):
        try:
            self.title = search_target
            article = wikipedia.summary(search_target)
            self.content = self.process_article(article)
            return True
        except wikipedia.exceptions.PageError:
            self.content = [ ]
            return True
        except wikipedia.exceptions.DisambiguationError as disamb_list:
            disamb_list = [ [ option ] for option in disamb_list.options ]
            if parameters.num_disamb:
                self.content = disamb_list[:parameters.keep_first] + random.sample(disamb_list[parameters.keep_first:], parameters.num_disamb)
            else:
                self.content = disamb_list.options
            return False

    def process_article(self, article):
        try:
            pos_parenthesis = [ article.find('('), article.find(') ') ]
            num_clues = 0
            for clue in parameters.pronunciation_clues:
                num_clues = num_clues + article.count(clue, pos_parenthesis[0],pos_parenthesis[1])
            if pos_parenthesis[0] < parameters.pronunciation_pos and num_clues > parameters.pronunciation_limit:
                article = article[:pos_parenthesis[0]] + article[pos_parenthesis[1]+2:] 
        except:
            pass
        for substitution_rule in parameters.substitutions:
            article = article.replace(substitution_rule[0],substitution_rule[1])
        article = [ [ parag.strip() ] for parag in article.splitlines()]
        return article

if __name__ == "__main__":
    wkp = wikireader()
    wkp.retrieve_article("chernobyl disaster")
    for parag in wkp.content:
        print parag
        
    wkp.retrieve_article("mercury")
    for parag in wkp.content:
        print parag
        
    wkp.retrieve_article("afa4q2gbsq3")
    for parag in wkp.content:
        print parag