import os

os.system('sudo mn --custom ~/merge/mergeTopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6653 --mac --nat')
