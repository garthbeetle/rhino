import rhinoscriptsyntax as rs
import Rhino

doc = Rhino.RhinoDoc.ActiveDoc
activeViewport = doc.Views.ActiveView.ActiveViewport
viewport_info = Rhino.DocObjects.ViewportInfo(activeViewport)


folder = rs.BrowseForFolder(message="Browse for folder", title="Save Frames")
if folder is None: quit()

option = rs.GetString("Option Name")
scale = rs.GetString("resolution?")


width =  activeViewport.Size.Width*int(scale)
height =  activeViewport.Size.Height*int(scale)



eType = rs.GetString(message = "Input the view filter!")
vType = rs.GetString(message = "Input the layer filter!")
eViews = []
eLayerStates = []
fileFolder = str(folder)
plugin = rs.GetPlugInObject("Rhino Bonus Tools")
if plugin is not None:
    eViews = rs.NamedViews()
    eLayerStates = plugin.LayerStateNames()
    for i in range(len(eViews)):
        rs.RestoreNamedView(eViews[i])
        if eType in eViews[i]:
            print 'yah'
            for j in range(len(eLayerStates)):
                print j
                view = str(eViews[i])
                if vType in eLayerStates[j]:
                    plugin.RestoreLayerState(eLayerStates[j])
                    rs.RestoreNamedView(eViews[i])
                    circle = rs.AddCircle([0,0,0], 2)
                    rs.DeleteObject(circle)
                    name = str(eLayerStates[j]) + option + view
                    command = "-ViewCapturetoFile \"" + fileFolder + "\\" + name + ".png\" "
                    sizeCommand = " Width=" + str(width) + " Height=" + str(height)
                    #rs.Command(" Width=1180 Height=738 Scale=1 DrawGrid=No DrawWorldAxes=No DrawCPlaneAxes=No TransparentBackground=Yes")
                    rs.Command(command + sizeCommand + " _Enter")
                print j
