#!/usr/bin/python
# Demonstrating SAX-based parsing of XML
import sys
import xml.sax

class XmlReader( xml.sax.ContentHandler ):
  def __init__(self):
    xml.sax.ContentHandler.__init__(self)
    self.tagFound = False
    self.actors = []

  def startElement( self, name, attributes ):
    #print "element name:", name
    if name == 'Actor':
      self.tagFound = True
    for attribute in attributes.getNames():
      pass

  def endElement( self, name ) :
    pass

  def characters( self, content ) :
    # strip only removes spaces!
    content = content.strip()
    if self.tagFound:
      self.actors.append(str(content))
    self.tagFound = False

def main():
  print "Beginning XML processor..."
  if len(sys.argv) != 2:
    print "usaage:", sys.argv[0], "<xml file>"
    sys.exit()
  file = sys.argv[1]
  try:
    reader = XmlReader()
    xml.sax.parse ( file, reader )
    print reader.actors
  except IOError, message:
    print "Error reading file: ", message
  except xml.sax.SAXParseException, message:
    print "Error parsing file: ", message

if __name__ == "__main__":
  main()
