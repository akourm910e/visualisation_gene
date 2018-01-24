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
from tulip import *
from tulipogl import *
from tulipgui import *

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


#################################################################################### 
def algoGraph(graph, viewLayout):
   fm3pParams = tlp.getDefaultPluginParameters("FM^3 (OGDF)", graph)
   fm3pParams["Unit edge length"] = 50
   graph.applyLayoutAlgorithm("FM^3 (OGDF)", viewLayout, fm3pParams)


 
#####################################################################################

 ##################################################################################### 
def deleteZero(graph, tp):  
  for m in graph.getNodes() :
    myTp=[]
    for i in tp:
      myTp.append(i[m])
    if all(x==0 for x in myTp):
      graph.delNode(m)
#        graph.delNode(m) 
      
    
def completeGraph(graph):
  for n in graph.getNodes():
    for m in graph.getNodes():
      if (n!=m):
        edges=graph.existEdge(n,m, False)
        #print(edges.isValid())
       
        if edges.isValid()==False:
          graph.addEdge(n,m)
         

        
  
 
def filtrateEdges(graph, tp, viewWeight):
 #selectionner nodes des genes non exprimes

 #selectionner edges
 for n in graph.getEdges():
   source = graph.source(n)
   target = graph.target(n)
   node1=[]
   node2=[]
   for i in tp:
     node1.append(i[source])
     node2.append(i[target])
   viewWeight[n]=pearsonCoeff(node1, node2)
   if (-0.2>viewWeight[n]>0.2):
     graph.delEdge(n)
     
   
     

 
  
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
 
 tp = [tp1_s,tp2_s,tp3_s,tp4_s,tp5_s,tp6_s,tp7_s,tp8_s,tp9_s,tp10_s,tp11_s,tp12_s,tp13_s,tp14_s,tp15_s,tp16_s,tp17_s]
 
 defineGraph(graph, Locus, viewLabel, viewColor, viewSize, Positive, Negative)
# algoGraph(graph, viewLayout)
# completeGraph(graph)
 deleteZero(graph, tp)
# filtrateEdges(graph, tp, viewWeight)



#heat map
 listeNodes = []
 for i in graph.getNodes():
   listeNodes.append(i)
   
 myMap = graph.addSubGraph("map")
 viewBorderColor = myMap.getColorProperty("viewBorderColor")
 viewBorderWidth = myMap.getDoubleProperty("viewBorderWidth")
 viewColor = myMap.getColorProperty("viewColor")
 viewLayout = myMap.getLayoutProperty("viewLayout")
 viewShape = myMap.getIntegerProperty("viewShape")
 viewSize = myMap.getSizeProperty("viewSize")
 viewShape.setAllNodeValue(4) #des rectangles
 viewBorderWidth.setAllNodeValue(1.) # avec une bordure d'epaisseur 1
 viewBorderColor.setAllNodeValue(tlp.Color(0,0,0))	
 Locus=myMap.getStringProperty("Locus")
 Expression=myMap.getDoubleProperty("Expression")

 nodes_map={}
#inverser lignes et colonnes + ajouter couleur
 for i in range(0, 1105):
   nodes_map[i]= {}
   for j in range (0,17):
     monLocus = Locus[listeNodes[i]]
     monTp = tp[j]
     monExpression = monTp[listeNodes[i]]
     myProperties={}
     myProperties["Locus"]=monLocus
     myProperties["Expression"]=monExpression
     #print(monLocus, " - ", monExpression)
     nodes_map[i][j]= myMap.addNode(propertiesValues=myProperties)
 for i in range(0,1105):
   for j in range(0,17):
     n = nodes_map[i][j]
     if(i!=0):
       myMap.addEdge(nodes_map[i-1][j], n)
     if(j!=0):
       myMap.addEdge(nodes_map[i][j-1], n)
 
 params = tlp.getDefaultPluginParameters("FM^3 (OGDF)", myMap)
 params["Egde Length Property"] = 2
 success = myMap.applyLayoutAlgorithm('FM^3 (OGDF)', viewLayout, params)
 
 X = -1
 for ligne in nodes_map:
	 X += 1
	 Y = 0
	 for n in nodes_map[ligne]:
	  viewLayout[nodes_map[ligne][n]] = tlp.Coord(X*2, Y*2, 0)
	  Y += 1
  


# Import a grid approximation (with default parameters)
graph = tlp.importGraph("Grid Approximation")

viewLayout = graph.getLayoutProperty("viewLayout")
viewSize = graph.getSizeProperty("viewSize")
viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
viewColor = graph.getColorProperty("viewColor")
viewLabel = graph.getStringProperty("viewLabel")

# Apply an FM^3 layout on it
fm3pParams = tlp.getDefaultPluginParameters("FM^3 (OGDF)", graph)
fm3pParams["Unit edge length"] = 100
graph.applyLayoutAlgorithm("FM^3 (OGDF)", viewLayout, fm3pParams)

# Compute an anonymous degree property
degree = tlp.DoubleProperty(graph)
degreeParams = tlp.getDefaultPluginParameters("Degree")
graph.applyDoubleAlgorithm("Degree", degree, degreeParams)

# Map the node sizes to their degree
sizeMappingParams = tlp.getDefaultPluginParameters("Metric Mapping", graph)
sizeMappingParams["property"] = degree
sizeMappingParams["min size"] = 1
sizeMappingParams["max size"] = 30
graph.applySizeAlgorithm("Metric Mapping", viewSize, sizeMappingParams)

# Create a heat map color scale
heatMap = tlp.ColorScale([tlp.Color(0, 255, 0), tlp.Color(0,0,0), tlp.Color(255, 0, 0)])

# Map the node colors to their degree using the heat map color scale
# Also set the nodes labels to their id
for n in graph.getNodes():
    viewColor[n] = heatMap.getColorAtPos((degree[n] - degree.getNodeMin()) / (degree.getNodeMax() - degree.getNodeMin()))
    viewLabel[n] = str(n.id)

# Add a border to edges
viewBorderWidth.setAllEdgeValue(1)

# Create a Node Link Diagram view and set some rendering parameters
nodeLinkView = tlp.addNodeLinkDiagramView(graph)
renderingParameters = nodeLinkView.getRenderingParameters()
renderingParameters.setViewArrow(True)
renderingParameters.setMinSizeOfLabel(20)
nodeLinkView.setRenderingParameters(renderingParameters)
