# AVL Trees

- Cây AVL là một loại cây nhị phân tìm kiếm, được thiết kế để duy trì sự cân bằng, đảm bảo hiệu suất cao trong các thao tác như tìm kiếm, chèn, và xóa.
- Cây AVL là một cấu trúc dữ liệu hiệu quả, duy trì sự cân bằng thông qua thuộc tính chiều cao, đảm bảo các thao tác trên cây hoạt động với độ phức tạp logarit.

### 1. Cân bằng và Tầm quan trọng

- Để tối ưu hóa các thao tác, cây nhị phân cần được giữ cân bằng.
- Chiều cao của cây là thước đo quan trọng để đánh giá mức độ cân bằng:
  - Chiều cao của một nút là đường dài nhất từ nút đó đến một lá.

### 2. Định nghĩa Chiều cao theo Đệ quy

- Đối với nút lá: Chiều cao = 1.
- Đối với các nút khác:
  - Chiều cao = 1 + giá trị lớn hơn giữa chiều cao của con trái và con phải.

### 3. Thuộc tính AVL

- Một cây được gọi là cây AVL nếu:
  - Chênh lệch chiều cao giữa con trái và con phải của mọi nút không lớn hơn 1.
- Thuộc tính này đảm bảo cây được duy trì cân bằng.

### 4. Cơ sở lý thuyết

- Cây AVL có chiều cao theo logarit:
  - Nếu duy trì thuộc tính AVL, chiều cao cây luôn là O(log(n)).
- Liên hệ với Số Fibonacci:
  - Kích thước cây con trong cây AVL liên quan đến dãy Fibonacci.
  - Chứng minh bằng quy nạp:
    - Cơ sở: Nút có chiều cao 1 tương ứng với số Fibonacci đầu tiên.
    - Bước quy nạp: Nếu một nút duy trì thuộc tính AVL, kích thước cây con của nó sẽ ít nhất bằng số Fibonacci tương ứng với chiều cao của nút đó.

### 5. Hiệu suất

- Thuộc tính AVL đảm bảo các thao tác như:
  - Tìm kiếm, Chèn, Xóa: Thực hiện trong O(log(n)).
