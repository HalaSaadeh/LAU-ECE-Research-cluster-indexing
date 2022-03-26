from tika import parser

def extractFrom(file):
    '''
    Extract the textual content from files.
    
    Args:
        - file: local path to the file
    Returns:
        - the textual content from the file
    '''
    parsed_pdf = parser.from_file("D:\Research\SDG Corpus\goal_1.pdf")
    file_content = parsed_pdf['content'] 
    print(file_content)
    
    print('File extracted!')
    return file_content

extractFrom("test")
