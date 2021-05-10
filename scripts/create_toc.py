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
    
    path = pathlib.Path('content/public/') / "**/*.md"

    # Find problems using glob and set topics 

    problems = sorted(glob.glob(str(path), recursive=True))

    problems = [p.strip('.md') for p in problems]
    topics = [p.split('/')[2] for p in problems]

    # YAML load the template toc

    toc = pathlib.Path('toc_template.yml').read_text()
    toc_dicts = yaml.safe_load(toc)

    # Populate the TOC
    dict_list = []

    for topic in topics:
        temp_dict = {'part': topic.split('.')[1],
                    'chapters': [{'file': p} for p in problems]}
        
        dict_list.append(temp_dict)

    # Add the dict_list with problem TOC to the template TOC
    toc_dicts.extend(dict_list)

    # Save the YAML dump to a file
    new_toc = yaml.dump(toc_dicts,sort_keys=False,default_flow_style=False)

    pathlib.Path('_toc.yml').write_text(new_toc)

if __name__ == '__main__':
    main()