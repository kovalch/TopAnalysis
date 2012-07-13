#!/bin/zsh

BASEDIR=`pwd`

foreach channel (ee emu mumu)
   
   foreach syst (JESDOWN JESUP RESDOWN RESUP MATCHUP MATCHDOWN MASSUP MASSDOWN PU_UP PU_DOWN SCALEUP SCALEDOWN MCATNLO POWHEG)   
   #foreach syst (JESDOWN JESUP RESDOWN RESUP MATCHUP MATCHDOWN MASSUP MASSDOWN PU_UP PU_DOWN SCALEUP SCALEDOWN MCNLOUP MCNLODOWN POWHEGUP POWHEGDOWN)
   #foreach syst (MCNLOUP MCNLODOWN POWHEGUP POWHEGDOWN)
   
       cd selectionRoot/$syst/$channel/
       echo
       echo "Creating Links in ... " 
       pwd
       echo 
       ln -s ../../Nominal/$channel/* .
       cd $BASEDIR
   end

end

foreach SignalSyst (MATCHUP MATCHDOWN MASSUP MASSDOWN SCALEUP SCALEDOWN MCATNLO POWHEG)

   rm selectionRoot/$SignalSyst/*/ttbarbg.root
   rm selectionRoot/$SignalSyst/*/ttbarsignalplustau.root

end

mkdir selectionRoot/HADUP selectionRoot/HADDOWN

foreach channel (ee emu mumu)

   mkdir selectionRoot/HADUP/$channel
   mkdir selectionRoot/HADDOWN/$channel
   
   cp selectionRoot/MCATNLO/$channel/* selectionRoot/HADUP/$channel
   cp selectionRoot/POWHEG/$channel/* selectionRoot/HADDOWN/$channel

   cd selectionRoot/HADUP/$channel/
   echo
   echo "Creating Links in ... " 
   pwd
   echo 
   ln -s ../../Nominal/$channel/* .
   cd $BASEDIR

   cd selectionRoot/HADDOWN/$channel/
   echo
   echo "Creating Links in ... " 
   pwd
   echo 
   ln -s ../../Nominal/$channel/* .
   cd $BASEDIR

   rm selectionRoot/HADUP/$channel/ttbarbg.root
   rm selectionRoot/HADUP/$channel/ttbarsignalplustau.root
   rm selectionRoot/HADDOWN/$channel/ttbarbg.root
   rm selectionRoot/HADDOWN/$channel/ttbarsignalplustau.root

end

