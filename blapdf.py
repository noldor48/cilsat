# importing the required classes
from pypdf import PdfReader, PdfWriter

def PDFrotate(origFileName, newFileName, rotation):

    # creating a pdf Reader object
    reader = PdfReader(origFileName)

    # creating a pdf writer object for new pdf
    writer = PdfWriter()

    # rotating each page
    for page in range(len(reader.pages)):

        pageObj = reader.pages[page]
        pageObj.rotate(rotation)

        # Add the rotated page object to the PDF writer
        writer.add_page(pageObj)

    # Write the rotated pages to the new PDF file
    with open(newFileName, 'wb') as newFile:
        writer.write(newFile)



def main():

    # original pdf file name
    origFileName = 'Nnnnnn.pdf'

    # new pdf file name
    newFileName = 'rotated_example.pdf'

    # rotation angle
    rotation = 270

    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)

if __name__ == "__main__":
    # calling the main function
    main()