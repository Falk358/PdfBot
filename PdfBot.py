import sysenv
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.memory import ChatMessageHistory
from langchain.chains import AnalyzeDocumentChain, ChatVectorDBChain, LLMChain, SequentialChain
from langchain.document_loaders import PyPDFLoader
#from langchain.text_splitter import 

class PdfRepl():
    def __init__(self, dir: str, document: str) -> None:
        self.docpath = "".join([dir,"/",document])
        self.load_pdf(self.docpath)
    
    def load_pdf(self, path: str)->list:
        loader = PyPDFLoader(path)
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
    my_pdf = PdfRepl("pdf_library","core_rulebook_wrath_glory.pdf")
    pages = my_pdf.getPages()
    print(pages[0])









if __name__ == "__main__":
    main()