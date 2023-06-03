import sysenv
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.memory import ChatMessageHistory
from langchain.chains import AnalyzeDocumentChain, ChatVectorDBChain, LLMChain, SequentialChain
from langchain.document_loaders import PyMuPDFLoader
from os import path
import re
#from langchain.text_splitter import 

class PdfRepresentation():
    def __init__(self, dir: str, document_filepath: str) -> None:
        docpath = "".join([dir, document_filepath])
        if self.__checkPath__(docpath):
            self.docpath = docpath
            self.load_pdf(self.docpath)
        else:
            print(f"file {document_filepath} doesn't exist!")
            exit(-1)
   
    def __checkPath__(self, filepath: str) -> bool:
        return path.exists(filepath)
        
    def load_pdf(self, path: str)->list:
        loader = PyMuPDFLoader(path)
        data = loader.load_and_split()
        self.pages = data
        return data
    
    def getPages(self)->list:
        if self.pages is not None:
            return self.pages
        else:
            print("no data loaded from pdf yet.")
            return None

def getEmbeddings():
    pass



def main()-> None:
    my_env = sysenv.load(".env")
    filepath = input("Please enter path to PDF you want to chat to:")
    file_matches= re.split("(.*/)([a-zA-Z0-9_ \.]+)$", filepath) 
    print (f"path to file:{file_matches[1]}\nfilename: {file_matches[2]}")
    path_to_file = file_matches[1]
    filename = file_matches[2]
    my_pdf = PdfRepresentation(path_to_file, filename)
    pages = my_pdf.getPages()
    print(pages[0])









if __name__ == "__main__":
    main()
