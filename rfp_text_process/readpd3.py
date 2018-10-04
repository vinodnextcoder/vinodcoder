import pdftotext
import sys,re,requests
reload(sys)
sys.setdefaultencoding( "utf-8" )
with open("CRM_EDW_RFP.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
# for page in pdf:
#     print(page)
#     data=page.split("\n")

#     f=open("vinod.txt","a")
#     f.write(str(page))
#     f.close()
    
for i in range(1,5):
    f=open("tablecontent","a")
    f.write(str(pdf[i]))
    f.close()
    
    #print pdf[i]
# Just read the second page


# Or read all the text
