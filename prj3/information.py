import libvirt
virt_manager = libvirt.open("qemu:///system")
print("The program is used for getting the information of the virtual machines")
print("-----------------------------------------")
IDs=virt_manager.listDomainsID()
number=len(IDs)
if number==0:
    print("There is no virtual machine open now!")
    exit()
elif number==1:
    print("There is 1 virtual machine open now!")
else:
    print("There are %d virtual machines open now!"%number)
k=0
for id in IDs:
    k+=1
    print("-----------------------------------------")
    print("Virtual Machine %d:"%k)
    vm = virt_manager.lookupByID(id)
    print ("ID of VM: %s" % (vm.UUIDString()))
    print ("Name of VM: %s" % (vm.name()))  
    state=vm.info()[0]
    if state==1:
        print ("Status of VM: running")
    elif state==3:
        print("Statue of VM: pausing")
    else:
        print("Statue of VM: stopping")
    print ("Max Memory of VM: %d MB (%d GB)" % (vm.info()[1]/1024,vm.info()[1]/1024**2))
    print ("Number of CPUs: %d" % (vm.info()[3]))
virt_manager.close()
