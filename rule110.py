#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = (
  '/rule110/(.+)','rule110',
  '/rule110/','rule110',
  '/','rule110',
       )

z = '0' #zero symbol
o = '1' #one symbol

rules = {
  '000':'0',
  '001':'1',
  '010':'1',
  '011':'1',
  '100':'0',
  '101':'1',
  '110':'1',
  '111':'0'
        }

# Customizations
# uncomment this section to change
# the symbols to be printed 
'''
z = ' ' #zero symbol
o = '#' #one symbol

rules = {
  '%s%s%s'%(z,z,z):z,
  '%s%s%s'%(z,z,o):o,
  '%s%s%s'%(z,o,z):o,
  '%s%s%s'%(z,o,o):o,
  '%s%s%s'%(o,z,z):z,
  '%s%s%s'%(o,z,o):o,
  '%s%s%s'%(o,o,z):o,
  '%s%s%s'%(o,o,o):z
        }
'''

class rule110:
  
  def GET(self,iters='50'):
    #set failsafe argument
    try:
      iterations = int(iters)
    except: iterations = 50

    #generate first state
    state  = z*iterations+o
    output = [state]
    
    #for each row
    for row in xrange(iterations):
      line = []
      #for each character
      for i in xrange(iterations+1):
        #get the triplet from neighbor cells. Use zero if not applicable.
        point = ''.join([state[i-1] if i>0 else z, state[i], state[i+1] if i<iterations else z])
        #add next state to the line according to the rules
        line.append(rules[point])
      #concat line and append to output
      output.append(''.join(line))
      #update the current state
      state = output[-1]
    
    #generate html page
    return '''
<html>
  <head> <title>Rule 100 | %d iterations</title> 
         <!--Pretty printing-->
         <style>
           body { line-height:0.5; }
           pre  { font-style:normal; font-size:0.2em; font-family:"Lucida Console"; }
         </style>
  </head>
  <body>
    <pre>%s</pre>
  </body>
</html>
           '''%(iterations,'\n'.join(output))

if __name__ == "__main__": 
  # fcgi configuration
  # uncomment the next line if you use fast-cgi
  #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
  app = web.application(urls, globals())
  app.run()        
