Sylajone: Arabic syntax Analyzer library
========================================

مكتبة سيلجون للتحليل النحوي
===========================

Sylajone: Arabic syntax Analyzer library

.. figure:: doc/sylajone_header.png
   :alt: sylajone logo

   sylajone logo

.. figure:: https://img.shields.io/pypi/dm/sylajone
   :alt: PyPI - Downloads

   PyPI - Downloads

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+-------------+------------------------------------------------------------------------------------------------+
| Features    | value                                                                                          |
+=============+================================================================================================+
| Authors     | `Authors.md <https://github.com/linuxscout/sylajone-arabic-syntax/master/AUTHORS.md>`__        |
+-------------+------------------------------------------------------------------------------------------------+
| Release     | 0.1                                                                                            |
+-------------+------------------------------------------------------------------------------------------------+
| License     | `GPL <https://github.com/linuxscout/sylajone-arabic-syntax/master/LICENSE>`__                  |
+-------------+------------------------------------------------------------------------------------------------+
| Tracker     | `linuxscout/sylajone/Issues <https://github.com/linuxscout/sylajone-arabic-syntax/issues>`__   |
+-------------+------------------------------------------------------------------------------------------------+
| Source      | `Github <http://github.com/linuxscout/sylajone-arabic-syntax>`__                               |
+-------------+------------------------------------------------------------------------------------------------+
| Feedbacks   | `Comments <https://github.com/linuxscout/sylajone-arabic-syntax/>`__                           |
+-------------+------------------------------------------------------------------------------------------------+
| Accounts    | [@Twitter](https://twitter.com/linuxscout))                                                    |
+-------------+------------------------------------------------------------------------------------------------+

Description
-----------

Sylajone: Arabic syntax Analyzer library

مزايا:
~~~~~~

-  استخلاص العلاقات النحوية بين ثنائيات الكلمات : (فعل -فاعل، فعل-مفعول
   به، ناصب منصوب، جار مجرور)


install
~~~~~~~

.. code:: shell

    pip install sylajone

Usage
~~~~~

import
^^^^^^

.. code:: python

    pip install sylajone

Test
^^^^

.. code:: python

    >>> import sylajone.anasyn as asn
    >>> import pprint
    >>> 
    >>> text  =  u"يعبد الله منذ أن تطلع الشمس"
    >>> result  =  []
    >>> anasyn  =  asn.SyntaxAnalyzer()    
    >>> result  =  anasyn.analyze_text(text)
    >>> anasyn.pprint(result)

-  Extract semantic relation, display only found relations

.. code:: python

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

-  Extract semantic relation, display all words and tags

   .. code:: python

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

-  convert to pandas \`\`\`python >>> # convert to pandas ... import
   pandas as pd >>> # flatten the result ... df =
   pd.DataFrame(anasyn.decode(result)) >>> print(df.head()) action affix
   affix\_key forced\_word\_case ... unvocalized unvoriginal vocalized
   word 0 -ي-- -ي--\|المضارع المنصوب:هو:y False ... يعبد عبد يُعَبِّدَ
   يعبد 1 -ي-- -ي--\|المضارع المجهول المجزوم:هو:y False ... يعبد عبد
   يُعَبَّدْ يعبد 2 -ي-- -ي--\|المضارع المجهول:هو:y False ... يعبد عبد
   يُعَبَّدُ يعبد 3 -ي-- -ي--\|المضارع المعلوم:هو:y False ... يعبد عبد
   يُعَبِّدُ يعبد 4 -ي-- -ي--\|المضارع المجزوم:هو:y False ... يعبد عبد
   يُعَبِّدْ يعبد

[5 rows x 50 columns] >>> df.to\_csv("output/test.csv", encoding="utf8",
sep=":raw-latex:'\t'")

[requirement]
^^^^^^^^^^^^^

::

    1. CodernityDB>=0.5.0   /  CodernityDB3>=0.6.0
    2. libqutrub>=1.2.4.1
    3. naftawayh>=0.4
    4. pyarabic>=0.6.8
    5. qalsadi>=0.3.5
