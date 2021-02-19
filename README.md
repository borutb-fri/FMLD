# Face-Mask-Label-Dataset (FMLD)
A challenging, in the wild dataset for experimentation with face masks. The dataset is the biggest annotated face mask dataset with 63,072 face images.

Images annotated for FMLD were taken from the 
- [MAFA](https://imsg.ac.cn/research/maskedface.html) [2] [MAFA Datasets: [Google Drive](https://drive.google.com/open?id=1nbtM1n0--iZ3VVbNGhocxbnBGhMau_OG), [Kaggle](https://www.kaggle.com/rahulmangalampalli/mafa-data)] and 
- [Wider Face](http://shuoyang1213.me/WIDERFACE) [3] [Training Images: [Google Drive](https://drive.google.com/file/d/0B6eKvaijfFUDQUUwd21EckhUbWs/view?usp=sharing), Validation Images: [Google Drive](https://drive.google.com/file/d/0B6eKvaijfFUDd3dIRmpvSk8tLUk/view?usp=sharing)] datasets.

## Overall FMLD statistics

Images annotated for FMLD were taken from the MAFA and Wider Face datasets and partitioned into three classes (correctly worn masks, incorrectly worn masks and without masks) and later equipped with additional labels.

![tabel](images/table.png)

## Dataset lists
### lists of images from the MAFA dataset:
- [MAFA_training.txt](MAFA_training.txt)
- [MAFA_testing.txt](MAFA_testing.txt)

### lists of images from the Wider Face dataset
- [Wider_training.txt](Wider_training.txt)
- [Wider_testing.txt](Wider_testing.txt)

## Labels/Annotations for all images
Our annotations [1]:  [FMLD_annotations.zip](FMLD_annotations.zip)

![labels](images/labels-01.png)

## Citation
If you use our annotations, please use following citations
```
[1] Batagelj, B.; Peer, P.; Štruc. V.; Dobrišek S. 
How to correctly detect face masks for COVID-19 from visual information? 
Appl. Sci. 20XX, XX, XXXX. https://doi.org/XX.XXXX/appXXXXXXX

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

