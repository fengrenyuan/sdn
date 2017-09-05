from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
		
		Topo.__init__(self)

		host_1 = self.addHost('h1')
		host_2 = self.addHost('h2')
		host_3 = self.addHost('h3')
		switch_1 = self.addSwitch('s1')
		switch_2 = self.addSwitch('s2')
		switch_3 = self.addSwitch('s3')
		switch_4 = self.addSwitch('s4')

		self.addLink(switch_3, host_1)
		self.addLink(switch_3, host_2)
		self.addLink(switch_4, host_3)
		self.addLink(switch_3, switch_2)
		self.addLink(switch_3, switch_4)
		self.addLink(switch_4, switch_1)
		self.addLink(switch_2, switch_1)

topos = {'mytopo':(lambda:MyTopo())}
