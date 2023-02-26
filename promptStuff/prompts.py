layoutPrompt = """Given the text of the Arxiv paper you now know about, can you give me a proposed structure for a Jupyter notebook that would summarize the papers key contributions and findings. The Jupyter notebook should be structured in a logical and coherent way, with sections and sub-sections that reflect the papers organization. Please assume that the Jupyter notebook will be used by someone who is familiar with the general field of AI, but may not be familiar with the specific topic of the paper. The output should be in this format:
- each section should be numbered and have a title (e.g., Training and Inference)
- each subsection should start with a dash (e.g., - Overview of the training process)

Only give the structured layout -- do not describe or discuss the paper."""

sectionPrompt = """Given the text of the Arxiv paper that you have context for, can you generate code for t
"""

