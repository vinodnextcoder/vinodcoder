import pdftotext,os
import sys,re,requests
reload(sys)
sys.setdefaultencoding( "utf-8" )
if not os.path.exists("./ALL_TXT"):
    os.makedirs("./ALL_TXT")
dirs=os.listdir("./ALL_PDF")
for files in dirs:
    #print files
    with open("./ALL_PDF/"+files, "rb") as f:
        pdf = pdftotext.PDF(f)
        print pdf
    filename=files.replace(".pdf",".txt")
    print filename
    for i in range(1,5):
        f=open("./ALL_TXT/"+filename,"a")
        f.write(str(pdf[i]))
        f.close()

    #print pdf[0]
# Iterate over all the pages
# for page in pdf:
#     print(page)
#     data=page.split("\n")

#     f=open("vinod.txt","a")
#     f.write(str(page))
#     f.close()
    
# for i in range(1,5):
#     f=open("tablecontent","a")
#     f.write(str(pdf[i]))
#     f.close()
