from mininet.net import Mininet
from mininet.node import OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

N=int(sys.argv[1])
M=int(sys.argv[2])

def emptyNet():

    net = Mininet( controller=OVSController , link=TCLink)

    net.addController( 'c0' )
    print 'Controller Added\n'
    e=1
    o=1
    hosts=[]
    switches=[]
    e_ip='11.0.0.'
    o_ip='11.0.1.'
    print '\n'
    for i in range(0,M*N):
        if i%2==0:
            hosts.append(net.addHost('host_'+str(i+1), ip=e_ip+str(e)+'/24'))
            e+=1
        else:
            hosts.append(net.addHost('host_'+str(i+1), ip=o_ip+str(o)+'/24'))
            o+=1
        print "Added host"+str(i+1)

    print '\n'

    for x in range(0,N):
        switches.append(net.addSwitch('switch_'+str(x+1)))
        print "Added switch"+str(x+1)

    print '\n'
    info( '*** Creating links\n' )

    bwidth=0
    for x in range(0,N):
        for y in range(0,M):
            net.addLink( hosts[M*x+y], switches[x] , bw=bwidth+1)
            bwidth=(bwidth+1)%2
            print "host_"+str(M*x+y+1)+"----switch_"+str(x)

    for x in range(0,N-1):
        net.addLink(switches[x],switches[x+1],bw=2)
        print "switch_"+str(x)+"-----switch_"+str(x+1)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

