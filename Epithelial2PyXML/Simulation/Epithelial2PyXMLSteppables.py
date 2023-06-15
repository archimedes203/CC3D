from cc3d.core.PySteppables import *
import numpy as np

class Epithelial2PyXMLSteppable(SteppableBasePy):

    def __init__(self, frequency=1): ##########################################################################################################################

        SteppableBasePy.__init__(self,frequency)

    def start(self): ##########################################################################################################################
        """
        Called before MCS=0 while building the initial simulation
        """
        
        # Determine here the number of CPU cores you want to use for 
        # parallel computing (I have a maximum of 8 on the Alienware).
        self.change_number_of_work_nodes(4)
        
        
        # Run brief analysis of cell IDs, cluster IDs and cell types. This gives us 
        # an idea of whether or not the cells (which are actually cell compartments in the
        # biological sense) are being appropriately clustered by our cluster fusion algorithm.
        
        count = 0
        
        print('Assessing cell and cluster IDs for cell types APICAL, BASAL, NUCLEUS...')
        
        for cell in self.cell_list:
         
            count += 1                  
            
            # Grabs the ID of the cluster to which the cell at i,j,k belongs. 
            # Again, initially, the Cluster ID = Cell ID but we want to potentially change this.
            cluster_id = cell.clusterId
      
            # Cell ID
            id = cell.id
            
            # Get cell type at pixel                
            cell_type = cell.type
            
            # Print out info for all cells (except cuticle and medium, for now):
            
            if (cell_type == 0):
                pass
            elif (cell_type == 1):
                print('---------------------')
                print('Cell type: CUTICLE')
                print('Cluster ID: ', cluster_id)
                print('Cell ID: ', id)
                print('Count: ', count)
                print('---------------------')
            elif (cell_type == 2):
                print('---------------------')
                print('Cell type: APICAL')
                print('Cluster ID: ', cluster_id)
                print('Cell ID: ', id)
                print('Count: ', count)
                print('---------------------')
            elif (cell_type == 3):
                print('---------------------')
                print('Cell type: BASAL')
                print('Cluster ID: ', cluster_id)
                print('Cell ID: ', id)
                print('Count: ', count)
                print('---------------------')
            else:
                print('---------------------')
                print('Cell type: NUCLEUS')
                print('Cluster ID: ', cluster_id)
                print('Cell ID: ', id)
                print('Count: ', count)
                print('---------------------')
        print('Pre-simulation assessment complete!')
        # Begin clustering process here: 
        
        print('Creating iterable lists of cell IDs depending on cell types...')
        # Initialize lists to store cell IDs depending on cell type and cluster IDs.
        # Make these global variables so that you can use them in the function at the end as well.
        
        global AP, BAS, NUC, CLUST
        
        AP = [] # for storing APICAL cell IDs
        BAS = [] # for storing BASAL cell IDs
        NUC = [] # for storing NUCLEUS cell IDs
        CLUST = [] # for storing cluster IDs of each cell we iterate through
        
        
        for cell in self.cell_list:
            
            # READ/WRITE  ACCESS                
            cell_type = cell.type
            # READ ONLY ACCESS        
            cell_id = cell.id
            # READ ONLY ACCESS - can be modified using reassignClusterId function        
            cluster_id = cell.clusterId
            
            if (cell_type == 2): # if cell is APICAL, store cell ID in apical cell ID list
                AP.append(cell_id)
                CLUST.append(cluster_id)
            elif (cell_type == 3): # if cell is BASAL, store cell ID in basal cell ID list
                BAS.append(cell_id)
                CLUST.append(cluster_id)
            elif (cell_type == 4): # if cell is NUCLEUS, store cell ID in nucleus cell ID list
                NUC.append(cell_id)
                CLUST.append(cluster_id)
  
        
        print('Iterable list generation was successful!')    
        print('AP length: ', len(AP))
        print('BAS length: ', len(BAS))
        print('NUC length: ', len(NUC))
        print('CLUST length: ', len(CLUST))
        if (len(CLUST) == len(AP) + len(BAS) + len(NUC)):
            print('Nr. cluster IDs matches nr. cell IDs! :-)')
        
            
        # CLUSTER FUSION (this currently only affects portions of all ID lists that are same size)
        
        # Get size of the smallest of the three lists (AP, BAS, NUC):
        global smallest
        smallest = 0
        
        if (len(AP) < len(BAS) and len(AP) < len(NUC)):
            smallest = len(AP)
        elif (len(BAS) < len(NUC)):
            smallest = len(BAS)
        else:
            smallest = len(NUC)
            
        # Iterate through AP, BAS, NUC list portions that are of same length (i.e., as long 
        # as the smallest list of all three lists): 
        for i in range(smallest):
            
            # Grab i-th apical, basal, nucleus component 
            apical = self.fetch_cell_by_id(AP[i])
            basal = self.fetch_cell_by_id(BAS[i])
            nucleus = self.fetch_cell_by_id(NUC[i])
            
            # Re-assign basal and nucelus components to cluster already occupied by apical component. 
            self.reassign_cluster_id(basal, AP[i])
            self.reassign_cluster_id(nucleus, AP[i])
        
        
        ### NOTE: THIS PARTICULAR PORTION OF THE CODE CAUSES ERRORS WITH VARIOUS BACKGROUND PLUGINS THAT RUN IN THE SIMULATOR
        ###       THIS APPEARS TO BE BECAUSE WE'RE DELETING CELLS THAT ARE THEN LOOKED FOR BUT NOT ACCOUNTED FOR BY PLUGINS
        
        # # Mark any regions of the ID lists larger than the smallest of the
        # # three lists as 'death zones' within which any component with a cell ID there
        # # will be deleted from the lattice
        # deathAP = AP[smallest: len(AP)+1]
        # deathBAS = BAS[smallest: len(BAS)+1]
        # deathNUC = NUC[smallest: len(NUC)+1] 
        
        # # Kill all superfluous apical components
        # for j in range(len(deathAP)):
            
            # # Get cell to 'kill'
            # deadAP = self.fetch_cell_by_id(deathAP[j])
            
            # # Set target volume of cell to 0
            # # READ/WRITE  ACCESS                
            # deadAP.targetVolume = 0
            # deadAP.lambdaVolume = 0
            
        # # Kill all superfluous basal components
        # for j in range(len(deathBAS)):
            # deadBAS = self.fetch_cell_by_id(deathBAS[j])
            # deadBAS.targetVolume = 0
            # deadBAS.lambdaVolume = 0
            
            
        
        # # Kill all superfluous nucleus components
        # for j in range(len(deathNUC)):
            # deadNUC = self.fetch_cell_by_id(deathNUC[j])
            # deadNUC.targetVolume = 0
            # deadNUC.lambdaVolume = 0
            


    def step(self, mcs): ##########################################################################################################################
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """


    def finish(self): ##############################################################################################################################
        """
        Called after the last MCS to wrap up the simulation
        """
        
        # Run the analysis algorithm again to check clustering.
        
        for i in range(len(CLUST)):
            
            count = 0
            print('---------------------')
            print('Cluster ID: ', CLUST[i])
            
            for cell in self.cell_list:
                
                cluster_id = cell.clusterId
                id = cell.id
                cell_type = cell.type
                
                if (cluster_id == CLUST[i]):
                    
                    count += 1
                    if (cell_type == 2):
                        print('Cell type: APICAL')
                    elif (cell_type == 3):
                        print('Cell type: BASAL')
                    elif (cell_type == 4):
                        print('Cell type: NUCLEUS')
                    
                    print('Cell ID: ', id)
                    
            print('Count in cluster: ', count)      
            print('---------------------')
            
 

    def on_stop(self): ##########################################################################################################################
        """
        Called if the simulation is stopped before the last MCS
        """
