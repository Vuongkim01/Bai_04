# /*****************/
# Mã sinh viên:
# Họ tên: Kim Duy Vương
# /*****************/

from abc import ABC, abstractmethod


class BonusRecord:
    def __init__(self, amount, reason=""):
        self._amount = amount
        self._reason = reason

    @property
    def amount(self):
        return self._amount

    @property
    def reason(self):
        return self._reason

    def __str__(self):
        if self._reason:
            return f"{self._amount:,.0f} ({self._reason})"
        return f"{self._amount:,.0f}"


class Employee(ABC):
    def __init__(self, employee_id, full_name, department="Unassigned", monthly_bonus=0):
        if not employee_id or not str(employee_id).strip():
            raise ValueError("Mã nhân sự không được rỗng.")
        if not full_name or not str(full_name).strip():
            raise ValueError("Họ tên không được rỗng.")
        if not department or not str(department).strip():
            raise ValueError("Phòng ban không được rỗng.")
        if monthly_bonus < 0:
            raise ValueError("Thưởng không được âm.")

        self._employee_id = str(employee_id).strip()
        self._full_name = str(full_name).strip()
        self._department = str(department).strip()
        self._monthly_bonus = monthly_bonus
        self._bonus_history = []

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not value or not str(value).strip():
            raise ValueError("Họ tên không được rỗng.")
        self._full_name = str(value).strip()

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if not value or not str(value).strip():
            raise ValueError("Phòng ban không được rỗng.")
        self._department = str(value).strip()

    @property
    def monthly_bonus(self):
        return self._monthly_bonus

    @property
    def bonus_history(self):
        return list(self._bonus_history)

    def add_bonus(self, amount_or_rate, reason_or_reference=None, reason=None):
        if reason is not None:
            rate = amount_or_rate
            reference_amount = reason_or_reference
            bonus_reason = reason
            if not (0 < rate <= 0.5):
                raise ValueError("Tỷ lệ thưởng phải > 0 và <= 0.5.")
            if reference_amount is None or reference_amount <= 0:
                raise ValueError("Giá trị tham chiếu phải > 0.")
            if not bonus_reason or not str(bonus_reason).strip():
                raise ValueError("Lý do thưởng không được rỗng.")
            bonus_amount = rate * reference_amount
            self._monthly_bonus += bonus_amount
            self._bonus_history.append(
                BonusRecord(bonus_amount, str(bonus_reason).strip()))
        elif reason_or_reference is not None:
            amount = amount_or_rate
            bonus_reason = reason_or_reference
            if amount <= 0:
                raise ValueError("Khoản thưởng phải > 0.")
            if not bonus_reason or not str(bonus_reason).strip():
                raise ValueError("Lý do thưởng không được rỗng.")
            self._monthly_bonus += amount
            self._bonus_history.append(
                BonusRecord(amount, str(bonus_reason).strip()))
        else:
            amount = amount_or_rate
            if amount <= 0:
                raise ValueError("Khoản thưởng phải > 0.")
            self._monthly_bonus += amount
            self._bonus_history.append(BonusRecord(amount))

    def reset_bonus(self):
        self._monthly_bonus = 0
        self._bonus_history.clear()

    @abstractmethod
    def calculate_gross_pay(self):
        pass

    @abstractmethod
    def get_employee_type(self):
        pass

    def display_payroll_info(self):
        print(f"  Mã NV       : {self._employee_id}")
        print(f"  Họ tên      : {self._full_name}")
        print(f"  Phòng ban   : {self._department}")
        print(f"  Loại NV     : {self.get_employee_type()}")
        print(f"  Thưởng tháng: {self._monthly_bonus:,.0f}")
        if self._bonus_history:
            print("  Lịch sử thưởng:")
            for record in self._bonus_history:
                print(f"    - {record}")

    def __str__(self):
        return (f"[{self.get_employee_type()}] {self._employee_id} - "
                f"{self._full_name} | Phòng: {self._department} "
                f"| Thu nhập: {self.calculate_gross_pay():,.0f}")
