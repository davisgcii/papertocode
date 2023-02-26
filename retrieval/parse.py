import re

def split_sections():
    
    with open('./control.tex', 'r') as f:
      tex_string = f.read()
    
    # find all section titles and their starting index
    sections = re.findall(r'\\section{(.+?)}', tex_string, flags=re.DOTALL)
    section_indices = [match.start() for match in re.finditer(r'\\section{', tex_string)]

    # add index for end of last section
    section_indices.append(len(tex_string))

    # split string into sections and store in dictionary
    section_dict = {}
    for i in range(len(sections)):
        start = section_indices[i]
        end = section_indices[i+1]
        section_text = tex_string[start:end]
        section_title = sections[i].strip()
        section_dict[section_title] = section_text

    return section_dict


sections = split_sections()

print(sections['Introduction'])