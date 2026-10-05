# /*****************/
# Kim Duy Vương
# 20237410
# /*****************/

from employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, employee_id, full_name, department="Unassigned",
                 monthly_salary=0, responsibility_allowance=0, monthly_bonus=0):
        super().__init__(employee_id, full_name, department, monthly_bonus)
        if monthly_salary < 0:
            raise ValueError("Lương cố định không được âm.")
        if responsibility_allowance < 0:
            raise ValueError("Phụ cấp trách nhiệm không được âm.")
        self._monthly_salary = monthly_salary
        self._responsibility_allowance = responsibility_allowance

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if value < 0:
            raise ValueError("Lương cố định không được âm.")
        self._monthly_salary = value

    @property
    def responsibility_allowance(self):
        return self._responsibility_allowance

    @responsibility_allowance.setter
    def responsibility_allowance(self, value):
        if value < 0:
            raise ValueError("Phụ cấp trách nhiệm không được âm.")
        self._responsibility_allowance = value

    def calculate_gross_pay(self):
        return (self._monthly_salary
                + self._responsibility_allowance
                + self._monthly_bonus)

    def get_employee_type(self):
        return "Nhân viên lương cố định"

    def display_payroll_info(self):
        super().display_payroll_info()
        print(f"  Lương tháng : {self._monthly_salary:,.0f}")
        print(f"  Phụ cấp TN  : {self._responsibility_allowance:,.0f}")
        print(f"  >>> Thu nhập : {self.calculate_gross_pay():,.0f}")
        print("-" * 50)
