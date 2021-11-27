#   Copyright 2021 Borut Batagelj.

import glob
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tqdm import tqdm

show_annotations=False #show image with annotations
save_faces=True #save faces from images to folders: correctly_worn, without_mask, incorrectly_worn

gt_dir='FMLD_annotations/'; #FMLD xml folder

images_wider_dir='WIDER/' #folder where are WIDER_val and WIDER_train
images_mafa_dir='MAFA/' #folder where are test-images and train-images

gt_files=glob.glob(gt_dir+'*/*.xml')
gt_num=len(gt_files)

if save_faces and not os.path.exists('faces'):
    os.makedirs('faces/test/compliant/correctly_worn')  
    os.makedirs('faces/test/non-compliant/without_mask')
    os.makedirs('faces/test/non-compliant/incorrectly_worn')
  
    os.makedirs('faces/train/compliant/correctly_worn')
    os.makedirs('faces/train/non-compliant/without_mask')
    os.makedirs('faces/train/non-compliant/incorrectly_worn')

for xml_file in tqdm(gt_files):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    if save_faces:
        filename = root.find('filename').text
        folder = root.find('folder').text

    database = root.find('source/database').text
    path = root.find('path').text
    
    if database == 'WIDER':
        image_path = os.path.join(images_wider_dir,path)
    elif database == 'MAFA':
        image_path = os.path.join(images_mafa_dir,path)

    if save_faces or show_annotations:
        if not os.path.exists(image_path):
             filepath = os.path.dirname(image_path)
             print(f'Download {database} dataset and provide images in folder: {filepath}.\n')
             quit()
        I = plt.imread(image_path)
        [h,w,c]=I.shape

    if show_annotations:
        plt.imshow(I)
        ax = plt.gca()

    for ii, boxes in enumerate(root.iter('object'), start=1):
        name = boxes.find('name').text

        ymin, xmin, ymax, xmax = None, None, None, None

        
        xmin = max(0,int(float(boxes.find("bndbox/xmin").text)))
        ymin = max(0,int(float(boxes.find("bndbox/ymin").text)))
        xmax = min(w,int(float(boxes.find("bndbox/xmax").text)))
        ymax = min(h,int(float(boxes.find("bndbox/ymax").text)))
        BBox=[xmin, ymin, xmax-xmin, ymax-ymin]


        sub_folder = None
        if boxes.find('difficult').text == '1':
            col='white'
        else:
            if name == 'unmasked_face':
                col='red'
                sub_folder = 'non-compliant/without_mask/'
            elif name == 'masked_face':
                col='green'
                sub_folder = 'compliant/correctly_worn/'
            elif name == 'invalid_face':
                col='blue'
            elif name == 'incorrectly_masked_face':
                col='yellow'
                sub_folder = 'non-compliant/incorrectly_worn/'

            if save_faces and sub_folder:
                plt.imsave(os.path.join('faces',folder,sub_folder,filename[0:-4]+'-face'+str(ii)+'.png'), I[ymin:ymax,xmin:xmax,:])

        if show_annotations:
            rect = patches.Rectangle((BBox[0], BBox[1]), BBox[2], BBox[3],linewidth=2, edgecolor=col, facecolor='none')
            ax.add_patch(rect)
    plt.show()