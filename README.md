# Mininet-fattree

In this we create a 2-stage Fat Tree network using N-port switches, where N is an input parameter to your python script running Mininet simulation. N should be an even number. 

Start topology with :

sudo mn --custom ~/mininet/custom/fattree.py --topo fattree,N 

where N is the number of ports per switch.
