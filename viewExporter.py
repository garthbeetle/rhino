import rhinoscriptsyntax as rs


eType = rs.GetString(message = "Input the view filter!")
eViews = []
eLayerStates = []
fileFolder = r'C:\Users\s-rasher\Desktop\coxoption'
plugin = rs.GetPlugInObject("Rhino Bonus Tools")
if plugin is not None:
    eViews = rs.NamedViews()
    eLayerStates = plugin.LayerStateNames()
    for i in range(len(eViews)):
        if eType in eViews[i]:
            rs.RestoreNamedView(eViews[i])
            for j in range(len(eLayerStates)):
                plugin.RestoreLayerState(eLayerStates[j])
                imgDrop = '"' + fileFolder + str(eType) + str(i) + str(j) + '.png"'
                rs.Command("-_ViewCapturetoFile " + imgDrop + " Width=2000 Height=1500 Scale=1 DrawGrid=No DrawWorldAxes=No DrawCPlaneAxes=No TransparentBackground=No" + " _Enter")
