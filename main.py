from src.Work import Work


def main() -> None:
	work = Work(5, 10)
	ar_sum = work.my_sum()
    
	print(ar_sum)
	print(work)

	work_2 = Work(5, '10')
	

if __name__ == '__main__':
	main()

