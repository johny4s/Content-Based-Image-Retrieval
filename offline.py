from PIL import Image
from pathlib import Path
import numpy as np
from feature_extractor import FeatureExtractor
import os
os.environ['TF_CPP_MON_LOG_LEVEL']='2'


if __name__ == '__main__':
    fe = FeatureExtractor()
    for img_path in Path("./static/image").glob("*.jpg"):
        print(img_path)
        feature = fe.extract(img=Image.open(img_path))
        print(type(feature),feature.shape)
        feature_path = Path("./static/feature") / (img_path.stem + ".npy") 
        print(feature_path)
        np.save(feature_path, feature)