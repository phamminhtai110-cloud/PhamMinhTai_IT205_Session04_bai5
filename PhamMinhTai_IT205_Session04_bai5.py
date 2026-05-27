print("=== HE THONG TINH TONG DOANH THU CA LIEN TUC ===")

total_revenue = 0
total_bills = 0
large_bills = 0

customer_number = 1

while True:
    print(f"\nKhach hang {customer_number} - Nhap gia tri hoa don: ", end="")
    bill_value = int(input())
    
    total_revenue = total_revenue + bill_value
    total_bills = total_bills + 1
    
    if bill_value >= 1000000:
        large_bills = large_bills + 1
    
    choice = input("Co muon nhap tiep khong? (C/K): ").strip().upper()
    
    if choice == "K":
        break
    
    customer_number = customer_number + 1

print("\n--- BAO CAO DOANH THU CUOI NGAY RIKKEI STORE ---")

if total_bills > 0:
    large_bill_percentage = (large_bills / total_bills) * 100
    print(f"Tong so hoa don da xu ly: {total_bills} hoa don.")
    print(f"Tong doanh thu ngay hom nay: {total_revenue:,} VND.")
    print(f"So hoa don lon (≥ 1,000,000 VND): {large_bills} hoa don.")
    print(f"Ty le hoa don lon dat: {large_bill_percentage:.1f}% tren tong so don hang.")
else:
    print("Khong co hoa don nao duoc nhap trong ca nay.")