import os
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

# Open the PDF file in read-binary mode
with open('route.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PdfFileReader(file)

    # Iterate over each page
    for page in range(pdf.getNumPages()):
        # Get the page object
        current_page = pdf.getPage(page)

        # Extract the text from the page
        text = current_page.extractText()

        # Split the text into a list of words
        words = text.split()

        # Iterate over each word
        for i, word in enumerate(words):
            # Check if the word has more than 3 letters
            if len(word) > 3:
                # Make the first 3 letters bold
                words[i] = '<b>' + word[:3] + '</b>' + word[3:]

        # Join the modified words into a single string
        modified_text = ' '.join(words)

        # Create a new page object with the modified text
        modified_page = PdfFileWriter().addBlankPage()
        modified_page.insertText(0, 0, modified_text)

        # Add the modified page to the output PDF
        output_pdf = PdfFileWriter()
        output_pdf.addPage(modified_page)

# Save the output PDF to a file
with open('modified.pdf', 'wb') as output_file:
    output_pdf.write(output_file)
