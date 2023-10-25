from pathlib import Path
import skimage
import skimage as ski
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.feature import hog
from HistogramLBP import HistogramLBP

group = {"triste": 0, "alegre": 1, "normal": 2, "enojado": 3}


def get_data(image_set, group):
    features_vector = [0 for _ in range(len(image_set))]
    for i, image in enumerate(image_set):
        image = rgb2gray(resize(image_raw, (28, 28)))
        lbp = HistogramLBP(image)
        hog_histogram = hog(image)
        features_vector[i] = [group] + lbp.histogram + list(hog_histogram)
    del image
    return features_vector


image_raw = ski.io.imread('img.jpg')
path = Path('./dataset')
data = []
for i in path.iterdir():
    group_number = group[i.parts[1]]
    emotion_path_elements = list(Path(f'./dataset/{i.name}/').iterdir())
    for index, j in enumerate(Path(f'./dataset/{i.name}/').iterdir()):
        image_raw = skimage.io.imread(j)
        image = rgb2gray(resize(image_raw, (28, 28)))
        lbp = HistogramLBP(image)
        hog_histogram = [round(i, 2) for i in hog(image)]
        line = ','.join([str(i) for i in ([group_number] + lbp.histogram + list(hog_histogram))])
        print(i.parts[1], index)
        data.append(line)

with open('out.csv', 'w') as out:
    header = ['emocion,']
    header.extend([f'lbp_{i+1},' for i in range(59)])
    header.extend([f'hog_{i+1},' for i in range(81)])
    header = ''.join(header)
    header = header[:-1]
    header += '\n'
    out.writelines(header)
    for i in data:
        i += '\n'
        out.writelines([i])
