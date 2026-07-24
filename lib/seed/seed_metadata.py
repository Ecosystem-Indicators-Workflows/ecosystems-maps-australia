#!/usr/bin/env python3
'''
A function to get get metadata from the SEED portal
'''
import urllib
import urllib.request, json 
from IPython.display import Markdown

def md_download(metadata_url):
    '''
    Simple function to download metadata from seed
    '''
    with urllib.request.urlopen(metadata_url) as url:
        metadata = json.load(url)
        if (metadata['success']):
            print("Metadata successfully downloaded")
        return(metadata)

def md_desc(metadata, show_keys = ['title','lineage']):
    '''
    Simple function to print basic from seed
    '''
    for keyname in show_keys:
        if keyname in metadata['result'].keys():
            mdtext = Markdown("**{}**\n\n{}\n\n".format(keyname, metadata['result'][keyname]))
            display(mdtext)
    for resource in metadata['result']['resources']:
        mdtext = Markdown("**{}**: {} -- [{}]({})".format(resource['name'], resource['description'], resource['format'], resource['url']))
        display(mdtext)

        
if(__name__ == "__main__"):
    _testEncodeIdentifier()