
def configure_simulation():

    from cc3d.core.XMLUtils import ElementCC3D
    
    CompuCell3DElmnt=ElementCC3D("CompuCell3D",{"Revision":"0","Version":"4.4.0"})
    
    MetadataElmnt=CompuCell3DElmnt.ElementCC3D("Metadata")
    
    # Basic properties simulation
    MetadataElmnt.ElementCC3D("NumberOfProcessors",{},"1")
    MetadataElmnt.ElementCC3D("DebugOutputFrequency",{},"10")
    # MetadataElmnt.ElementCC3D("NonParallelModule",{"Name":"Potts"})
    
    PottsElmnt=CompuCell3DElmnt.ElementCC3D("Potts")
    
    # Basic properties of CPM (GGH) algorithm
    PottsElmnt.ElementCC3D("Dimensions",{"x":"80","y":"80","z":"20"})
    PottsElmnt.ElementCC3D("Steps",{},"10000")
    PottsElmnt.ElementCC3D("Temperature",{},"20.0")
    PottsElmnt.ElementCC3D("NeighborOrder",{},"2")
    
    PluginElmnt=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"CellType"})
    
    # Listing all cell types in the simulation
    PluginElmnt.ElementCC3D("CellType",{"TypeId":"0","TypeName":"Medium"})
    PluginElmnt.ElementCC3D("CellType",{"Freeze":"","TypeId":"1","TypeName":"CUTICLE"})
    PluginElmnt.ElementCC3D("CellType",{"TypeId":"2","TypeName":"APICAL"})
    PluginElmnt.ElementCC3D("CellType",{"TypeId":"3","TypeName":"BASAL"})
    PluginElmnt.ElementCC3D("CellType",{"TypeId":"4","TypeName":"NUCLEUS"})
    
    PluginElmnt_1=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"Volume"})
    PluginElmnt_1.ElementCC3D("VolumeEnergyParameters",{"CellType":"CUTICLE","LambdaVolume":"2.0","TargetVolume":"50"}) # FROZEN
    PluginElmnt_1.ElementCC3D("VolumeEnergyParameters",{"CellType":"APICAL","LambdaVolume":"5","TargetVolume":"15"})
    PluginElmnt_1.ElementCC3D("VolumeEnergyParameters",{"CellType":"BASAL","LambdaVolume":"2","TargetVolume":"40"})
    PluginElmnt_1.ElementCC3D("VolumeEnergyParameters",{"CellType":"NUCLEUS","LambdaVolume":"20","TargetVolume":"0.5"})
    
    PluginElmnt_2=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"CenterOfMass"})
    
    # Module tracking center of mass of each cell
    
    PluginElmnt_3=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"NeighborTracker"})
    
    # Module tracking neighboring cells of each cell
    
    PluginElmnt_4=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"Contact"})
    # Specification of adhesion energies
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"Medium","Type2":"Medium"},"0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"Medium","Type2":"CUTICLE"},"16.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"Medium","Type2":"APICAL"},"16.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"Medium","Type2":"BASAL"},"12.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"Medium","Type2":"NUCLEUS"},"25.0")
    
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"CUTICLE"},"10.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"APICAL"},"1.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"BASAL"},"15.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"NUCLEUS"},"18.0")
    
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"APICAL"},"2.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"BASAL"},"12.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"NUCLEUS"},"25.0")
    
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"BASAL","Type2":"BASAL"},"2.0")
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"BASAL","Type2":"NUCLEUS"},"20.0")
    
    PluginElmnt_4.ElementCC3D("Energy",{"Type1":"NUCLEUS","Type2":"NUCLEUS"},"25.0")
    
    PluginElmnt_4.ElementCC3D("NeighborOrder",{},"4")
    
    PluginElmnt_5=CompuCell3DElmnt.ElementCC3D("Plugin",{"Name":"ContactInternal"})
    # Specification of internal adhesion energies
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"Medium","Type2":"Medium"},"0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"Medium","Type2":"CUTICLE"},"10.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"Medium","Type2":"APICAL"},"10.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"Medium","Type2":"BASAL"},"10.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"Medium","Type2":"NUCLEUS"},"10.0")
    
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"CUTICLE"},"0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"APICAL"},"2.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"BASAL"},"8.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"CUTICLE","Type2":"NUCLEUS"},"15.0")
    
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"APICAL"},"0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"BASAL"},"2.0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"APICAL","Type2":"NUCLEUS"},"18.0")
    
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"BASAL","Type2":"BASAL"},"0")
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"BASAL","Type2":"NUCLEUS"},"2.0")
    
    PluginElmnt_5.ElementCC3D("Energy",{"Type1":"NUCLEUS","Type2":"NUCLEUS"},"0")
    PluginElmnt_5.ElementCC3D("NeighborOrder",{},"4")
    
    SteppableElmnt=CompuCell3DElmnt.ElementCC3D("Steppable",{"Type":"UniformInitializer"})
    
    # Initial layout of cells in the form of rectangular slab
    RegionElmnt=SteppableElmnt.ElementCC3D("Region")
    RegionElmnt.ElementCC3D("BoxMin",{"x":"0","y":"0","z":"0"})
    RegionElmnt.ElementCC3D("BoxMax",{"x":"80","y":"80","z":"19"})
    RegionElmnt.ElementCC3D("Gap",{},"0")
    RegionElmnt.ElementCC3D("Width",{},"7")
    RegionElmnt.ElementCC3D("Types",{},"APICAL,BASAL,NUCLEUS")
    
    RegionElmnt=SteppableElmnt.ElementCC3D("Region")
    RegionElmnt.ElementCC3D("BoxMin",{"x":"0","y":"0","z":"19"})
    RegionElmnt.ElementCC3D("BoxMax",{"x":"80","y":"80","z":"20"})
    RegionElmnt.ElementCC3D("Gap",{},"0")
    RegionElmnt.ElementCC3D("Width",{},"7")
    RegionElmnt.ElementCC3D("Types",{},"CUTICLE")


    CompuCellSetup.setSimulationXMLDescription(CompuCell3DElmnt)    

    


        
    CompuCellSetup.setSimulationXMLDescription(CompuCell3DElmnt)

            
from cc3d import CompuCellSetup
        

configure_simulation()            

            

from Epithelial2Steppables import Epithelial2Steppable

CompuCellSetup.register_steppable(steppable=Epithelial2Steppable(frequency=1))


CompuCellSetup.run()
