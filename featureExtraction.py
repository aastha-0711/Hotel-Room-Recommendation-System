import numpy as np
import pandas as pd
from DeepImageSearch import Index, LoadData

# store the os path of all image folder in the list
image_list = LoadData().from_folder(folder_list=['static/images'])

# for Faster Search we need to index Data first
# after Indexing, meta data stored on the local path
Index(image_list).Start()
