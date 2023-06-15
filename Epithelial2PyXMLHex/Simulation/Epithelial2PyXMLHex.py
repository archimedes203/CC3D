
from cc3d import CompuCellSetup
        

from Epithelial2PyXMLHexSteppables import Epithelial2PyXMLHexSteppable

CompuCellSetup.register_steppable(steppable=Epithelial2PyXMLHexSteppable(frequency=1))


CompuCellSetup.run()
