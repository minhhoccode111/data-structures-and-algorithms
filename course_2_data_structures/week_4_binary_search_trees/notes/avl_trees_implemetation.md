# AVL Trees implementation

- Bài giảng tiếp tục về cây AVL, tập trung vào cách cài đặt và duy trì thuộc tính AVL trong các thao tác như chèn và xóa.
- Cây AVL duy trì thuộc tính cân bằng sau các thao tác chèn và xóa.
- Hiệu quả cho các bài toán tìm kiếm với độ phức tạp logarit.

### 1. Vấn đề mất cân bằng

- Thuộc tính AVL: Chênh lệch chiều cao giữa hai con của một nút không vượt quá 1.
- Khi chèn hoặc xóa, chiều cao cây có thể thay đổi, dẫn đến việc vi phạm thuộc tính AVL.
- Thay đổi chiều cao chỉ ảnh hưởng đến các nút trên đường dẫn thao tác (từ gốc đến nút bị chèn hoặc xóa).

### 2. Cài đặt Chèn

- Quy trình chèn:
  1. Thực hiện chèn nút mới như bình thường.
  2. Bắt đầu từ nút vừa chèn, thực hiện cân bằng lại cây trên đường dẫn đến gốc.
- Cân bằng lại:
  - Nếu chiều cao của con trái lớn hơn con phải hơn 1, thực hiện xoay phải.
  - Nếu chiều cao con phải lớn hơn con trái hơn 1, thực hiện xoay trái.
  - Điều chỉnh chiều cao của nút và tiếp tục cân bằng nút cha.
- Xoay đơn: Khi chênh lệch chiều cao giữa con trái và con phải là 2.
- Xoay kép: Khi chiều cao bất thường nằm ở cây con của nút trái hoặc phải.

### 3. Xóa và Duy trì Cân bằng

- Quy trình xóa:
  1. Xóa nút như bình thường.
  2. Sau khi xóa, vùng cây bị ảnh hưởng có thể mất cân bằng.
  3. Thực hiện cân bằng lại bắt đầu từ vị trí bị ảnh hưởng.
- Cân bằng lại sau xóa:
  - Tương tự như chèn, thực hiện xoay đơn hoặc xoay kép để duy trì thuộc tính AVL.

### 4. Hiệu suất

- Các thao tác cân bằng (xoay và điều chỉnh chiều cao):
  - Chi phí mỗi cấp cây là O(1).
  - Tổng chi phí trên toàn cây là O(log(n)).
- Nhờ đó, các thao tác cơ bản như tìm kiếm, chèn, xóa đều có độ phức tạp O(log(n)).
