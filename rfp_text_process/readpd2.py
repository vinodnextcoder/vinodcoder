import pdftotext
import sys,re,requests
reload(sys)
sys.setdefaultencoding( "utf-8" )
with open("FINAL RFP.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
for page in pdf:
    print(page)
    data=page.split("\n")

    f=open("makrand.txt","a")
    f.write(str(page))
    f.close()
    
# Just read the second page


# Or read all the text
