from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):

		Topo.__init__(self)

		host_1 = self.addHost('h1')
		host_2 = self.addHost('h2')
		host_3 = self.addHost('h3')
		host_4 = self.addHost('h4')
		host_5 = self.addHost('h5')
		host_6 = self.addHost('h6')
		switch_4 = self.addSwitch('s4')
		switch_3 = self.addSwitch('s3')
		switch_2 = self.addSwitch('s2')
		switch_1 = self.addSwitch('s1')

		self.addLink(switch_1, host_1)
		self.addLink(switch_1, host_2)
		self.addLink(switch_1, host_3)
		self.addLink(switch_3, host_4)
		self.addLink(switch_4, host_5)
		self.addLink(switch_4, host_6)

                self.addLink(switch_1, switch_2)
		self.addLink(switch_2, switch_3)
		self.addLink(switch_2, switch_4)

topos = {'mytopo':(lambda:MyTopo())}
