for N in 2 4 8 16 24 32 64 128;
do
	echo $N
	python3 codegen.py $N 1000000 > main.c 2> white.c 
	gcc -O0 -o main main.c  
	gcc -O0 -o white white.c 
	time ./main 
	time ./white  
	sudo perf stat -r 5 -e power/energy-cores/ ./main 
	sudo perf stat -r 5 -e power/energy-cores/ ./white
done
