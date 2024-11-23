# AVL Trees Split and Merge

## Thao tác Gộp (Merge)

- Mục đích: Kết hợp hai cây tìm kiếm nhị phân (BST) thành một cây duy nhất, với điều kiện tất cả các phần tử của cây thứ nhất nhỏ hơn toàn bộ các phần tử của cây thứ hai.
- Cách thực hiện:
  - Nếu có một nút trung gian làm gốc, việc gộp rất đơn giản:
    - Nút này được dùng làm gốc mới, cây thứ nhất làm con trái, cây thứ hai làm con phải.
    - Thao tác này chỉ mất thời gian cố định.
  - Nếu không có nút trung gian:
    - Phần tử lớn nhất của cây thứ nhất được loại bỏ và sử dụng làm gốc mới.
    - Thao tác này tốn thời gian tương ứng với chiều cao của cây.
- Gộp cân bằng (trên cây AVL):
  - Đảm bảo cây mới vẫn cân bằng sau khi gộp.
  - Duyệt qua cây lớn hơn để tìm một cây con có chiều cao phù hợp để gộp với cây nhỏ hơn.
  - Thời gian thực hiện:
    - Phụ thuộc vào sự chênh lệch chiều cao giữa hai cây.
    - Tổng thời gian tối đa là (O(log(n))), tương ứng với chiều cao của cây.

## Thao tác Chia (Split)

- Mục đích: Tách một cây BST thành hai cây dựa trên một giá trị khoá (key):
  - Cây thứ nhất chứa tất cả các phần tử nhỏ hơn khoá.
  - Cây thứ hai chứa tất cả các phần tử lớn hơn khoá.
- Cách thực hiện:
  - Tìm kiếm giá trị khoá trong cây.
  - Dọc theo đường đi của tìm kiếm, phân chia các cây con bên trái và bên phải thành hai nhóm:
    - Nhóm các cây nhỏ hơn khoá.
    - Nhóm các cây lớn hơn khoá.
  - Tái gộp các nhóm cây con để tạo ra hai cây hoàn chỉnh.
- Chia cân bằng (trên cây AVL):
  - Sử dụng các thao tác gộp cân bằng để đảm bảo cả hai cây kết quả vẫn duy trì tính cân bằng.
  - Thời gian thực hiện là (O(log(n))), nhờ vào đặc tính chiều cao giới hạn của cây AVL.

## Hiệu quả

- Cả hai thao tác gộp và chia đều được tối ưu trên cây AVL:
  - Đảm bảo tính cân bằng của cây trong mọi trường hợp.
  - Thời gian thực hiện là (O(log(n))), rất nhanh chóng so với các phương pháp thông thường.
