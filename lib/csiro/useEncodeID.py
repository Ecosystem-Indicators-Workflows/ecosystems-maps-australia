#!/usr/bin/env python3
'''
Examples of using encodeIdentifier()
'''


from encodeID import *
# or you could use:
# from encodeID import encodeIdentifier

#=================================
# Web Service V1 (DEPRECATED!)
# https://ws.data.csiro.au/
#=================================
#https://ws.data.csiro.au/ implicit


print("https://ws.data.csiro.au. explicit")
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE", version=1)
print(identifier)
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE",
                      baseURL="https://ws.data.csiro.au/")
print(identifier)
print("\n")

print("contstruct a ws.data.csiro.au URL")
baseURL = "https://ws.data.csiro.au/"
endpoint = "collections/{identifier}"
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE", version=1)
url = baseURL + endpoint.replace("{identifier}", identifier)
print(url)
print("\n")

#=================================
# Web Service V2
# https://data.csiro.au/dap/ws/v2/
#=================================
print("https://data.csiro.au/dap/ws/v2/ implicit")
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE")
print(identifier)
print("\n")

print("https://data.csiro.au/dap/ws/v2/ explicit")
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE", version=2)
print(identifier)
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE",
                      baseURL="https://data.csiro.au/dap/ws/v2/")
print(identifier)
print("\n")

print("contstruct a /ws/v2 URL")
baseURL = "https://data.csiro.au/dap/ws/v2/"
endpoint = "collections/{identifier}"
identifier = encodeIdentifier("https://doi.org/10.4225/08/563869A931CFE", version=2)
url = baseURL + endpoint.replace("{identifier}", identifier)
print(url)