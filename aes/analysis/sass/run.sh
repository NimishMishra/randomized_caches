
for j in {100..20000..1000}
do
for i in {0..15}
do 
   python3 analysis.py $i $j >> ranks.txt
done
   echo -n "For $j traces: GE = "
   python3 guessing_entropy.py
   rm ranks.txt
done
