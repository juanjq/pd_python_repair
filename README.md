# pdf_python_repair
A script to edit pdfs in different ways. Installed with,
```
import httpimport
with httpimport.remote_repo(['pdfpy'], 'https://raw.githubusercontent.com/juanjq/pdfpy/main'):
     import pdf_python_repair
```
For this we need installed `PyPDF2`, using `pip install PyPDF2`

And the functions that include are,

## `repair(file_name)`

Repair the pdf because when saving images in python the archive needs to be repaired. For using it we need to input the file name,

* `file_name=` The name and direction of the file

```
pdf_python_repair.repair(file_name)
```


## `merge(pdf_order, name_merged)`

Merge a set of pdfs in one,

* `pdf_order=` A list with the pdf names in the order to be saved.
* `name_merged` Name to save the total merged pdf, by default, `merged_pdf.pdf`

```
pdf_python_repair.merged(pdf_order)
```


