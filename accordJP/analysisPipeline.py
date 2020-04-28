
import sys
import shlex 
import subprocess as sp


def launchModelStep (filepath, phenotype = "pheno_data.txt"):
    print ("****** Begin JOB:' " + str(filepath) + "'")

    #print 'Number of arguments', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)


    #for path in filepath :
    print ('*************************************')
    print ('Current working path:', str(filepath))

    ## Create system command

    cmd = "sbatch -p standard -o " + filepath + "/model_setup_step1.out ./bin/model_setup_step1.sh  " + filepath + " " +   str(phenotype)
    print (cmd)
    sp.call(cmd,  shell=True)
    print ("Launching model setup step 1:" +  cmd)

        #dout=log_file,stderr=logerr_file)

    print ("*************************************")
    print ("******* End JOB: model step 1")
    print ("*************************************\n")




def launchModelStep1 (root, filepath, phenotype = "pheno_data.txt"):
    print ("****** Begin JOB:' " + str(filepath) + "'")

    #for path in filepath :
    print ('*************************************')
    print ('Current working path:', str(filepath))

    ## Create system command

    path =  root + "/" + filepath
    cmd = "sbatch -p standard -o " + path + "/model_setup_step1.out " + path + "/bin/model_setup_step1.sh " + path +  str(phenotype)
    print (cmd)
    print ("Launching model setup step 1:" +  cmd)
    sp.call(cmd)
    print ("*************************************")
    print ("******* End JOB: model step 1")
    print ("*************************************\n")
