from retrieval.main import get_context
from prompts import layoutPrompt

# use langchain and ingested paper to query for what the jupyter notebook layout should look like
# create functino decorato
def getLayout(arxiv_link: str):
    """
    getLayout(url: str) -> layout: list[str]
    """
    return get_context(arxiv_link, layoutPrompt)

## for each portion of the layout, generate a simple prompt that can be used to query langchain
def getSectionPrompt(section: str):
    """
    getSectionPrompt(section: str) -> prompt: str
    """
    return

### for each section of the layout, query langchain to get the portions of the paper that are most relevant to that code section
def getSectionContext(prompt: str):
    """
    getSectionContext(prompt: str) -> context: str
    """
    return

#### for each code section and provided context, generate the code for that section
def getSectionCode(section: str, context: str):
    """
    getSectionCode(section: str, context: str) -> code: str
    """
    return

##### for each code section, check formatting, correctness, etc.
def checkSectionCode(code: str):
    """
    checkSectionCode(code: str) -> code: str
    """
    return

# stitch together and markup all of the code sections to create the final jupyter notebook
def stitchNotebook(layout: list[str], code: list[str]):
    """
    stitchNotebook(layout: list[str], code: list[str]) -> notebook: str
    """
    return

# check formatting, correctness, etc. of the final jupyter notebook
def checkNotebook(notebook: str):
    """
    checkNotebook(notebook: str) -> notebook: str
    """
    return

# save the stitched together code as a jupyter notebook
def saveNotebook(notebook: str):
    """
    saveNotebook(notebook: str) -> none
    """
    return


