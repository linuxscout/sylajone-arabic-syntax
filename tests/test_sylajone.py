#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_dict.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )

import sys
import pandas as pd

import qalsadi.analex     
import pyarabic.araby as araby
sys.path.append('../')
import sylajone.anasyn as asn

def test(display="pprint"):
    import pprint
    text  =  u"يعبد الله منذ أن تطلع الشمس"
    result  =  []
    #~ analex    =  qalsadi.analex.Analex()    
    analyzer  =  asn.SyntaxAnalyzer()    
    
    #~ result_lex = analex.check_text(text)
    #~ result, synodelist   =  analyzer.analyze(result_lex)
    result   =  analyzer.analyze_text(text)
    #~ result    =  analyzer.analyze_text(text)
    
    if display == "pandas":
        # the result contains objets
        df = pd.DataFrame(analyzer.decode(result))
        print(df.head())
        df.to_csv("output/test.csv", encoding="utf8", sep="\t")
    elif display == "pprint":
        # the result contains objets
        analyzer.pprint(result)        
    elif display == "only":
        # the result contains objets
        syn_result = analyzer.display_syn(result)
        pprint.pprint(syn_result)      
    elif display == "all":
        # the result contains objets
        syn_result = analyzer.display_syn(result, all=True)
        pprint.pprint(syn_result)
    else:
        pprint.pprint(analyzer.decode(result))


if __name__  ==  '__main__':
    #~ test2()
    #~ display_format = "all"
    #~ display_format = "pandas"
    #~ display_format = "only"
    #~ display_format = "NONE"
    display_format = "pprint"
    test(display_format)
