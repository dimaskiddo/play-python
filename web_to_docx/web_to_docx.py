#!/usr/bin/env python3

import sys
import getopt
import urllib.request

from docx import Document
from htmldocx import HtmlToDocx

## Main Function
def main(argv):
  ## Vars for Arguments Input
  url = ''
  output = ''

  ## Check Is There Any Arguments When Executing
  if len(argv) == 0:
    ## If No Arguments Than Print Help and Exit
    help()

  ## Try to Parse Argments
  try:
    ## Parse Arguments
    opts, _ = getopt.getopt(argv,"u:o:",["url=","output="])
  except getopt.GetoptError:
    ## If There is an Error While Parsing Then
    ##   Print Help and Exit
    help()

  ## Match The Argument Parameter Then
  ##   Parse it to the Vars
  for opt, arg in opts:
    ## If There is Argument for "-u" or "--url" Then
    ##   Parse it into URL var
    if opt in ("-u", "--url"):
        url = arg
    ## If There is Argument for "-o" or "--output" Then
    ##   Parse it into Output var
    elif opt in ("-o", "--output"):
        output = arg

  ## Initialize Module
  document = Document()
  converter = HtmlToDocx()

  ## Set Request Header
  ##   Some Website Might Be Protected When There is No User-Agent We Will Get 403 Forbidden
  web_header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

  ## Set Web Request URL and Header
  web_request = urllib.request.Request(url, None, web_header)

  ## Open Web With Request GET Method
  print("Openning URL from  :", url)
  web_page = urllib.request.urlopen(web_request)

  ## Parse Web Content and Decode it to HTML UTF-8
  web_content = web_page.read().decode("utf8")

  ## Close Web Request
  web_page.close()

  ## Save Web Content HTML to Output File
  print("Saving Output to   :", output)
  converter.add_html_to_document(web_content, document)
  document.save(output)

  ## Print Task Completed and Exit
  completed()

## Function to Print Task Completed and Exit
def completed():
  ## Exit With Status Code 0
  print("")
  print("Task Completed")
  sys.exit(0)

## Print Help and Exit Function
def help():
  ## Print Helm Message
  print(sys.argv[0], "-u https://www.python.org -o python.docx")

  ## Exit With Status Code 0
  sys.exit(0)

## Start Main Process
if __name__ == "__main__":
  ## Parse Any Argument to Main Function
  main(sys.argv[1:])
