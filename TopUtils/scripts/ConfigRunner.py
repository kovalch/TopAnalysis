#! /usr/bin/env python

## system imports
import os
import sys
import getopt
import threading

## timer and threading
from TopAnalysis.TopUtils.tools.Timer import Timer

## configuration
import TopAnalysis.Configuration.processes as input
import TopAnalysis.TopUtils.tools.ConfigWrapper as cms

##-----------------------------------------------------------------------------------
## executive script for cmsRun, Version 1.1
## twiki: https://twiki.cern.ch/twiki/bin/view/CMS/ConfigRunner
class CfgRunner:
    ##
    ## configurables
    ##
    
    ## output logfile
    __outputLog       = ''
    ## error  logfile
    __outputErr       = ''
    ## file service output path
    __fileServicePath = ''
    ## file service output name    
    __fileServiceName = ''
    ## cfg file for cmsRun
    __config          = ''
    ## physics process/sample
    __process         = ''
    ## event of events to process
    __numberOfEvents  = 0
    ## event of events to skip    
    __numberOfSkips   = 0
    ## verbose mode
    __verbose         = False
    ## interactive mode
    __interactive     = False    

    ##
    ## internal variables
    ##
    
    ## time in seconds to wait
    __sleeptime   = 10
    ## user defined parameters
    __userParams  = ''
    ## for interactive mode
    __runs_ = ''
    ## for cmsRun execution
    __jobStarted = False
    ## error handling
    __errorToken = ['RootError', 'Exception', 'Root_Error']

##-----------------------------------------------------------------------------------    
##  Constructor
    def __init__(self):
        self.__cmsRunTimer  = {}
        self.__analysisTimer= {}

##-----------------------------------------------------------------------------------        
##  * start sequence
    def beginJob(self):
        print "**************************************************"
        print "* starting ConfigRunner...                       *"
        print "*                                                *"
        print "*                                                *"
        print "*                                                *"    
        print "*                                                *"
        print "*                                      V00-00-00 *"
        print "**************************************************"
        
##-----------------------------------------------------------------------------------        
##  * end sequence
##  * this may contain the execution of histPlotter or something similar                
    def endJob(self):
        print "**************************************************"
        print "* leaving ConfigRunner...                        *"
        print "*                                                *"
        print "*                                                *"
        print "*                                                *"    
        print "*                                                *"
        print "*                                      Good Bye! *"
        print "**************************************************"  

##-----------------------------------------------------------------------------------
##  * Parse command line options
##  * Do basic check whether the options make sense or not
##  * Depending on the options execute 'doAll' or 'doJob'
    def main(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                                       'hvic:p:e:s:o:',
                                       ['help','verbose','interactive','cfg=','proc=','evts=','skip=','out=','path=','user=']
                                       )
        except getopt.error, msg:
            print msg
            print "for help use --help"
            sys.exit(2)

        for o, a in opts:
            if o in ("-h", "--help"):
                ################################################
                ## get help
                ################################################                
                print __doc__
                sys.exit(0)
            elif o in ("-v", "--verbose"):
                ################################################
                ## run verbose mode
                ################################################
                self.__verbose = True
            elif o in ("-i", "--interactive"):
                ################################################                
                ## run interactive mode
                ################################################                
                self.__interactive = True                
            elif o in ("-c", "--cfg"):
                ################################################                
                ## cmssw cfg file
                ################################################                
                self.__config = a
            elif o in ("-p", "--proc"):
                ################################################                
                ## process of consideration
                ################################################                
                self.__process = a
            elif o in ("-e", "--evts"):
                ################################################                
                ## number of events to be processed
                ################################################                
                self.__numberOfEvents = int(a)
            elif o in ("-s", "--skip"):
                ################################################                
                ## number of events to be skipped
                ################################################                
                self.__numberOfSkips  = int(a)                
            elif o in ("-o", "--out"):
                ################################################                
                ## define output file with process suffix
                ################################################
                if (not (a == '')):
                    self.__fileServiceName = a
            elif o in ("--path"):
                ################################################
                ## define error file with sample suffix
                ################################################                
                if (not a == ''):
                    self.__fileServicePath = a
            elif o in ("-u", "--user"):
                ################################################                
                ## add user defined parameters
                ################################################
                if (not a == ''):
                    self.__userParams = a
            else:
                self.__errorMsg()
                print '* * argument(s) not recognized. See --help for usage'

        ## check number of events
        if (self.__numberOfEvents == 0):
            self.__errorMsg()
            print '* * no events to be processed. Choose --evts to specify'
            sys.exit(1)

        ## check physics process
        if (self.__process == ''):
            self.__errorMsg()
            print '* * no physics process specified. Choose --proc to specify'
            sys.exit(1)            

        ## check configfile
        if (self.__config == ''):
            self.__errorMsg()
            print '* * no config file specified. Choose --cfg to specify'
            
        if (not os.path.exists(self.__config)):
            self.__errorMsg()
            print '* * config file doen\'t exist. Please check spelling'
            sys.exit(1)

        ## check fileServiceName
        if (self.__fileServiceName == ''):
            self.__errorMsg()
            print '* * no output name specified. Choose --out to specify'
            sys.exit(1)
            
        ## run
        if(self.__interactive):
            self.__doAll()
        else:
            self.__doJob(self.__process)
            self.__waitingForEnd(self.__process)

##-----------------------------------------------------------------------------------
##  * print head for simple error message            
    def __errorMsg(self):
        print "**************************************************"
        print "* Error:"


##-----------------------------------------------------------------------------------
##  * print message on screen
##  * used in __waitForFirst        
    def __printMsg(self, msg):
        print msg

##-----------------------------------------------------------------------------------
##  * read string from file (in read only)
##  * used in __waitForFirst                
    def __readFromFile(self, filename):
        file = open(filename, 'r')
        str = file.read()
        file.close()
        return str        

##-----------------------------------------------------------------------------------
##  * wait for the first event to be processed
##  * do some basic job monitoring
##  * estimate time elapsed to start cmsRun
##  * start runtime estimate            
    def __waitForFirst(self, process):
        printEvery = self.__sleeptime*1.3
        msg = "* * waiting for the 1st event of '" + str(process) + "' to be processed..." 
        printtimer = {}
        ## print msg up to 10 times
        for i in range(0,10):
            printtimer[i] = threading.Timer(printEvery*i, self.__printMsg, [msg])
            printtimer[i].start()
        ## wait until the files are created by cmsRun
        while(not os.path.exists(self.__outputErr)):
            Timer.sleep(1)
            ## if after 1min no file is created the script aborts
            if self.__cmsRunTimer[process].timePassed(os.times()) > 60:
                print "* * waited more then 1min for job to begin"
                print "* * aborting job..."
                os.sys.exit(1)
        ## waits until first event has been read
        while (self.__readFromFile(self.__outputErr) == ""):
            Timer.sleep(1)
            
        ## clear printtimer
        for i in printtimer:
            printtimer[i].cancel()
            
        ## make a first print out from logfile on screen
        if (self.__verbose):
            print self.__readFromFile(self.__outputErr)

        ## check for configuration file errors
        if '---- Configuration BEGIN' in self.__readFromFile(self.__outputErr):
            print '* * Configuration error; abort submission'
            os.system.exit(1)
        ## check if run started properly
        if not 'Begin processing the 1st record.' in self.__readFromFile(self.__outputErr):
            print '* * error occured; first event could not be processed in cmsRun job'
            os.system.exit(1)
        self.__cmsRunTimer[process].stop()
        ## print time to screen to get cmsRun starting
        print '* * time elapsed to start cmsRun:', self.__cmsRunTimer[process].getMeasuredTime() 
        ## start analysis timer
        self.__analysisTimer[process].start()

##-----------------------------------------------------------------------------------
##  * execute cmsRun via shell console
##  * needs runtime environment to be set first            
    def __executeCMSrun(self, configfile):
        print '* * executing cmsRun...'
        if os.path.exists(configfile):
            print '* * >> cmsRun ' + configfile
            if os.path.exists(self.__outputLog):
                os.remove(self.__outputLog)
            if os.path.exists(self.__outputErr):
                os.remove(self.__outputErr)   
            
            ## needs runtime environment to be set first
            if (self.__interactive):
                os.system('cmsRun ' + configfile + " >" + self.__outputLog + " 2> " + self.__outputErr + " < /dev/null&")
            else:
                os.system('cmsRun ' + configfile + " >" + self.__outputLog + " 2> " + self.__outputErr + " < /dev/null" )                    
            self.__cmsRunTimer[self.__process].start()
            print '* * '
            self.__waitForFirst(self.__process)
            self.__jobStarted = True
        else:
            self.__errorMsg()
            print '* * requested configfile does not exist: this should never happen!'

##-----------------------------------------------------------------------------------
##  * create tmp config file
##  * modify std configurables            
##  * call executeCMSrun            
    def __doJob(self, proc):
        ## create tmp config
        process = cms.ConfigWrapper(self.__config, proc)
        ## modify events
        process.modifyOption('events', self.__numberOfEvents)
        ## modify skips
        process.modifyOption('skips',  self.__numberOfSkips )
        ## modify source
        process.modifyOption('source', input.source[self.__process])
        ## modify output
        output = self.__fileServicePath
        output+= self.__fileServiceName
        output+= '_' + proc + "_"
        output+= Timer.getDate()
        output+= '.root'
        process.modifyOption('output',output)
        ## setup outputLogs
        self.__outputLog = output.__str__().replace('.root', '.out')
        self.__outputErr = output.__str__().replace('.root', '.err')
        ## initilize timers
        self.__cmsRunTimer[proc] = Timer()
        self.__analysisTimer[proc] = Timer()

        ## uncomment for testing
        #print "produced file: " + process.returnTempCfg()
        ## start cmsRun
        self.__executeCMSrun(process.returnTempCfg())

##-----------------------------------------------------------------------------------
##  * create a vector from a list of objects in a string separated by an arbitary
##    deliminator
##  * used in __doAll                
    def __vectorFromList(self, list, delim):
        myBuffer = []
        myVector = []
        if delim in list:
            myBuffer = list.split(delim)
        else:
            myBuffer = [list]
        
        for a in myBuffer:
            myVector.append(a)
            
        return myVector

##-----------------------------------------------------------------------------------
##  * wait for a single job to be finished
##  * perform basic job monitoring    
    def __waitingForEnd(self, process):
        err = False
        printEvery = self.__sleeptime
        if (self.__numberOfEvents == -1):
            ## every 30min when processing all events
            printEvery = self.__sleeptime*180
        else:
            ## every 100s for each 100 events else
            t = self.__numberOfEvents/100 - self.__numberOfEvents%100
            printEvery = self.__sleeptime*t
        
        ## print 'waiting up to 100 times
        printtimer = {}
        msg = "* * waiting for '" + str(process) + "' to end..."
        if printEvery > 0:
            for i in range(0,100):
                printtimer[i] = threading.Timer(printEvery*i, self.__printMsg, [msg])
                printtimer[i].start()

        ## while the run did not yet reach the run summary
        ## and wihle there did not yet occure any error
        while not 'Summary' in self.__readFromFile(self.__outputErr) and not err:
            ## spotted RootError
            if "Root_Error" in self.__readFromFile(self.__outputErr):
                print "* * RootError occured in ", process, ' process'
                err = True
            Timer.sleep(1)
            if((self.__analysisTimer[process].timePassed(os.times()) % printEvery) == 0):
                print '* * waiting for ', process, ' to end...'
        print '* * process ', process, ' finished'

        if printEvery > 0:
            ## clear printtimer
            for i in printtimer:
                printtimer[i].cancel()
        self.__analysisTimer[process].stop()
        print '* * time elapsed to exec  cmsRun:', self.__analysisTimer[process].getMeasuredTime()

##-----------------------------------------------------------------------------------
##  * start at least one job for each physics process
##  * do basic job monitoring for jobs in the background
##  * only called in interactive mode      
    def __doAll(self):
        ## get list of processes and create
        ## at least one run for each process
        self.__runs = self.__vectorFromList(self.__process, ';')
        ## for each 'process' in 'run'
        for i in self.__runs:
            self.__process = i
            ## check if process is defined
            if (self.__process in input.source.keys()):              
                self.__doJob(self.__process)
                if self.__jobStarted:
                    print ""
                    thread = threading.Thread(target=self.__waitingForEnd, args=(self.__process,))
                    thread.start()
                    self.__jobStarted = False
            elif self.__process == 'quit':
                os._exit(0)
            else:
                self.__errorMsg()
                print "* * not allowed process!"
                print "* * allowed processes are: ", cms.Config.allowedProcesses
                os._exit(1)
                
##-----------------------------------------------------------------------------------
if __name__ == '__main__':
    runner = CfgRunner()
    runner.beginJob()
    runner.main()
    runner.endJob()
