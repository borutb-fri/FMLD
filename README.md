# Face Mask Label Dataset (FMLD)
The Face Mask Label Dataset (FMLD) is a challenging, in the wild dataset for experimentation with face masks. The dataset is the biggest annotated face mask dataset with 63,072 face images.

This repository contains labels and annotations for all images and the PyTorch implementation of the following paper: [How to Correctly Detect Face-Masks for COVID-19 from Visual Information?](https://www.mdpi.com/2076-3417/11/5/2070/htm) [[1]](#citation)

Images annotated for FMLD were taken from datasets:
- [MAFA](https://imsg.ac.cn/research/maskedface.html) [2] [MAFA Datasets: [Google Drive](https://drive.google.com/open?id=1nbtM1n0--iZ3VVbNGhocxbnBGhMau_OG), [Kaggle](https://www.kaggle.com/rahulmangalampalli/mafa-data)] and 
- [Wider Face](http://shuoyang1213.me/WIDERFACE) [3] [Training Images: [Google Drive](https://drive.google.com/file/d/0B6eKvaijfFUDQUUwd21EckhUbWs/view?usp=sharing), Validation Images: [Google Drive](https://drive.google.com/file/d/0B6eKvaijfFUDd3dIRmpvSk8tLUk/view?usp=sharing)]

## Overall FMLD statistics

Images annotated for FMLD were taken from the MAFA and Wider Face datasets and partitioned into three classes (correctly worn masks, incorrectly worn masks and without masks) and later equipped with additional labels.

![tabel](images/table.png)

## Labels/Annotations for all images
Our annotations [1]:  [FMLD_annotations.zip](FMLD_annotations.zip)

## Dataset lists
### Lists of images from the MAFA dataset:
- [MAFA_training.txt](MAFA_training.txt)
- [MAFA_testing.txt](MAFA_testing.txt)

### Lists of images from the Wider Face dataset
- [Wider_training.txt](Wider_training.txt)
- [Wider_testing.txt](Wider_testing.txt)

![labels](images/labels-01.png "Available labels and the label distribution across the faces annotated for FMLD.")
As can be seen, the dataset contains labels for gender, pose and ethnicity in addition to the main labels indicating the presence of face masks and their correct/incorrect placement.

All images are annotated with labels indicating the presence of face masks, the placement of face masks (i.e., correct or incorrect), the gender of the subjects, their ethnicity and head pose.

### We used XML files in the PASCAL VOC file format for annotations. The annotation file for each image contains information about:
- the name of the original image,
- it’s size and
- the source dataset.

### The annotated face in the image can be:
- **with mask** (name: *masked_face*),
- **without mask** (name: *unmasked_face*) and
- **with mask worn incorrectly** (name: *incorrectly_masked_face*).

### Each face object has bounding box information and labels for
- gender (*male / female*),
- ethnicity (*asian / white / black*) and
- pose (*front / turned sideways*).

### Note: *difficult* label in testing dataset (difficult=1)
- faces with invalid label in original dataset (name: *invalid_face*)
- faces in original dataset but not included in our FMLD dataset (*unmasked_face*)
- additional faces added using a face detector (*masked_face /unmasked_face/incorrectly_masked_face*)

## Support code
code for display images with annotations and save faces from images

MATLAB code : [show_save_gt.m](show_save_gt.m)

Python code : [show_save_gt.py](show_save_gt.py)

## Example usage
### Monitoring if people are using masks correctly

[resnet152.pt](https://unilj-my.sharepoint.com/:u:/g/personal/borutb_fri1_uni-lj_si/EdmDsIgG9XBJkRVXDKyOwvEBK7pK1EEq9cBfOVm3kLzPvw?e=M9pULa): Pytorch model for classification.

[mask-test.py](mask-test.py): Python code to classify the correctly worn mask (*compliant/non-compliant*)

![shema](images/shema.png "Overall pipeline designed for the evaluation procedure.")

## Citation
If you use our annotations, please use following citations
```
[1] 
@Article{app11052070,
AUTHOR = {Batagelj, Borut and Peer, Peter and Štruc, Vitomir and Dobrišek, Simon},
TITLE = {How to Correctly Detect Face-Masks for COVID-19 from Visual Information?},
JOURNAL = {Applied Sciences},
VOLUME = {11},
YEAR = {2021},
NUMBER = {5},
ARTICLE-NUMBER = {2070},
URL = {https://www.mdpi.com/2076-3417/11/5/2070},
ISSN = {2076-3417},
DOI = {10.3390/app11052070}
}

[2]
@inproceedings{ge2017detecting,
  title={Detecting Masked Faces in the Wild with LLE-CNNs},
  author={Ge, Shiming and Li, Jia and Ye, Qiting and Luo, Zhao},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={2682--2690},
  year={2017}
}

[3]
@inproceedings{yang2016wider,
  Author = {Yang, Shuo and Luo, Ping and Loy, Chen Change and Tang, Xiaoou},
  Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  Title = {WIDER FACE: A Face Detection Benchmark},
  Year = {2016}
}

```
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

