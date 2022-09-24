from imutils import paths
from pdf2image import convert_from_path
from tqdm import tqdm
import tempfile
def preprocess(fname):

    imageName = list(paths.list_images(fname))

    outputDir = 'input_image/'
    # Store Pdf with convert_from_path function
    with tempfile.TemporaryDirectory() as path:
        print(path)
        images = convert_from_path(fname, output_folder=path)

        for i in tqdm(range(len(images))):
            # Save pages as images in the pdf
            images[i].save(outputDir + "/page_%03d.jpg" % i, 'JPEG')

if __name__ == "__main__":
    inputDir = 'inputpdf/'
    fname = inputDir + "DÂN LÀNG HỒ.pdf"
    preprocess(fname)