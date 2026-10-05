# /*****************/
# Kim Duy Vương
# 20237410
# /*****************/

from employee import Employee


class SalesEmployee(Employee):
    MAX_COMMISSION_RATE = 0.3

    def __init__(self, employee_id, full_name, department="Unassigned",
                 base_salary=0, sales_revenue=0, commission_rate=0,
                 monthly_bonus=0):
        super().__init__(employee_id, full_name, department, monthly_bonus)
        if base_salary < 0:
            raise ValueError("Lương cơ bản không được âm.")
        if sales_revenue < 0:
            raise ValueError("Doanh số không được âm.")
        if not (0 <= commission_rate <= self.MAX_COMMISSION_RATE):
            raise ValueError(
                f"Tỷ lệ hoa hồng phải từ 0 đến {self.MAX_COMMISSION_RATE}.")
        self._base_salary = base_salary
        self._sales_revenue = sales_revenue
        self._commission_rate = commission_rate

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if value < 0:
            raise ValueError("Lương cơ bản không được âm.")
        self._base_salary = value

    @property
    def sales_revenue(self):
        return self._sales_revenue

    def update_sales_revenue(self, value):
        if value < 0:
            raise ValueError("Doanh số không được âm.")
        self._sales_revenue = value

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if not (0 <= value <= self.MAX_COMMISSION_RATE):
            raise ValueError(
                f"Tỷ lệ hoa hồng phải từ 0 đến {self.MAX_COMMISSION_RATE}.")
        self._commission_rate = value

    def calculate_gross_pay(self):
        return (self._base_salary
                + self._sales_revenue * self._commission_rate
                + self._monthly_bonus)

    def get_employee_type(self):
        return "Nhân viên kinh doanh"

    def display_payroll_info(self):
        super().display_payroll_info()
        print(f"  Lương CB    : {self._base_salary:,.0f}")
        print(f"  Doanh số    : {self._sales_revenue:,.0f}")
        print(f"  Hoa hồng    : {self._commission_rate * 100:.0f}%")
        commission = self._sales_revenue * self._commission_rate
        print(f"  Tiền HH     : {commission:,.0f}")
        print(f"  >>> Thu nhập : {self.calculate_gross_pay():,.0f}")
        print("-" * 50)
