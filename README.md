# Sylajone: Arabic syntax Analyzer library

#مكتبة سيلجون للتحليل النحوي

Sylajone: Arabic syntax Analyzer library

![sylajone logo](doc/sylajone_header.png  "sylajone logo")

![PyPI - Downloads](https://img.shields.io/pypi/dm/sylajone)


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/sylajone-arabic-syntax/master/AUTHORS.md)
Release  | 0.1
License  |[GPL](https://github.com/linuxscout/sylajone-arabic-syntax/master/LICENSE)
Tracker  |[linuxscout/sylajone/Issues](https://github.com/linuxscout/sylajone-arabic-syntax/issues)
Source  |[Github](http://github.com/linuxscout/sylajone-arabic-syntax)
Feedbacks  |[Comments](https://github.com/linuxscout/sylajone-arabic-syntax/)
Accounts  |[@Twitter](https://twitter.com/linuxscout))

## Description

Sylajone: Arabic syntax Analyzer library



###  مزايا:
* استخلاص العلاقات النحوية بين ثنائيات الكلمات : (فعل -فاعل، فعل-مفعول به، ناصب منصوب، جار مجرور)

<div dir="rtl">

- 

</div>
## Citation
```bibtex
@thesis{zerrouki2020adawat,
author = {Taha Zerrouki},
title = {Towards An Open Platform For Arabic Language Processing},
type = {PhD thesis},
institution = {Ecole Nationale Supérieure d'informatique, Alger, Algérie},
date = {2020},
}
```

### Usage

#### import
```python
pip install sylajone
```
#### Test 
```python
>>> import sylajone.anasyn as asn
>>> import pprint
>>> 
>>> text  =  u"يعبد الله منذ أن تطلع الشمس"
>>> result  =  []
>>> anasyn  =  asn.SyntaxAnalyzer()    
>>> result  =  anasyn.analyze_text(text)
>>> anasyn.pprint(result)
```

* Extract semantic relation, display only found relations

```python
>>> import pprint
>>> syn_result = anasyn.display_syn(result)
>>> pprint.pprint(syn_result)         
[[['اللهَ', 'يُعَبِّدَ', 'اللهُ', 'عَبَّدَ', 20],
  ['اللهَ', 'يُعَبِّدُ', 'اللهُ', 'عَبَّدَ', 20],
  ['اللهَ', 'يُعَبِّدْ', 'اللهُ', 'عَبَّدَ', 20],
  ['اللهَ', 'يَعْبُدَ', 'اللهُ', 'عَبَدَ', 20],
  ['اللهَ', 'يَعْبُدُ', 'اللهُ', 'عَبَدَ', 20],
  ['اللهَ', 'يَعْبُدْ', 'اللهُ', 'عَبَدَ', 20],
  ['اللهُ', 'يُعَبِّدَ', 'اللهُ', 'عَبَّدَ', 10],
...
```
* Extract semantic relation, display all words and tags
```python
>>> syn_result = anasyn.display_syn(result, all=True)
>>> pprint.pprint(syn_result)
[('يعبد', 'B', []),
 ('الله',
  'I',
  [['اللهَ', 'يُعَبِّدَ', 'اللهُ', 'عَبَّدَ', 20],
   ['اللهَ', 'يُعَبِّدُ', 'اللهُ', 'عَبَّدَ', 20],
   ['اللهَ', 'يُعَبِّدْ', 'اللهُ', 'عَبَّدَ', 20],
   ['اللهَ', 'يَعْبُدَ', 'اللهُ', 'عَبَدَ', 20],
   ['اللهَ', 'يَعْبُدُ', 'اللهُ', 'عَبَدَ', 20],
   ['اللهَ', 'يَعْبُدْ', 'اللهُ', 'عَبَدَ', 20],
   ['اللهُ', 'يُعَبِّدَ', 'اللهُ', 'عَبَّدَ', 10],
...
>>> 
```

* convert to pandas
```python
>>> # convert to pandas
... import pandas as pd
>>> # flatten the result
... df = pd.DataFrame(anasyn.decode(result))
>>> print(df.head())
  action affix                          affix_key  forced_word_case  ...   unvocalized  unvoriginal  vocalized  word
0         -ي--          -ي--|المضارع المنصوب:هو:y             False  ...          يعبد          عبد  يُعَبِّدَ  يعبد
1         -ي--  -ي--|المضارع المجهول المجزوم:هو:y             False  ...          يعبد          عبد  يُعَبَّدْ  يعبد
2         -ي--          -ي--|المضارع المجهول:هو:y             False  ...          يعبد          عبد  يُعَبَّدُ  يعبد
3         -ي--          -ي--|المضارع المعلوم:هو:y             False  ...          يعبد          عبد  يُعَبِّدُ  يعبد
4         -ي--          -ي--|المضارع المجزوم:هو:y             False  ...          يعبد          عبد  يُعَبِّدْ  يعبد

[5 rows x 50 columns]
>>> df.to_csv("output/test.csv", encoding="utf8", sep="\t")

```


#### [requirement]
  
    1. CodernityDB>=0.5.0   /  CodernityDB3>=0.6.0
    2. libqutrub>=1.2.4.1
    3. naftawayh>=0.4
    4. pyarabic>=0.6.8
    5. qalsadi>=0.3.5


### تسمية
أحمد بن سليجون هو أبو العباس أحمد بن يحيى بن زيد بن سيار، البغدادي النحوي، الشيباني أو ثعلب (200 هـ-291 هـ) (816-904)م، إمام الكوفيين في عهده، وثالث ثلاثة قامت على أعمالهم مدرسة الكوفة النحوية، العلامة المحدث، وإمام النحو، صاحب الفصيح والتصانيف، ولد ببغداد في السنة الثانية من خلافة المأمون وبها مات. 
