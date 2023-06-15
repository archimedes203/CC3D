
from cc3d import CompuCellSetup
        

from Epithelial2PyXMLSteppables import Epithelial2PyXMLSteppable

CompuCellSetup.register_steppable(steppable=Epithelial2PyXMLSteppable(frequency=1))


CompuCellSetup.run()
