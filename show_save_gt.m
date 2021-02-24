%   Copyright 2021 Borut Batagelj.

show_annotations=0; %show image with annotations
save_faces=1; %save faces from images to folders: correctly_worn, without_mask, incorrectly_worn

gt_dir='FMLD_annotations/'; %FMLD xml folder
images_wider_dir='WIDER/'; %folder where are WIDER_val and WIDER_train
images_mafa_dir='MAFA/'; %folder where are test-images and train-images

gt_files=dir([gt_dir,'*/*.xml']); 
gt_num=size(gt_files,1);


if save_faces
  mkdir('faces/test/compliant/correctly_worn');  
  mkdir('faces/test/non-compliant/without_mask');
  mkdir('faces/test/non-compliant/incorrectly_worn');
  
  mkdir('faces/train/compliant/correctly_worn');  
  mkdir('faces/train/non-compliant/without_mask');
  mkdir('faces/train/non-compliant/incorrectly_worn');
end


for i=1:gt_num
  xml_file=[gt_files(i).folder,'/',gt_files(i).name];
  mlStruct = VOCreadxml(xml_file);
  if strcmp(mlStruct.annotation.source.database,'WIDER')
    image_path=[images_wider_dir,mlStruct.annotation.path];
  elseif strcmp(mlStruct.annotation.source.database,'MAFA')
    image_path=[images_mafa_dir,mlStruct.annotation.path];
  end
  
  if (save_faces || show_annotations)
    I=imread(image_path);
    [h,w,~]=size(I);
  end

  if show_annotations
    figure(1); clf;
    imshow(I,'InitialMagnification','fit');
  end
  
  faces=size(mlStruct.annotation.object,2);
  for ii=1:faces
    
    name=mlStruct.annotation.object(ii).name;
    
    xmin=max(1,str2num(mlStruct.annotation.object(ii).bndbox.xmin)+1);
    ymin=max(1,str2num(mlStruct.annotation.object(ii).bndbox.ymin)+1);
    xmax=min(w,str2num(mlStruct.annotation.object(ii).bndbox.xmax)+1);
    ymax=min(h,str2num(mlStruct.annotation.object(ii).bndbox.ymax)+1);  
    BBox=[xmin ymin xmax-xmin ymax-ymin];
        
    if strcmp(mlStruct.annotation.object(ii).difficult,'1')  
      col='white';
    else
      if strcmp(name,'unmasked_face')  
        col='red';
        if save_faces
          imwrite(I(ymin:ymax,xmin:xmax,:),['faces/',mlStruct.annotation.folder,'/non-compliant/without_mask/',mlStruct.annotation.filename(1:end-4),'-face',num2str(ii),'.png']);
        end
      elseif strcmp(name,'masked_face') 
        col='green';
        if save_faces
          imwrite(I(ymin:ymax,xmin:xmax,:),['faces/',mlStruct.annotation.folder,'/compliant/correctly_worn/',mlStruct.annotation.filename(1:end-4),'-face',num2str(ii),'.png']);
        end
      elseif strcmp(name,'invalid_face') 
        col='blue';
      elseif strcmp(name,'incorrectly_masked_face') 
        col='yellow';
        if save_faces
          imwrite(I(ymin:ymax,xmin:xmax,:),['faces/',mlStruct.annotation.folder,'/non-compliant/incorrectly_worn/',mlStruct.annotation.filename(1:end-4),'-face',num2str(ii),'.png']);
        end
      end
    end

    if show_annotations
      rectangle('Position',BBox,'EdgeColor',col,'LineWidth',2);
    end
    
  end % for ii=1:faces
end % for i=1:gt_num
