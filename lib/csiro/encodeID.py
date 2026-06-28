#!/usr/bin/env python3
'''
A function to get the identifier from a Data Access Portal
persistent URL and then encode it for use in the DAP web
services.
'''

def encodeIdentifier(identifier, **kwargs):
    '''
    Take a DAP persistent URL (DOI, Handle, etc.), extract the
    identifier and then encode the slashes appropriately for
    the DAP web service.
    
    The original DAP web service (without a version number) used
    the "~" character instead of slashes.  This was changed in 
    version 2 to use URL encoded slashes "%2F"
    
    kwargs:
        baseURL     (e.g. baseURL="https://ws.data.csiro.au/")
        version     (e.g. version=2)
    
    version takes precedence over baseURL
    
    Examples:
    >>> doi = "https://doi.org/10.4225/08/59475c67be7a4"
    >>> encodeIdentifier(doi, version=1)
    '10.4225~08~59475c67be7a4'
    >>> encodeIdentifier(doi, version=2)
    '10.4225/08/59475c67be7a4'
    >>> encodeIdentifier(doi, baseURL="https://ws.data.csiro.au/")
    '10.4225~08~59475c67be7a4'
    >>> encodeIdentifier(doi, baseURL="https://data.csiro.au/dap/ws/v2/")
    '10.4225/08/59475c67be7a4'
    >>>
    '''
    
    baseURL = kwargs.get("baseURL")
    version = kwargs.get("version")
    
    if baseURL:
        if baseURL == "https://ws.data.csiro.au/":
            encodeChar = "~"
        elif baseURL == "https://data.csiro.au/dap/ws/v2/":
            encodeChar = "/"
        else:
            # default to v2 since v1 is being deprecated.
            encodeChar = "/"
    
    # specifying a version means baseURL effectively gets ignored.
    if version:
        if version == 1:
            encodeChar = "~"
        elif version == 2:
            encodeChar = "/"
        else:
            # default to v2 since v1 is being deprecated.
            encodeChar = "/"
    
    # default to v2 since v1 is being deprecated.
    if not baseURL and not version:
        version = 2
        encodeChar = "/"
    
    # Extract the ID.
    # This assumes that the URLs are from the persistent link on the DAP UI
    # collection landing pages
    # DOI URLs
    identifier = identifier.replace("https://doi.org/", "")
    identifier = identifier.replace("http://doi.org/", "")
    identifier = identifier.replace("https://dx.doi.org/", "")
    identifier = identifier.replace("http://dx.doi.org/", "")
    
    # Handle URLs
    identifier = identifier.replace("http://hdl.handle.net/", "")
    identifier = identifier.replace("https://hdl.handle.net/", "")
    identifier = identifier.replace("?index=1", "")
    
    # DAP URLs
    identifier = identifier.replace("https://data.csiro.au/dap/landingpage?pid=", "")
    identifier = identifier.replace("http://data.csiro.au/dap/landingpage?pid=", "")
    if ("https://data.csiro.au/collections/#/collection/CI" in identifier
        or "https://data.csiro.au/collections/#collection/CI" in identifier
        or "https://data.csiro.au/collections/collection/CI" in identifier
        or "https://data.csiro.au/collection/" in identifier):
        identifier = identifier.replace("https://data.csiro.au/collections/#/collection/CI", "")
        identifier = identifier.replace("https://data.csiro.au/collections/#collection/CI", "")
        identifier = identifier.replace("https://data.csiro.au/collections/collection/CI", "")
        identifier = identifier.replace("https://data.csiro.au/collection/", "")
        params = identifier.find("?")
        if params >= 0:
            identifier = identifier[:params]
    
    # What is left should be just the identifier.
    # Encode any slashes
    if version == 1:
        identifier = identifier.replace("/", encodeChar)
    
    return identifier
    
def _testEncodeIdentifier():
    testIDs = ["https://data.csiro.au/dap/landingpage?pid=csiro:5101",
               "http://hdl.handle.net/102.100.100/12320?index=1",
               "https://doi.org/10.4225/08/506102A93D1F0",
               "https://data.csiro.au/collections/collection/CIcsiro:5603v1",
               "https://data.csiro.au/collections/#collection/CIcsiro:5603v1",
               "https://data.csiro.au/collections/#/collection/CIcsiro:5603v1"]
    
    print("defaults:")
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID)
        print(collectionID)
    
    baseURL = "https://ws.data.csiro.au/"
    print("baseURL = {0}".format(baseURL))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, baseURL=baseURL)
        print(collectionID)
    
    baseURL = "https://data.csiro.au/dap/ws/v2/"
    print("baseURL = {0}".format(baseURL))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, baseURL=baseURL)
        print(collectionID)
    
    baseURL = "https://www.csiro.au"
    print("baseURL = {0}".format(baseURL))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, baseURL=baseURL)
        print(collectionID)
    
    version = 1
    print("Version = {0}".format(version))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version)
        print(collectionID)
    
    version = 2
    print("Version = {0}".format(version))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version)
        print(collectionID)
        
    version = 3
    print("Version = {0}".format(version))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version)
        print(collectionID)
        
    version = "wrong"
    print("Version = {0}".format(version))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version)
        print(collectionID)
    
    version = 2
    baseURL = "https://ws.data.csiro.au/"
    print("Version = {0}, baseURL = {1}".format(version, baseURL))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version, baseURL=baseURL)
        print(collectionID)
    
    version = 1
    baseURL = "https://data.csiro.au/dap/ws/v2/"
    print("Version = {0}, baseURL = {1}".format(version, baseURL))
    for collectionID in testIDs:
        collectionID = encodeIdentifier(collectionID, version=version, baseURL=baseURL)
        print(collectionID)
        
if(__name__ == "__main__"):
    _testEncodeIdentifier()