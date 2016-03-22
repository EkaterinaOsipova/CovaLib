import sys,os
sys.path.append(os.path.dirname(sys.argv[0]) + "/../")
from Code import *

def main(name, argv):
        if (len(argv) != 1):
                print_usage(name)
                return

        clu = Cluster.Cluster("CHEM")
        clu.runJobs(argv[0], "python $SCRIPTS/Prepare.py rec.pdb xtal-lig.pdb CYS 113 HG")

def print_usage(name):
        print "Usage : " + name + " <PDB_list_file>"


if __name__ == "__main__":
        main(sys.argv[0], sys.argv[1:])
