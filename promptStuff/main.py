import validators


# ensures the url is properly formatted
def validateUrlFormat(url: str):
    """
    validateUrlFormat(url: str) -> bool
    """
    # check if the url is a string
    if not isinstance(url, str):
        return False
    # check if the url is a valid url
    if not validators.url(url):
        return False
    
    return True
        

# use langchain and ingested paper to query for what the jupyter notebook layout should look like
# create functino decorato
def getLayout(url: str):
    """
    getLayout(url: str) -> layout: list[str]
    """
    return

## for each portion of the layout, generate a simple prompt that can be used to query langchain
def getSectionPrompt(section: str):
    """
    getSectionPrompt(section: str) -> prompt: str
    """
    return

### for each prompt, query langchain to get the portions of the paper that are most relevant to that code section
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


# main function
def main(url: str):
    """
    main(url: str) -> none
    """
    # get the layout of the jupyter notebook
    layout = getLayout(url)
    # for each section of the layout, generate the code for that section
    code = []
    for section in layout:
        # get the prompt for the section
        prompt = getSectionPrompt(section)
        # get the context for the section
        context = getSectionContext(prompt)
        # get the code for the section
        code.append(getSectionCode(section, context))
    # stitch together and markup all of the code sections to create the final jupyter notebook
    notebook = stitchNotebook(layout, code)
    # check formatting, correctness, etc. of the final jupyter notebook
    notebook = checkNotebook(notebook)
    # save the stitched together code as a jupyter notebook
    saveNotebook(notebook)
    return