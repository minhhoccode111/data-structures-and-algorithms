## Graph Basics

- Định nghĩa đồ thị:

  - Đồ thị (Graph) là mô hình trừu tượng dùng để biểu diễn các kết nối giữa các đối tượng
  - Thành phần:
    - Đỉnh (Vertices): Đại diện cho các đối tượng
    - Cạnh (Edges): Kết nối giữa các đỉnh, có thể là đường thẳng hoặc đường cong

- Ứng dụng của đồ thị:

  - Internet: Đồ thị kết nối các trang web thông qua các liên kết
  - Bản đồ: Giao lộ (đỉnh) kết nối với nhau qua các con đường (cạnh)
  - Mạng xã hội: Con người (đỉnh) kết nối qua các mối quan hệ như bạn bè, theo dõi
  - Robot: Cấu hình của robot là các đỉnh, chuyển động giữa các cấu hình là cạnh, hỗ trợ giải bài toán tái cấu hình robot

- Đồ thị vô hướng (Undirected Graph):

  - Gồm tập hợp V (đỉnh) và E (cạnh), trong đó mỗi cạnh kết nối một cặp đỉnh
  - Ví dụ: Đồ thị với các đỉnh A, B, C, D và các cạnh giữa các cặp đỉnh (A-B, A-C, A-D, C-D)

- Các khái niệm liên quan:

  - Vòng lặp (Loop): Một cạnh kết nối một đỉnh với chính nó
  - Cạnh đa (Multiple Edges): Nhiều cạnh cùng kết nối một cặp đỉnh
  - Đồ thị đơn giản (Simple Graph): Không có vòng lặp và không có cạnh đa

- Tính chất cơ bản:
  - Đếm số cạnh của một đồ thị bằng cách kiểm tra từng kết nối giữa các đỉnh
  - Đồ thị đơn giản thường được sử dụng để giảm bớt sự phức tạp trong xử lý

## Representing Graphs

- Đồ thị và cách biểu diễn:

  - Đồ thị gồm các đỉnh (vertices) và cạnh (edges) kết nối giữa các đỉnh
  - Có ba cách chính để biểu diễn đồ thị trên máy tính:
    1. Danh sách cạnh (Edge List): Lưu trữ danh sách các cặp đỉnh được kết nối
    2. Ma trận kề (Adjacency Matrix): Ma trận vuông, mỗi ô chứa 1 (nếu có cạnh) hoặc 0 (nếu không có cạnh) giữa hai đỉnh
    3. Danh sách kề (Adjacency List): Mỗi đỉnh lưu danh sách các đỉnh láng giềng

- So sánh các cách biểu diễn:

  - Xác định cạnh giữa hai đỉnh:
    - Ma trận kề: Nhanh, thời gian hằng số
    - Danh sách cạnh: Chậm, cần duyệt toàn bộ danh sách cạnh
    - Danh sách kề: Nhanh hơn danh sách cạnh, phụ thuộc vào số láng giềng của đỉnh
  - Liệt kê tất cả các cạnh:
    - Danh sách cạnh: Tốt nhất
    - Danh sách kề: Cũng hiệu quả nhưng mỗi cạnh được tính hai lần
    - Ma trận kề: Chậm nhất, thời gian tỷ lệ với số đỉnh bình phương
  - Liệt kê láng giềng của một đỉnh:
    - Danh sách kề: Nhanh nhất
    - Ma trận kề: Chậm, cần duyệt qua hàng của ma trận
    - Danh sách cạnh: Chậm, cần duyệt qua toàn bộ danh sách cạnh

- Độ phức tạp thuật toán trên đồ thị:

  - Phụ thuộc vào số đỉnh (V) và số cạnh (E)
  - Một số độ phức tạp phổ biến: O(V + E), O(V^1.5), O(V log V + E), v.v
  - So sánh hiệu quả thuật toán phụ thuộc vào độ dày đặc của đồ thị (density):
    - Đồ thị dày đặc (Dense Graphs): Số cạnh gần bằng số đỉnh bình phương (gần đầy đủ kết nối)
    - Đồ thị thưa (Sparse Graphs): Số cạnh nhỏ, thường gần bằng số đỉnh

- Ứng dụng thực tế:
  - Đồ thị dày đặc thường xuất hiện trong các bài toán kết nối toàn diện
  - Đồ thị thưa phổ biến trong mạng xã hội, Internet, bản đồ giao thông, v.v
