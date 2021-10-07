import os
import PyPDF2


def resize(path: str) -> str:
    """[summary]

    Args:
        path (str): [description]

    Returns:
        str: [description]
    """

    pdfReader = PyPDF2.PdfFileReader(path)
    writerObj = PyPDF2.PdfFileWriter()

    for i in range(pdfReader.getNumPages()):
        page = pdfReader.getPage(i)

        # Put custom values according your requirements
        page.mediaBox.lowerLeft = (200, 200)
        page.mediaBox.lowerRight = (595.28, 200)
        page.mediaBox.upperLeft = (0, 841.88)
        page.mediaBox.upperRight = (595.28, 841.88)

        writerObj.addPage(page)

    outstream = open(os.path.join("data", "output.pdf"), "wb")
    writerObj.write(outstream)
    outstream.close()


if __name__ == "__main__":
    resize("data/input.pdf")
