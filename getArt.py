import urllib.request
from tqdm import tqdm

def getArt(url, file):
    parent = "art/"
    urllib.request.urlretrieve(url, parent+str(file)+'.bmp')

def getUrl(line, index):
    return line.split(',')[-2].split('+')[index]

def main():
    file = open('out').read()
    file = file.split('\n')
    i = 1

    for line in tqdm(file):
        getArt(getUrl(line, 0), i)
        i+=1

main()

