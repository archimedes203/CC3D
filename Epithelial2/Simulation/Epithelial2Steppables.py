from cc3d.core.PySteppables import *
import numpy as np

class Epithelial2Steppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        
        # Use 2 CPU cores
        self.change_number_of_work_nodes(4)
        
        # Given there are 576 initial cluster IDs / cell IDs and 3 components to a cell
        # (apical, basal, nucleus), we should 
        
        # 1: cuticle
        # 2: apical
        # 3: basal
        # 4: nucleus
        ### ASSIGN APICALS, BASALS, NUCLEI TO CLUSTERS HERE
        
        # print('Initiating compartment allocation...')
        # for i in range(576):
            # for j in range(575):
                # for k in range(574):
                    
                    # print('Compartment allocation running....')
                    
                    # cell1 = self.fetch_cell_by_id(i+1)
                    # cell2 = self.fetch_cell_by_id(j+2)
                    # cell3 = self.fetch_cell_by_id(k+3)
                    
                    # cell1_type = cell1.type
                    # cell2_type = cell2.type
                    # cell3_type = cell3.type
                    
                    # cluster1 = cell1.clusterId
                    # cluster2 = cell2.clusterId
                    # cluster3 = cell3.clusterId
                    
                    # if(cell1_type == 2 and cell2_type == 3 and cell3_type ==4):
                        # self.reassign_cluster_id(cell2, cluster1)
                        # self.reassign_cluster_id(cell3, cluster1)
                    # elif (...):
                        # x = X_POSITION
                        # y = Y_POSITION
                        # size = SIZE
                        # cell = self.new_cell(self.TYPENAME)
                        # # size of cell will be SIZExSIZEx1
                        # self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                        
                        
                        
        # print('Compartment allocation complete!')
        ###################################################
        
        
        
        # Below are two scanning schemes that reveal information depending on what you're wanting to look at.
        # You can comment one (or both) out, dependning on what you need. The first scanner cycles through the
        # lattice pixel-for-pixel and prints to screen cell ID, cluster ID and cell type at each pixel.
        
        
        count = 0
        
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
                # print('---------------------')
                # print('Cell type: MEDIUM')
                # print('Cluster ID: ', cluster_id)
                # print('Cell ID: ', id)
                # print('Count: ', count)
                # print('---------------------')
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
            # else:
                # print('---------------------')
                # print('Cell type: NUCLEUS')
                # print('Cluster ID: ', cluster_id)
                # print('Cell ID: ', id)
                # print('Count: ', count)
                # print('---------------------')
        
        # Initialize counter so that scanner can count pixels
        # count = 0
        
        # for i in range(20):
            # for j in range(20):
                # for k in range(20):
                    
                    # # Update pixel counter
                    # count += 1
                    
                    # # Get cell object at pixel location i,j,k
                    # cell = self.cell_field[i, j, k]
                    
                    # # Get cluster ID of cell object at i,j,k
                    # cluster_id = cell.clusterId
                    
                    # # Get cell ID of cell object at i,j,k
                    # id = cell.id
                    
                    # # Get cell type of cell object at i,j,k
                    # cell_type = cell.type
                    
                    # print('-------------------------------')
                    # if (cell_type == 0): # Don't care about medium-type cells
                        # pass
                    # elif (cell_type == 1): # Don't care about cuticle cells here
                        # pass
                    # elif (cell_type == 2):
                        # print('Cell type: APICAL')
                    # elif (cell_type == 3):
                        # print('Cell type: BASAL')
                    # elif (cell_type == 4):
                        # print('Cell type: NUCLEUS')
                    
                    # print('Pixel: ', i,j,k)
                    # print('Cluster ID: ', cluster_id)
                    # print('Cell ID: ', id)
                    # print('Count: ', count)
                    # print('-------------------------------')

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """

        #for cell in self.cell_list:

            #print("cell.id=",cell.id)

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """
        count = 0
        
        for cell in self.cell_list:
         
                    count += 1                  
                    
                    # Grabs the ID of the cluster to which the cell at i,j,k belongs. 
                    # Again, initially, the Cluster ID = Cell ID but we want to potentially change this.
                    cluster_id = cell.clusterId
              
                    # Cell ID
                    id = cell.id
                    
                    # Get cell type at pixel                
                    cell_type = cell.type
     
                    if (cell_type == 0):
                        pass
                    elif (cell_type == 1):
                        pass
                        #print('Cell type: CUTICLE')
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
                    elif (cell_type == 4):
                        print('---------------------')
                        print('Cell type: NUCLEUS')
                        print('Cluster ID: ', cluster_id)
                        print('Cell ID: ', id)
                        print('Count: ', count)
                        print('---------------------')
                    

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
