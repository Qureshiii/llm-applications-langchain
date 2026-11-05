from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from docling.datamodel.pipeline_options import PipelineOptions
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize the standalone loader
loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()


print(docs[1].page_content)

