import os

import shutil
import random
#you must create train test and val folder in imagesdir and annoatation dir 
def split_data(images_dir, annotations_dir, train_pct=0.7, val_pct=0.2, test_pct=0.1):
    


      for image_file in os.listdir(images_dir):
          if image_file.endswith('.JPG'):
              image_path = os.path.join(images_dir, image_file)
              dest_dir = _random_split(train_pct, val_pct, test_pct)
              imagesplit = os.path.join(images_dir,dest_dir)
              shutil.move(image_path,imagesplit )

              annotation_file = image_file.replace('.JPG', '.txt')
              annotation_path = os.path.join(annotations_dir,annotation_file)
              annotsplit = os.path.join(annotations_dir,dest_dir)
              if os.path.exists(annotation_path):

                shutil.move(annotation_path, annotsplit)

def _random_split(train_pct, val_pct, test_pct):
    r = random.random()
    if r < train_pct:
        return 'train'
    elif r < train_pct + val_pct:
        return 'val'
    else:
        return 'test'

if __name__ == '__main__':
    images_dir = 'images/dir'
    annotations_dir = 'annotation/dir'
    split_data(images_dir, annotations_dir)