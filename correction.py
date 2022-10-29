import os
import re
inputDir = 'new_output'
resultDir = 'result'
path = os.listdir(inputDir)

dict = {'ơ̆': 'ố', 'ŏ': 'ồ', '_': '', 'ŭ': 'ủ', '-=': ''}
def correct(sentence):
    regex = r'[,.\\!“]?\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]*\S*\b[,.\\!”]?'
    return re.findall(regex, sentence)




for txt in path:
    txtFile = open(inputDir + '/' + txt, encoding='utf-8', errors='ignore').read()
    for original, replace in dict.items():
        txtFile = txtFile.replace(original, replace)
    LineList = txtFile.split('\n')
    LineList = [x for x in LineList if len(x) > 1]
    proper_noun = []
    for sentence in LineList:
        correctLine = correct(sentence)
        correctLine = [x for x in correctLine if len(x) > 1]
        proper_noun.append(correctLine)
    sentences =[]
    for line in proper_noun:
        sentence = ' '.join(line)
        sentences.append(sentence)
    txtFile = '\n'.join(sentences)



    with open(resultDir + '/' + txt, 'w', encoding='utf-8') as f:
        f.write(txtFile)
