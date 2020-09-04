import sys, os
root = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
modelnet_root = os.path.join(root, "tensorflow", "script", "dataset", "ModelNet40", "ModelNet40.points")
print(modelnet_root)
import vtk

iren = vtk.vtkRenderWindowInteractor()
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

renWin = vtk.vtkRenderWindow()
renWin.SetSize(1000, 1000)
iren.SetRenderWindow(renWin)

ren = vtk.vtkRenderer()
ren.SetBackground(1, 1, 1)
renWin.AddRenderer(ren)


def MakeActor(polydata):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor

if __name__ == "__main__":
    
    print("Check Dataset")

    sample_data_path = os.path.join(modelnet_root, "airplane", "train", "airplane_0001.upgrade.smp.points")
    
    print(sample_data_path)
    exit()


    sphere = vtk.vtkSphereSource()
    sphere.Update()

    polydata = sphere.GetOutput()


    actor = MakeActor(polydata)

    ren.AddActor(actor)

    renWin.Render()


    iren.Initialize()
    iren.Start()
