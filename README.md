# iPromoter-MFF-main
iPromoter-MFF is a multimodal deep learning model for identifying prokaryotic promoters across multiple species with high accuracy.
# iPromoter-MFF
## Multimodal Feature Fusion for Prokaryotic Promoter Identification

# Corresponding Author
ljs@swmu.edu.cn


# Overview
iPromoter-MFF is a robust deep learning framework designed to identify prokaryotic promoters across multiple species. By integrating multimodal data, including DNA sequence, composition, shape, and physicochemical properties, iPromoter-MFF provides highly accurate promoter predictions. The model uses Transformer-based encoders to capture sequential information, while dense networks handle structural information that traditional methods cannot interpret from sequences alone. Through systematic evaluation of 8 unimodal models (BiLSTM, CNN-RNN, RCNN, TextCNN, FNet, RNN-CNN, Multi-Text-CNN, and Transformers), and 2047 multimodal combinations, the most successful configuration was identified: Transformers + TextCNN + FNet + MACCS + ECFP6. This combination achieved outstanding performance across a variety of promoter prediction tasks.ly improving prediction accuracy and generalization ability. Through training and testing various models, this project demonstrates excellent performance on different datasets and tasks.

# Usage
## Preparation
1) Download this repository; all the files are in the 'examples/iPromoter-MFF' folder.

2) Download autoBioSeqpy from Please download the repository from the folder 'autobioseqpy2.0_20200805'. All the necessary files are included there for the version of autoBioSeqpy.

3) After downloading and extracting the source files, merge the examples folder into the root directory of autoBioSeqpy. The code for this work will then be located in 'examples/iPromoter-MFF'.

## Start to use
You can directly run the generateCMD.py file in the 'examples/iPromoter-MFF' directory to execute multimodal fusion tests. This will test 2047 model combinations, each repeated five times. Results will be stored in the outs folder, with a comprehensive summary provided in Table_S1.csv.

python examples/iPromoter-MFF/generateCMD.py

Command Line for Multimodal iPromoter-MFF Training and Validation

python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths ./examples/PDD/data/potr.txt ./examples/PDD/data/netr.txt ./examples/PDD/data/potr-TetraNC.txt ./examples/PDD/data/netr-TetraNC.txt ./examples/PDD/data/potr-Roll.txt ./examples/PDD/data/netr-Roll.txt ./examples/PDD/data/potr-Nucleosome.txt ./examples/PDD/data/netr-Nucleosome.txt ./examples/PDD/data/potr-RFHC.txt ./examples/PDD/data/netr-RFHC.txt --dataTrainLabel 1 0 1 0 1 0 1 0 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/FNet.py ./examples/PDD/model/TetraNC.py ./examples/PDD/model/Roll.py ./examples/PDD/model/Nucleosome.py ./examples/PDD/model/RFHC.py --verbose 1 --outSaveFolderPath outs0/TetraNC__Roll__Nucleosome__RFHC --savePrediction 1 --saveFig 1 --figDPI 300 --showFig 0 --batch_size 128 --epochs 20 --shuffleDataTrain 1 --spcLen 81 200 200 200 200 --useKMer 1 --KMerNum 3 --loss binary_crossentropy --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --metrics acc --noGPU 0 --paraSaveName parameters.txt --seed 1 --labelToMat False --colorText Auto --shuffleDataTest False --dataTrainModelInd 0 0 1 1 2 2 3 3 4 4 --dataTestModelInd --modelSaveName None --weightSaveName None --reshapeSize 

Single Model Command
====================
1.bilstm Model
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/bilstm.py --verbose 1 --outSaveFolderPath out/bilstm --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

2.cnnrnn Model
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/cnnrnn.py --verbose 1 --outSaveFolderPath out/cnnrnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

3.dpcnn Model
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/dpcnn.py --verbose 1 --outSaveFolderPath out/dpcnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

4.FastText Model
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/FastText.py --verbose 1 --outSaveFolderPath out/FastText --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

5.FNet
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/FNet.py --verbose 1 --outSaveFolderPath out/FNet --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

6.multi_text_cnn
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/multi_text_cnn.py --verbose 1 --outSaveFolderPath out/multi_text_cnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

7.rcnn
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/rcnn.py --verbose 1 --outSaveFolderPath out/rcnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

8.rnncnn
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/rnncnn.py --verbose 1 --outSaveFolderPath out/rnncnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

9.text_cnn
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/text_cnn.py --verbose 1 --outSaveFolderPath out/text_cnn --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3

10.transformer
python running.py --dataType dna --dataEncodingType dict --dataTrainFilePaths examples/PDD/data/pos_train.txt examples/PDD/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/PDD/model/transformer.py --verbose 1 --outSaveFolderPath out/transformer --savePrediction 1 --showFig 0 --saveFig 1 --batch_size 64 --epochs 25 --shuffleDataTrain 1 --spcLen 81 --noGPU 0 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --useKMer 1 --KMerNum 3


(--modelLoadFile examples/mol/model/transformer.py)  
(To increase reliability, this experiment was repeated five times, resulting in: out/transformer-1, out/transformer-2, out/transformer-3, out/transformer-4, out/transformer-5.)
