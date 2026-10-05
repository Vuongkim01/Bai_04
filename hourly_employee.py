# /*****************/
# Kim Duy Vương
# 20237410
# /*****************/

from employee import Employee


class HourlyEmployee(Employee):
    STANDARD_HOURS = 160
    MAX_HOURS = 250
    OVERTIME_MULTIPLIER = 1.5

    def __init__(self, employee_id, full_name, department="Unassigned",
                 hourly_rate=0, worked_hours=0, monthly_bonus=0):
        super().__init__(employee_id, full_name, department, monthly_bonus)
        if hourly_rate < 0:
            raise ValueError("Đơn giá giờ không được âm.")
        if not (0 <= worked_hours <= self.MAX_HOURS):
            raise ValueError(f"Số giờ làm phải từ 0 đến {self.MAX_HOURS}.")
        self._hourly_rate = hourly_rate
        self._worked_hours = worked_hours

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value < 0:
            raise ValueError("Đơn giá giờ không được âm.")
        self._hourly_rate = value

    @property
    def worked_hours(self):
        return self._worked_hours

    @worked_hours.setter
    def worked_hours(self, value):
        if not (0 <= value <= self.MAX_HOURS):
            raise ValueError(f"Số giờ làm phải từ 0 đến {self.MAX_HOURS}.")
        self._worked_hours = value

    def _calculate_base_pay(self):
        if self._worked_hours <= self.STANDARD_HOURS:
            return self._worked_hours * self._hourly_rate
        else:
            normal_pay = self.STANDARD_HOURS * self._hourly_rate
            overtime_pay = ((self._worked_hours - self.STANDARD_HOURS)
                           * self._hourly_rate * self.OVERTIME_MULTIPLIER)
            return normal_pay + overtime_pay

    def calculate_gross_pay(self):
        return self._calculate_base_pay() + self._monthly_bonus

    def get_employee_type(self):
        return "Nhân viên theo giờ"

    def display_payroll_info(self):
        super().display_payroll_info()
        print(f"  Đơn giá giờ : {self._hourly_rate:,.0f}")
        print(f"  Số giờ làm  : {self._worked_hours}")
        overtime = max(0, self._worked_hours - self.STANDARD_HOURS)
        if overtime > 0:
            print(f"  Giờ tăng ca  : {overtime}")
        print(f"  Lương cơ bản: {self._calculate_base_pay():,.0f}")
        print(f"  >>> Thu nhập : {self.calculate_gross_pay():,.0f}")
        print("-" * 50)
