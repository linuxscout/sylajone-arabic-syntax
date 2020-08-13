#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        anasyn
# Purpose:     Arabic syntax analyser, 
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     13-12-2017
# Copyright:   (c) Taha Zerrouki 2017
# Licence:     GPL
#-------------------------------------------------------------------------------
"""
Cache system for extrcat features for words relations.
"""
if __name__=="__main__":
    import sys
    sys.path.append('../');
    sys.path.append('../../support/');

import sys
import os
import pickledb
from pyarabic.arabrepr import arepr


class cache :
    """
        cache for word morphological analysis
    """
    def __init__(self, dp_path = False):
        """
        Create Analex Cache
        """
        # used for words
        self.cache = {}
        DB_PATH = os.path.join(os.path.expanduser('~'), '.thaalabCache.pickledb')
        if not dp_path:
            dp_path = DB_PATH
        else:
            dp_path = os.path.join(os.path.dirname(dp_path), '.thaalabCache.pickledb')
        #~ self.db =  pickledb.load(dp_path, False)
        try:
            self.db =  pickledb.load(dp_path, False)
        except:
            print("Can't Open data base", dp_path)
            self.db = None
    def __del__(self):
        """
        Delete instance and clear cache

        """
        self.cache = None
        if self.db:
            self.db.dump()
    def update(self):
        """update data base """
        #~ pass
        for word in self.cache:
            self.add_checked(word, self.cache[word])        
    def is_already_checked(self, word):
        """ return if ``word`` is already cached"""
        try:
            return bool(self.db.get(word))
        except:
            return False
        #~ except: return False;

    def get_checked(self, word):
        """ return checked ``word`` form cache"""
        #~ word = bytes(word, "utf-8")
        result = []
        if self.db:
            result = self.db.get(word)
        
        return result

    def add_checked(self, word, data):
        """ add checked ``word`` form cache"""
        if self.db:
            self.db.set(word, data)


    
    def exists_cache_word(self, word):
        """ test if word exists in cache"""
        #if exists in cache dictionary
        if word in self.cache:
            return True
        else: # test in database
            if self.is_already_checked(word):
                stored_data = self.get_checked(word)
                self.cache[word] = stored_data
                return bool(self.cache[word])
            else:
                # add null dict to the word index to avoid multiple database check
                self.cache[word] = {}
                return {}            

    
    def get_relation_freq(self, word_prev, word_cur, relation):
        self.exists_cache_word(word_prev)
        return self.cache.get(word_prev, {}).get(word_cur, {}).get(relation, 0);
    
    def is_related(self, word_prev, word_cur):
        """ test if two words are related"""
        #serach in cache
        self.exists_cache_word(word_prev)
        # if exists in cache or database
        return self.cache.get(word_prev, {}).get(word_cur, {});
                
            

    def add_relation(self, word_prev, word_cur, relation):
        
        #~ relation ='r'+str(relation)

        if word_prev not in self.cache:
            # test first that is in db cache
            if self.is_already_checked(word_prev):
                stored_data = self.get_checked(word_prev)
                self.cache[word_prev] = stored_data
            else: # create an new entry
                self.cache[word_prev] = {word_cur:{relation:1, }, }

        # word_prev exists
        # add word_cur to previous dict
        elif word_cur not in self.cache[word_prev]:
            self.cache[word_prev][word_cur] = {relation:1,}
                
        elif relation not in self.cache[word_prev][word_cur]:
            self.cache[word_prev][word_cur][relation] = 1
        else:
            self.cache[word_prev][word_cur][relation] += 1

    def display_all(self):
        """ display all contents of data base """
        #~ pass
        print("aranasyn.cache: dislay all records in Thaalib Database """)
        if self.db:
            for key in self.db.getall():
                print(key, self.db.get(key))
        
def mainly():
    mycache = cache()
    #mycache.display_all()      
    
if __name__=="__main__":
    mainly();
