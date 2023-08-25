import os
from PIL import Image
import numpy as np
import cv2
from tqdm import tqdm

os.makedirs('step3_aligned_sar', exist_ok=True)

for key,values in tqdm(json_data.items()):
    sar=os.path.join('../CVPR_2023_backup/sent1/', key.replace('jpg','tiff'))

    vv_path, vh_path = sar, sar.replace('VV','VH')
    vv=np.array(Image.open(vv_path))
    vh=np.array(Image.open(vh_path))
    
    vv=(vv-np.min(vv))/(np.max(vv)-np.min(vv))*255
    vh=(vh-np.min(vh))/(np.max(vh)-np.min(vh))*255
    
    vvvh=np.divide(np.abs(vv), np.abs(vh), out=np.zeros_like(np.abs(vv)), where=np.abs(vh)!=0)
    vvvh=(vvvh-np.min(vvvh))/(np.max(vvvh)-np.min(vvvh))*255
    
    vvvh=np.expand_dims(vvvh, axis=-1)
    vv=np.expand_dims(vv, axis=-1)
    vh=np.expand_dims(vh, axis=-1)
    sar_npy=np.concatenate((vv,vh,vvvh), axis=-1)
    
    sar_npy=Image.fromarray(np.uint8(sar_npy))
    sar_npy.save(os.path.join('step3_aligned_sar', key), "JPEG") 
