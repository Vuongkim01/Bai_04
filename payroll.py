# /*****************/
# Kim Duy Vương
# 20237410
# /*****************/

from employee import Employee


class Payroll:
    def __init__(self, period):
        if not period or not str(period).strip():
            raise ValueError("Kỳ lương không được rỗng.")
        self._period = str(period).strip()
        self._employees = []

    @property
    def period(self):
        return self._period

    @property
    def employees(self):
        return list(self._employees)

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Đối tượng phải là Employee.")
        for emp in self._employees:
            if emp.employee_id == employee.employee_id:
                raise ValueError(
                    f"Nhân sự mã {employee.employee_id} đã tồn tại trong bảng lương.")
        self._employees.append(employee)

    def find_employee(self, employee_id):
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def calculate_total_payroll(self):
        return sum(emp.calculate_gross_pay() for emp in self._employees)

    def calculate_payroll_by_department(self, department):
        return sum(emp.calculate_gross_pay()
                   for emp in self._employees
                   if emp.department == department)

    def find_highest_paid_employee(self):
        if not self._employees:
            return None
        return max(self._employees, key=lambda e: e.calculate_gross_pay())

    def display_payroll(self):
        print("=" * 60)
        print(f"  BẢNG LƯƠNG KỲ: {self._period}")
        print("=" * 60)
        if not self._employees:
            print("  (Không có nhân sự)")
            return
        for emp in self._employees:
            emp.display_payroll_info()
            print()
        print("=" * 60)
        print(f"  TỔNG BẢNG LƯƠNG: {self.calculate_total_payroll():,.0f}")
        highest = self.find_highest_paid_employee()
        if highest:
            print(f"  Thu nhập cao nhất: {highest.full_name} "
                  f"({highest.calculate_gross_pay():,.0f})")
        print("=" * 60)
