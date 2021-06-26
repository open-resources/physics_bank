# Author: Firas Moosvi
# Date: 2021-06-20

import pathlib
import os
import problem_bank_scripts as pbs
import altair as alt
import pandas as pd
import yaml
import urllib.parse

from collections import Counter

if __name__ == '__main__':

    source_root = 'content/public/'

    ## Analytics

    questions = []
    for root, dirs, files in os.walk(source_root):
        for file in files:
            if(file.endswith(".md")):
                questions.append(os.path.join(root,file))

    question_dict = {}

    topics = []

    for i,q in enumerate(questions):

        try: 
            mdtext = pathlib.Path(q).read_text(encoding='utf8')

            # Deal with YAML header
            header_text = mdtext.rsplit('---\n')[1]
            header = yaml.safe_load('---\n' + header_text)
        except:
            print(f'Problem in question: {q}')

            raise
        
        question_dict[f"Q{i}"] = {}
        question_dict[f"Q{i}"]['title'] = header['title']
        question_dict[f"Q{i}"]['topic'] = header['topic']
        question_dict[f"Q{i}"]['outcomes'] = header['outcomes']
        
        topics.append(header['topic'])

    df = pd.DataFrame(dict(Counter(topics)),index=['Count']).T.reset_index()
    df = df.rename(columns={'index':'Topic'})

    ## Create plot of questions by topic
    chart = alt.Chart(df).mark_bar().encode(alt.Y('Topic',sort='-x',title=''),alt.X('Count')).properties(title=f'Questions by Topic (N={len(df.index)}')
    chart.save('images/topics.png',webdriver='firefox',scale_factor=2)

    ## Write Table of links file
    table = f"# Question Index \n \n \n | Question | Public HTML | Public MD | Instructor MD | PL |\n| --------- | --------- | --------- | --------- | --------- |\n"

    for i,q in enumerate(questions):

        html_pub = f"https://firas.moosvi.com/oer/physicsbank/content/"+q.replace('.md','.html')
        gh_pub = f"https://github.com/open-resources/physics_bank/blob/main/content/"+q
        gh_ins = f"https://github.com/open-resources/instructor_physics_bank/blob/main/output/"+q.replace('public','instructor')


        url_html_pub = f"[Q {i+1}]({urllib.parse.quote(html_pub,safe='/:')})"
        url_gh_pub = f"[Q {i+1}]({urllib.parse.quote(gh_pub,safe='/:')})"
        url_gh_ins = f"[Q {i+1}]({urllib.parse.quote(gh_ins,safe='/:')})"
        table += f'''{i+1} |  {url_html_pub}| {url_gh_pub} | {url_gh_ins} | [TBD]() | \n'''

    pathlib.Path("content/index.md").write_text(table)
