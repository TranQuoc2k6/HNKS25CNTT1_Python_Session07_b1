student_name = input("Nhập họ và tên của bạn: ")
student_code = input("Nhập mã học viên: ")
email = input("Nhập email của bạn: ")


print(f"\n\nHọ tên: {student_name.strip().title()}")
print(f"Mã học viên: {student_code.strip().upper()}")
print(f"Email: {email.strip().lower()}")



"""
1. Phân tích lỗi
    - Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
        Vì chuỗi trong python có tính bất biến. Khi đã gán giá trị thì không thể thay đổi, chỉ có thể tạo ra một biến mới 
        -> Nên trong trường hợp này phải tạo một biến mới lưu trữ student_name.strip()

    - Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A" trong chương trình hiện tại?
        Tương tự như trường hợp trên cần phải tạo ra một biến mới để lưu trữ student_name.strip()
            hoặc có thể .title() vào biến vừa lưu trữ student_name.strip()

    - Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
        Tương tự như các trường hợp trên
    - Vì sao email.lower() không làm email chuyển thành chữ thường?
        Tương tự
    - Muốn các phương thức xử lý chuỗi có hiệu lực, cần làm gì?
    --> Ta cần tạo biến để lưu trữ các giá trị đó
"""