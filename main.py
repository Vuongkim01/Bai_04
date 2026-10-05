# /*****************/
# Kim Duy Vương
# 20237410
# /*****************/

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from employee import Employee
from salaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee
from sales_employee import SalesEmployee
from payroll import Payroll


def test_data():
    print("=" * 60)
    print("  DỮ LIỆU KIỂM THỬ CHÍNH")
    print("=" * 60)

    e001 = SalariedEmployee(
        employee_id="E001",
        full_name="Nguyễn Minh An",
        department="Đào tạo",
        monthly_salary=15_000_000,
        responsibility_allowance=2_000_000
    )
    e001.add_bonus(1_000_000)
    assert e001.calculate_gross_pay() == 18_000_000, \
        f"E001 sai: {e001.calculate_gross_pay()}"
    print(f"[OK] E001 thu nhập: {e001.calculate_gross_pay():,.0f} (mong đợi: 18,000,000)")

    e002 = HourlyEmployee(
        employee_id="E002",
        full_name="Trần Thu Bình",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=150
    )
    e002.add_bonus(500_000)
    assert e002.calculate_gross_pay() == 15_500_000, \
        f"E002 sai: {e002.calculate_gross_pay()}"
    print(f"[OK] E002 thu nhập: {e002.calculate_gross_pay():,.0f} (mong đợi: 15,500,000)")

    e003 = HourlyEmployee(
        employee_id="E003",
        full_name="Lê Hoàng Chi",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=170
    )
    assert e003.calculate_gross_pay() == 17_500_000, \
        f"E003 sai: {e003.calculate_gross_pay()}"
    print(f"[OK] E003 thu nhập: {e003.calculate_gross_pay():,.0f} (mong đợi: 17,500,000)")

    e004 = SalesEmployee(
        employee_id="E004",
        full_name="Phạm Quốc Dũng",
        department="Kinh doanh",
        base_salary=8_000_000,
        sales_revenue=200_000_000,
        commission_rate=0.05
    )
    e004.add_bonus(0.02, 50_000_000, "Thưởng doanh số vượt mức")
    assert e004.calculate_gross_pay() == 19_000_000, \
        f"E004 sai: {e004.calculate_gross_pay()}"
    print(f"[OK] E004 thu nhập: {e004.calculate_gross_pay():,.0f} (mong đợi: 19,000,000)")

    payroll = Payroll("2026-09")
    payroll.add_employee(e001)
    payroll.add_employee(e002)
    payroll.add_employee(e003)
    payroll.add_employee(e004)

    total = payroll.calculate_total_payroll()
    assert total == 70_000_000, f"Tổng sai: {total}"
    print(f"\n[OK] Tổng bảng lương: {total:,.0f} (mong đợi: 70,000,000)")

    total_ht = payroll.calculate_payroll_by_department("Hỗ trợ")
    assert total_ht == 33_000_000, f"Tổng Hỗ trợ sai: {total_ht}"
    print(f"[OK] Tổng phòng Hỗ trợ: {total_ht:,.0f} (mong đợi: 33,000,000)")

    highest = payroll.find_highest_paid_employee()
    print(f"[OK] Thu nhập cao nhất: {highest.full_name} ({highest.calculate_gross_pay():,.0f})")

    print()
    payroll.display_payroll()
    return payroll


def test_boundary_and_error():
    print("\n" + "=" * 60)
    print("  KIỂM THỬ BIÊN VÀ KIỂM THỬ LỖI")
    print("=" * 60)

    test_count = 0

    # 1. Mã nhân sự rỗng
    try:
        SalariedEmployee("", "Test Name")
        print("[FAIL] Test 1")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 1: Mã NV rỗng -> {e}")

    # 2. Họ tên rỗng
    try:
        SalariedEmployee("E999", "")
        print("[FAIL] Test 2")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 2: Họ tên rỗng -> {e}")

    # 3. Thưởng âm
    try:
        SalariedEmployee("E999", "Test", monthly_bonus=-100)
        print("[FAIL] Test 3")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 3: Thưởng âm -> {e}")

    # 4. Lương cố định âm
    try:
        SalariedEmployee("E999", "Test", monthly_salary=-1)
        print("[FAIL] Test 4")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 4: Lương âm -> {e}")

    # 5. Số giờ > 250
    try:
        HourlyEmployee("E999", "Test", worked_hours=260)
        print("[FAIL] Test 5")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 5: Giờ > 250 -> {e}")

    # 6. Số giờ âm
    try:
        HourlyEmployee("E999", "Test", worked_hours=-5)
        print("[FAIL] Test 6")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 6: Giờ âm -> {e}")

    # 7. Hoa hồng > 0.3
    try:
        SalesEmployee("E999", "Test", commission_rate=0.5)
        print("[FAIL] Test 7")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 7: Hoa hồng > 0.3 -> {e}")

    # 8. add_bonus với amount <= 0
    try:
        emp = SalariedEmployee("E999", "Test", monthly_salary=10_000_000)
        emp.add_bonus(-500)
        print("[FAIL] Test 8")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 8: Thưởng <= 0 -> {e}")

    # 9. add_bonus với rate > 0.5
    try:
        emp = SalariedEmployee("E999", "Test", monthly_salary=10_000_000)
        emp.add_bonus(0.6, 100_000, "Sai")
        print("[FAIL] Test 9")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 9: Rate > 0.5 -> {e}")

    # 10. Trùng mã NV trong Payroll
    try:
        pr = Payroll("2026-10")
        emp1 = SalariedEmployee("E100", "NV A", monthly_salary=10_000_000)
        emp2 = HourlyEmployee("E100", "NV B", hourly_rate=50_000)
        pr.add_employee(emp1)
        pr.add_employee(emp2)
        print("[FAIL] Test 10")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 10: Trùng mã NV -> {e}")

    # 11. Payroll rỗng
    pr_empty = Payroll("2026-10")
    result = pr_empty.find_highest_paid_employee()
    if result is None:
        test_count += 1
        print("[OK] Test 11: Payroll rỗng -> find_highest_paid_employee trả None")

    # 12. Đúng biên 160 giờ
    emp_160 = HourlyEmployee("E160", "Biên 160", hourly_rate=100_000, worked_hours=160)
    expected = 160 * 100_000
    if emp_160.calculate_gross_pay() == expected:
        test_count += 1
        print(f"[OK] Test 12: 160 giờ -> {emp_160.calculate_gross_pay():,.0f}")

    # 13. Biên 161 giờ (1 giờ tăng ca)
    emp_161 = HourlyEmployee("E161", "Biên 161", hourly_rate=100_000, worked_hours=161)
    expected = 160 * 100_000 + 1 * 100_000 * 1.5
    if emp_161.calculate_gross_pay() == expected:
        test_count += 1
        print(f"[OK] Test 13: 161 giờ -> {emp_161.calculate_gross_pay():,.0f}")

    # 14. add_bonus với lý do rỗng
    try:
        emp = SalariedEmployee("E999", "Test", monthly_salary=10_000_000)
        emp.add_bonus(500_000, "")
        print("[FAIL] Test 14")
    except ValueError as e:
        test_count += 1
        print(f"[OK] Test 14: Lý do rỗng -> {e}")

    print(f"\nTổng test đạt: {test_count}/14")


def test_overloading_explanation():
    print("\n" + "=" * 60)
    print("  GIẢI THÍCH NẠP CHỒNG VÀ GHI ĐÈ")
    print("=" * 60)

    print("""
1. Phiên bản addBonus() nào được chọn trong từng lời gọi?
   - add_bonus(1_000_000): Phiên bản 1 (chỉ amount), vì chỉ có 1 tham số.
   - add_bonus(500_000, "Thưởng KPI"): Phiên bản 2 (amount + reason),
     vì có 2 tham số và tham số thứ 2 là chuỗi.
   - add_bonus(0.02, 50_000_000, "Thưởng doanh số"): Phiên bản 3
     (rate + reference_amount + reason), vì đủ 3 tham số.
   Trong Python, việc lựa chọn dựa trên số lượng tham số truyền vào
   tại thời điểm chạy (runtime dispatch qua default arguments).

2. Việc lựa chọn phương thức nạp chồng:
   Trong các ngôn ngữ tĩnh (Java, C++), nạp chồng được chọn tại thời
   điểm biên dịch (compile-time) dựa trên chữ ký phương thức.
   Trong Python, vì chỉ có 1 phương thức với default args, việc dispatch
   diễn ra tại thời điểm chạy (runtime).

3. Việc lựa chọn calculateGrossPay() của lớp dẫn xuất:
   Đây là đa hình (polymorphism). Khi gọi calculate_gross_pay() qua
   tham chiếu kiểu Employee, Python sử dụng dynamic dispatch để gọi
   phương thức của lớp dẫn xuất thực tế tại runtime.

4. Nếu thay danh sách kiểu Employee bằng nhiều danh sách riêng:
   Sẽ mất đa hình, phải dùng if/else theo loại nhân sự, vi phạm
   nguyên tắc Open/Closed. Mỗi khi thêm loại mới phải sửa nhiều chỗ.

5. Khi thêm loại ContractEmployee:
   - Chỉ cần tạo lớp mới kế thừa Employee, ghi đè calculate_gross_pay()
     và get_employee_type().
   - Payroll KHÔNG cần sửa vì dùng đa hình qua kiểu Employee.
""")


if __name__ == "__main__":
    test_data()
    test_boundary_and_error()
    test_overloading_explanation()
