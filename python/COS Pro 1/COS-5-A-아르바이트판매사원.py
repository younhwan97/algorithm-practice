class Job:
	def __init__(self):
		self.salary = 0
	
	def get_salary(self):
		return salary

class PartTimeJob@@@:
	def __init__(self, work_hour, pay_per_hour):
		super().__init__()
		self.work_hour = work_hour
		self.pay_per_hour = pay_per_hour
	
	@@@:
		self.salary = self.work_hour * self.pay_per_hour
		if self.work_hour >= 40:
			self.salary += (self.pay_per_hour * 8)
		return self.salary

class SalesJob@@@:
	def __init__(self, sales_result, pay_per_sale):
		super().__init__()
		self.sales_result = sales_result
		self.pay_per_sale = pay_per_sale

	@@@:
		if self.sales_result > 20:
			self.salary = self.sales_result * self.pay_per_sale * 3
		elif self.sales_result > 10:
			self.salary = self.sales_result * self.pay_per_sale * 2
		else:
			self.salary = self.sales_result * self.pay_per_sale
		return self.salary

def solution(part_time_jobs, sales_jobs):
	answer = 0
	for p in part_time_jobs:
		part_time_job = PartTimeJob(p[0], p[1])
		answer += part_time_job.get_salary()
	for s in sales_jobs:
		sale_job = SalesJob(s[0], s[1])
		answer += sale_job.get_salary()
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
part_time_jobs = [[10, 5000], [43, 6800], [5, 12800]]
sales_jobs = [[3, 18000], [12, 8500]]
ret = solution(part_time_jobs, sales_jobs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")