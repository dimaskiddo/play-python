#!/usr/bin/env python3

import sys
import getopt

from pytube import YouTube

## Main Function
def main(argv):
  ## Vars for Arguments Input
  url = ''

  ## Check Is There Any Arguments When Executing
  if len(argv) == 0:
    ## If No Arguments Than Print Help and Exit
    help()

  ## Try to Parse Argments
  try:
    ## Parse Arguments
    opts, _ = getopt.getopt(argv,"u:",["url="])
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

  ## Fetch YouTube Video Meta Data from URL
  video_meta = YouTube(url)
  video_title = video_meta.title

  print("Title        :", video_title)
  print("Downloading  :")

  ## Save Video Stream in MP4 format
  print("- Video File...")
  video_filter = video_meta.streams \
                .filter(progressive=True, file_extension='mp4') \
                .order_by('resolution').desc().first()

  video_filter.download(filename=video_title+".mp4")

  ## Save Video Caption in SRT format
  ##   Still Have a BUG
  # print("- Video Caption...")
  # output_caption = video_title + '.srt'
  # video_caption = video_meta.captions['en']

  # video_caption.download(title=output_caption, srt=True)

  ## Exit With Status Code 0
  sys.exit(0)

## Print Help and Exit Function
def help():
  ## Print Helm Message
  print(sys.argv[0], "-u http://youtube.com/watch?v=2lAe1cqCOXo")

  ## Exit With Status Code 0
  sys.exit(0)

## Start Main Process
if __name__ == "__main__":
  ## Parse Any Argument to Main Function
  main(sys.argv[1:])
