# Author: Firas Moosvi
# Date: 2021-05-09

"""Create Table of Contents

Usage: 
    create_toc.py [path]
"""

from docopt import docopt
import yaml
import pathlib
import glob

def main():
    #args = docopt(__doc__)

    # # Select default path if no path is provided
    # if args['[path]']:
    #     path = pathlib.Path(args['[path]'])
    # else:
    
    path = pathlib.Path('content/public/')

    # Get all the md files in the bank
    files = list(path.glob("**/*.md"))

    # Extract topics from the file names
    topics = sorted(set([file.parts[2] for file in files]))

    # YAML load the template toc

    toc = pathlib.Path('scripts/toc_template.yml').read_text()
    toc_dicts = yaml.safe_load(toc)

    # Populate the TOC
    dict_list = []

    for topic in topics:
        
        # get all questions for a particular topic
        topic_questions = sorted([str(f).split('.md')[0] for f in files if f.parts[2]==topic])
        
        temp_dict = {'caption': topic.split('.')[1],
                    'chapters': [{'file': p} for p in topic_questions]}

        dict_list.append(temp_dict)

    # Add the dict_list with problem TOC to the template TOC
    toc_dicts['parts'].extend(dict_list)

    # Save the YAML dump to a file
    new_toc = yaml.dump(toc_dicts,sort_keys=False,default_flow_style=False)

    pathlib.Path('_toc.yml').write_text(new_toc)

if __name__ == '__main__':
    main()
