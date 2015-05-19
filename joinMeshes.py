import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
import System.Guid, System.Drawing.Color

layernames = rs.GetLayers()

for layer in layernames:
    rs.CurrentLayer(layer)
    objs = scriptcontext.doc.Objects.FindByLayer(layer)
    meshes = []
    for obj in objs:
        if rs.IsMesh(obj):
            meshes.append(obj)
    mesh = rs.JoinMeshes(meshes, delete_input = True)
