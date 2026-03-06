# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:35:51 2022

@author: tmp
"""

import os, sys
from itertools import combinations
positiveSeqFile = './examples/PDD/data/potr.txt'
negativeSeqFile = './examples/PDD/data/netr.txt'

# positiveFeaFiles = []
# negativeFeaFiles = []
# dataPath = './data'
# for f in os.listdir(dataPath):
#     if f.startswith('po'):
#         positiveFeaFiles.append('%s/%s' %(dataPath,f))
#     elif f.startswith('ne'):
#         negativeFeaFiles.append('%s/%s' %(dataPath,f))

    
positiveFeaFiles = ['./examples/PDD/data/potr-HexaNC.txt', './examples/PDD/data/potr-TetraNC.txt', './examples/PDD/data/potr-PentaNC.txt', './examples/PDD/data/potr-MGW.txt', './examples/PDD/data/potr-ProT.txt', './examples/PDD/data/potr-Roll.txt', './examples/PDD/data/potr-HelT.txt', './examples/PDD/data/potr-EP.txt', './examples/PDD/data/potr-Nucleosome.txt','./examples/PDD/data/potr-DnaseI.txt','./examples/PDD/data/potr-RFHC.txt']

negativeFeaFiles = ['./examples/PDD/data/netr-HexaNC.txt', './examples/PDD/data/netr-TetraNC.txt', './examples/PDD/data/netr-PentaNC.txt', './examples/PDD/data/netr-MGW.txt', './examples/PDD/data/netr-ProT.txt', './examples/PDD/data/netr-Roll.txt', './examples/PDD/data/netr-HelT.txt', './examples/PDD/data/netr-EP.txt', './examples/PDD/data/netr-Nucleosome.txt','./examples/PDD/data/netr-DnaseI.txt','./examples/PDD/data/netr-RFHC.txt']

# spcLenList = []

feaDict = {}
for i in range(len(positiveFeaFiles)):
    posFile = positiveFeaFiles[i]
    negFile = negativeFeaFiles[i]
    feaName = os.path.split(posFile)[-1].split('-')[-1].split('.')[0]
    modelName = './examples/PDD/model/%s.py' %feaName
    # assert os.path.exists(modelName)
    feaDict[feaName] = (posFile,negFile,modelName,200)

repeatTime = 5

cmdTemp = 'python running.py --dataType dna %s --dataEncodingType dict %s --dataTrainFilePaths %s --dataTrainLabel 1 0%s --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/rnncnn.py %s --verbose 1 --showFig 0 --outSaveFolderPath %s --savePrediction 1 --saveFig 1 --batch_size 128 --epochs 20 --shuffleDataTrain 1 --spcLen 81 %s --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3 --dataTrainModelInd 0 0%s'
errCMDList = []
feaNames = list(feaDict.keys())

for repeatNum in range(repeatTime):
    for combNum in range(11):
        combIterObj = combinations(feaNames, combNum + 1)
        
        for combIter in combIterObj:
            dataType = ''
            dataEncodingType = ''
            dataTrainFilePaths = positiveSeqFile+' '+negativeSeqFile #oriFile needed
            dataTrainLabel = ''
            modelLoadFile = ''
            outSaveFolderPath = 'outs%d/' %repeatNum
            spcLen = ''
            dataTrainModelInd = ''
            modelCount = 1
            
            for feaName in combIter:
                _posFile,_negFile,_modelName,_spcLen = feaDict[feaName]
                
                dataType += ' other'
                dataEncodingType += ' other'
                dataTrainFilePaths += ' ' + _posFile + ' ' + _negFile
                dataTrainLabel += ' 1 0'
                modelLoadFile += ' ' + _modelName
                outSaveFolderPath += feaName + '__'
                spcLen += ' %d' %_spcLen
                dataTrainModelInd += ' %d %d' %(modelCount,modelCount)
                modelCount += 1
            outSaveFolderPath = outSaveFolderPath[:-2]
            cmd = cmdTemp %(dataType, dataEncodingType, dataTrainFilePaths, dataTrainLabel, modelLoadFile, outSaveFolderPath, spcLen, dataTrainModelInd)
            print('#' * 10)
            print(cmd)
            isErr = os.system(cmd)
            if isErr:
                errCMDList.append('%d::%s' %(repeatNum,cmd))
print('#'*50)
print('err:')
for cmd in errCMDList:
    print('*'*10)
    print(cmd)
