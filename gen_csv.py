import glob
from pprint import pprint as pp

SRC_DIR = "./temp/*/*/*"

# <root>/<Scene>/<Class>/img.png

chunk = []
for file in glob.glob(SRC_DIR):
    chunk.append(file.split('/')[2:])
    
pp(chunk)
