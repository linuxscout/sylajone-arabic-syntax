import sys
sys.path.append('../')    
import sylajone.anasyn as asn
import pprint

text  =  u"يعبد الله منذ أن تطلع الشمس"
result  =  []
anasyn  =  asn.SyntaxAnalyzer()    
result  =  anasyn.analyze_text(text)
anasyn.pprint(result)        



# Extract synantic relation, display only found relations
syn_result = anasyn.display_syn(result)
pprint.pprint(syn_result)      

# Extract synantic relation, display all words and tags
syn_result = anasyn.display_syn(result, all=True)
pprint.pprint(syn_result)

# convert to pandas
import pandas as pd
# flatten the result
df = pd.DataFrame(anasyn.decode(result))
print(df.head())
df.to_csv("output/test.csv", encoding="utf8", sep="\t")

