count=0
for j in $@ ;do
count=$(($count+1))
done
 if [ $count -eq 1 ] ;then
	python3 "2019201038_2.py" $1
	exit
elif [ $count -eq 2 ] ;then
	python3 "2019201038_1.py" $1 $2
	exit
fi
