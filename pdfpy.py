from PyPDF2                import PdfFileMerger 

def repair(file_name):
    EOF_MARKER = b'%%EOF'                                #we look for the EOF marker that is the 'End' of the actual pdf

    with open(file_name, 'rb') as f:                     #reading the pdf
        contents = f.read()

    # check if EOF is somewhere else in the file
    if EOF_MARKER in contents:
        # we can remove the early %%EOF and put it at the end of the file
        contents = contents.replace(EOF_MARKER, b'')
        contents = contents + EOF_MARKER
    else:
        contents = contents[:-6] + EOF_MARKER

    #replacing the file with same name ended by '_r'
    with open(file_name, 'wb') as f:
        f.write(contents)

        
#function to merge a list of pdfs, giving the name files of them     
def merge_pdf(pdf_order,name_merged='merged_pdf'):

      #merging pdfs
      merger = PdfFileMerger()
      for pdf in pdf_order:
          merger.append(pdf)

      #name of the merged pdf
      merger.write(name_merged+'.pdf')         #name of final file

      merger.close()  
