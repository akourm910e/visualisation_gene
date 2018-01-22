# Powered by Python 3.5



# To cancel the modifications performed by the script

# on the current graph, click on the undo button.



# Some useful keyboards shortcuts : 

# * Ctrl + D : comment selected lines.

# * Ctrl + Shift + D : uncomment selected lines.

# * Ctrl + I : indent selected lines.

# * Ctrl + Shift + I : unindent selected lines.

# * Ctrl + Return : run script.

# * Ctrl + F : find selected text.

# * Ctrl + R : replace selected text.

# * Ctrl + Space : show auto-completion dialog.



from tulip import tlp

import math



# The updateVisualization(centerViews = True) function can be called

# during script execution to update the opened views



# The pauseScript() function can be called to pause the script execution.

# To resume the script execution, you will have to click on the "Run script " button.



# The runGraphScript(scriptFile, graph) function can be called to launch

# another edited script on a tlp.Graph object.

# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)



# The main(graph) function must be defined 

# to run the script on the current graph

###################################################################################
 # LABEL 
 # SIZE 
 # SHAPE
 # COLOR
###################################################################################

def defineGraph(graph, Locus, viewLabel, viewColor, viewSize, Positive, Negative):
 for n in graph.getNodes():

   viewLabel[n] = str(Locus[n])
   #viewShape[n] = 
   viewSize[n] = tlp.Size(1,2,3)

 for n in graph.getEdges():
   if ((Positive[n]==True) and (Negative[n]==False)):
     viewColor[n] = tlp.Color.Blush
   elif ((Positive[n]==False) and (Negative[n]==True)):
     viewColor[n] = tlp.Color.Sapphire
   elif ((Positive[n]==True) and (Negative[n]==True)):
     viewColor[n] = tlp.Color.Orange
   elif ((Positive[n]==False) and (Negative[n]==False)):
     viewColor[n] = tlp.Color.Green

####################################################################################
# dessin de graph -  
#utiliser le modÃÂ¨le de forces, justification: modÃÂ¨le qui marche le mieux Ã proiri
#a adapter selon expression des facteurs pour bonus

#################################################################################### 
def algoGraph(graph, viewLayout):
   fm3pParams = tlp.getDefaultPluginParameters("FM^3 (OGDF)", graph)
   fm3pParams["Unit edge length"] = 50
   graph.applyLayoutAlgorithm("FM^3 (OGDF)", viewLayout, fm3pParams)


 
#####################################################################################
 #ÃÂcrire lÃ¢ÂÂalgorithme permettant de construire un graphe complet dont les sommets

 # sont les sommets du rÃÂ©seau initial et les poids associÃÂ©s aux arÃÂªtes correspondent
 ##################################################################################### 
def completeGraph(graph):
  for n in graph.getNodes():
    for m in graph.getNodes():
      if (n!=m):
        edges=graph.existEdge(n,m, False)
        #print(edges.isValid())
       
        if edges.isValid()==False:
          graph.addEdge(n,m)
          print("inside")
        
  
 
def filtrateEdges(graph, tp):
 x =[]
 y =[]
 node1=[]
 for n in graph.getEdges():
   source = graph.source(n)
   target = graph.target(n)
   node1=[]
   for i in tp:
     node1.append(i[source])
     #y.append(i[target])
   x.append(node1)
     
    
 print (x)
 
  
########### PEARSON CALCUL ##############
def average(x):

 assert len(x) > 0

 return float(sum(x)) / len(x)



def pearsonCoeff(x, y):

 assert len(x) == len(y)

 n = len(x)

 assert n > 0

 avg_x = average(x)

 avg_y = average(y)

 diffprod = 0

 xdiff2 = 0

 ydiff2 = 0

 for idx in range(n):
  
   xdiff = x[idx] - avg_x
    
   ydiff = y[idx] - avg_y
  
   diffprod += xdiff * ydiff
  
   xdiff2 += xdiff * xdiff
  
   ydiff2 += ydiff * ydiff
  


 return diffprod / math.sqrt(xdiff2 * ydiff2)



def main(graph): 

 Locus = graph.getStringProperty("Locus")

 Negative = graph.getBooleanProperty("Negative")

 Positive = graph.getBooleanProperty("Positive")

 tp1_s = graph.getDoubleProperty("tp1 s")

 tp10_s = graph.getDoubleProperty("tp10 s")

 tp11_s = graph.getDoubleProperty("tp11 s")

 tp12_s = graph.getDoubleProperty("tp12 s")

 tp13_s = graph.getDoubleProperty("tp13 s")

 tp14_s = graph.getDoubleProperty("tp14 s")

 tp15_s = graph.getDoubleProperty("tp15 s")

 tp16_s = graph.getDoubleProperty("tp16 s")

 tp17_s = graph.getDoubleProperty("tp17 s")

 tp2_s = graph.getDoubleProperty("tp2 s")

 tp3_s = graph.getDoubleProperty("tp3 s")

 tp4_s = graph.getDoubleProperty("tp4 s")

 tp5_s = graph.getDoubleProperty("tp5 s")

 tp6_s = graph.getDoubleProperty("tp6 s")

 tp7_s = graph.getDoubleProperty("tp7 s")

 tp8_s = graph.getDoubleProperty("tp8 s")

 tp9_s = graph.getDoubleProperty("tp9 s")

 viewBorderColor = graph.getColorProperty("viewBorderColor")

 viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")

 viewColor = graph.getColorProperty("viewColor")

 viewFont = graph.getStringProperty("viewFont")

 viewFontSize = graph.getIntegerProperty("viewFontSize")

 viewIcon = graph.getStringProperty("viewIcon")
 
 viewLabel = graph.getStringProperty("viewLabel")

 viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")

 viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")

 viewLabelColor = graph.getColorProperty("viewLabelColor")

 viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")

 viewLayout = graph.getLayoutProperty("viewLayout")

 viewMetric = graph.getDoubleProperty("viewMetric")

 viewRotation = graph.getDoubleProperty("viewRotation")

 viewSelection = graph.getBooleanProperty("viewSelection")
 
 viewShape = graph.getIntegerProperty("viewShape")


 viewSize = graph.getSizeProperty("viewSize")

 viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")

 viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")

 viewTexture = graph.getStringProperty("viewTexture")

 viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")

 viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")

 viewWeight = graph.getDoubleProperty("viewWeight")
 
 tp = [tp1_s,tp10_s,tp11_s,tp12_s,tp13_s,tp14_s,tp15_s,tp16_s,tp17_s,tp2_s,tp13_s,tp4_s,tp5_s,tp6_s,tp7_s,tp8_s,tp9_s]
 
 defineGraph(graph, Locus, viewLabel, viewColor, viewSize, Positive, Negative)
 algoGraph(graph, viewLayout)
 completeGraph(graph)
 



