from vmm import *
import sys, threading

f = open(sys.argv[1], 'r')
requestList = f.readlines()
f.close()

memorySize = int(sys.argv[2])
P = noPages = int(memorySize/pageSize)
B = noBitsForPage = int(math.log(P, 2))

for entry in requestList:
	pid, rw, vaddr = entry.split(',')
	pid = int(pid)
	rw = rw.strip()
	vaddr = vaddr.strip()
	if not process.__contains__(pid):
		processInit(pid)
	requests[pid].append((rw, vaddr))

thread_mmu = threading.Thread(target=mmu)
thread_os_scheduler = threading.Thread(target=scheduler)
thread_os_scheduler.start();
thread_mmu.start();
