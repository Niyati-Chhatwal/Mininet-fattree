from mininet.topo import Topo
class FatTree( Topo ):
  
    CoreSwitchList = []
    EdgeSwitchList = []
    HostList = []
 
    def __init__( self, k):
        " Create Fat Tree topo."
        self.CoreLayerSwitch = k/2
        self.EdgeLayerSwitch = k
        self.density = k/2
        self.Host =  k*k/2
        # Init Topo
        Topo.__init__(self)
  
        self.createTopo()

        self.createLink()

    def createTopo(self):
        self.createCoreLayerSwitch(self.CoreLayerSwitch)
        self.createEdgeLayerSwitch(self.EdgeLayerSwitch)
        self.createHost(self.Host)

    """
    Create Switch and Host
    """

    def _addSwitch(self, number, level, switch_list):
        for x in range(1, number+1):
            switch_list.append(self.addSwitch('s' + str(level) + str(x)))

    def createCoreLayerSwitch(self, number):

        self._addSwitch(number, 2, self.CoreSwitchList)

    def createEdgeLayerSwitch(self, number):

        self._addSwitch(number, 1, self.EdgeSwitchList)

    def createHost(self, number):
        for x in range(1, number+1):
    
            self.HostList.append(self.addHost(str("H") + str(x)))

    """
    Add Link
    """
    def createLink(self):
        for x in range(0,self.EdgeLayerSwitch):
            for i in range(0,self.CoreLayerSwitch):
                self.addLink(self.EdgeSwitchList[x],self.CoreSwitchList[i])


        for x in range(0, self.EdgeLayerSwitch):
            for i in range(0, self.density):
                self.addLink(self.EdgeSwitchList[x],self.HostList[self.density * x + i])
      
topos = { 'fattree' : ( lambda k : FatTree(k)) }
