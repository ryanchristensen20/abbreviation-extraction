# Extraction of abbreviation-definition pairs

## Version: 0.2.6

Tellic forked version: drops checks for sentence structure containing balanced parenthesis and brackets.

This is a Python3 implementation of the [Schwartz-Hearst algorithm](https://psb.stanford.edu/psb-online/proceedings/psb03/schwartz.pdf)
for identifying abbreviations and their corresponding definitions in free text[1].
    
## Installation as a module

    python3 setup.py install
    
or

    pip install abbreviations
    
### Usage

    from abbreviations import schwartz_hearst
    
    # By default, the most recently encountered definition for each term is returned
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text='The emergency room (ER) was busy')
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(file_path='<path_to_file>')
    
    # If multiple definitions are encountered for each term, you might want to return the most common for each
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text='...', most_common_definition=True)
    
    # ... or you might want to return the first encountered definition for each
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text='...', first_definition=True)

[1] A. Schwartz and M. Hearst (2003) A Simple Algorithm for Identifying Abbreviations Definitions in Biomedical Text.
Biocomputing, 451-462.
