# KLTN---Robot-face-recognizer
Khóa luận tốt nghiệp (2019): Robot nhận diện khuôn mặt. Khoa Công nghệ thông tin, trường Đại Học Công Nghiệp Tp.HCM. Sinh viên thực hiện: Huỳnh Quốc Thắng - 15064001 và Nguyễn Trung Tú - 15040821.
MỤC LỤC
Danh Mục Hình Ảnh	4
Danh Mục Bảng Biểu	7
Danh mục các từ viết tắt (tiếng Anh)	8
LỜI NÓI ĐẦU	10
1. Tổng quan tình hình nghiên cứu thuộc lĩnh vực Internet of things:	10
2. Ý nghĩa khoa học và thực tiễn của đề tài:	10
CHƯƠNG 1: GIỚI THIỆU	11
1.1 Tổng quan đề tài:	11
1.2 Mục tiêu đề tài:	11
1.3 Phạm vi đề tài:	11
1.4 Mô tả đề tài:	12
CHƯƠNG 2: CƠ SỞ LÝ THUYẾT (TÌM HIỂU VỀ IOT).	13
2.1 Khái niệm IoT:	13
2.2 Cơ sở kỹ thuật IoT:	15
2.2.1 Công suất thiết bị (Device Power)(7).	15
2.2.2 Các giao thức truyền tải dữ liệu (IoT Protocol).	17
2.2.3 Công nghệ cảm biến (Sensor Technology)(23).	21
2.3 Một số ứng dụng nổi bật của IoT:	22
CHƯƠNG 3. TÌM HIỂU VỀ PHẦN CỨNG.	25
3.1. Raspberry Pi 3.	25
3.2. Nguồn cho Raspberry Pi 3 5.1VDC 2.5A Micro USB.	27
3.3. Thẻ nhớ SanDisk MicroSDHC Ultra 16Gb 80MB/S.	28
3.4. Mạch còi Buzzer.	28
3.5. Sensor Cảm biến ánh sáng quang trở CDS(25).	28
3.6. Camera.	29
3.7. Động cơ Servo.	29
BẢNG DỰ TRÙ KINH PHÍ	30
CHƯƠNG 4. THIẾT KẾ VÀ THỰC HIỆN.	31
4.1. Hệ điều hành cho Raspberry Pi 3.	31
4.1.1 Chuẩn bị hệ điều hành cho Raspberry Pi.	31
4.1.2 Tiến hành cài đặt hệ điều hành Raspbian.	32
4.1.3 Sử dụng Raspberry Pi thông qua Laptop/Desktop.	36
4.2. Khái quát về các thư viện.	38
4.2.1 Thư viện OpenCV.	38
4.2.2 Thư viện Numpy (Nummerical Python).	39
4.2.3 Cài đặt thư viện.	40
4.2.4 Thư viện Imaging (PIL).	45
4.2.5 Thư  viện os.	46
4.2.6 Thư viện argparse.	46
4.2.7 Thư viện MySQLdb	46
4.2.8 Thư viện time	46
4.2.9 Nền tảng Python	46
4.2.10 ArduinoIDE	48
4.3. Cài đặt Cơ sở dữ liệu và cấu hình.	49
4.3.1 Giới thệu về My SQL.	49
4.3.2 Cài đặt	49
4.4. Cài đặt Web server (Apache web server) và phpMyAdmin:	53
4.4.1 Cài đặt Apache Web server:	53
4.4.2 Cài đặt phpMyAdmin:	54
4.5. Tiến hành cài đặt các thư viện liên quan khác:	57
4.5.1. RPi.GPIO.	57
4.5.2. Thư viện Imaging (PIL(36))	57
4.5.3. Kết nối các thiết bị theo mạch sơ đồ.	57
4.6. Tiến hành lắp ráp mô hình:	58
4.6.1. Chuẩn bị dụng cụ.	58
4.6.2. Thực hiện.	59
4.7. Tiến hành code và chạy thử:	61
CHƯƠNG 5: KẾT LUẬN.	64
5.1. Kết quả đạt được.	64
5.2. Những chắc năng chưa thực hiện được.	64
5.3. Hướng phát triển.	64
Bảng phân công công việc.	66
Tài liệu tham khảo.	69

 
Danh Mục Hình Ảnh
Hình 2.1 1 Internet of things (Internet vạn vật)	13
Hình 2.1 2 Ứng dụng tủ lạnh thông minh.	14

Hình 2.2. 1 IoT Stack	15
Hình 2.2. 2 Bluetooth Low Energy	17
Hình 2.2. 3 Wi-Fi	17
Hình 2.2. 4 Zigbee	17
Hình 2.2. 5 Giao thức MQTT - Message Queue Telemetry Transport	18
Hình 2.2. 6 Giao thức CoAP - Constrained Applications Protocol	19
Hình 2.2. 7 Giao thức XMPP - Extensible Messaging và Presence Protocol	21
Hình 2.2. 8 Công nghệ cảm biến	22

Hình 2.3. 1 Một số ứng dụng IoT	23
Hình 2.3. 2 Ứng dụng IoT trong sản xuất nông nghiệp	24
Hình 2.3. 3 Ứng dụng IoT Ngôi nhà thông minh	24
Hình 2.3. 4 Ứng dụng IoT trong chăm sóc Y Tế	25

Hình 3.1. 1 Raspberry Pi 3	25
Hình 3.1. 2 Chi tiết Raspberry Pi 3	26

Hình 3.2. 1 Nguồn Raspberry Pi 3	27

Hình 3.4. 1 Mạch còi Buzzer	28

Hình 3.5. 1 Quang trở	28

Hình 3.6. 1 Camera	29

Hình 4.1. 1 Raspberry Pi Desktop	31
Hình 4.1. 2 Phần mềm format thẻ nhớ	32
Hình 4.1. 3 Write32DiskImager	32
Hình 4.1. 4 Hình ảnh welcome khi khởi động Raspberry	33
Hình 4.1. 5 Cửa sổ thiết lập ban đầu của hệ điều hành Raspberry	33
Hình 4.1. 6 Cài đặt mật khẩu	34
Hình 4.1. 7 Raspberry Pi Configuration	34
Hình 4.1. 8 Cửa sổ terminal	35
Hình 4.1. 9 Lệnh cập nhật hệ điều hành	35
Hình 4.1. 10 Lệnh nâng cấp hệ điều hành	36
Hình 4.1. 11 Quét IP của Raspberry Pi	36
Hình 4.1. 12 Bảng kết nối điều khiển Remote Desktop	37
Hình 4.1. 13 Màn hình đăng nhập Raspberry Pi	37

Hình 4.2. 1 Open CV	38
Hình 4.2. 2 Thư viện Numpy	39
Hình 4.2. 3 Cài đặt Cmake và một số công cụ khác	40
Hình 4.2. 4 Lệnh cài đặt I/O image Packages	40
Hình 4.2. 5 Lệnh cài đặt I/O video packages	40
Hình 4.2. 6 Lệnh cài đặt OpenCV 3.1.0	41
Hình 4.2. 7 Lệnh cài đặt pip	41
Hình 4.2. 8 Lệnh cài đặt môi trường ảo	41
Hình 4.2. 9 Lệnh cài đặt môi trường ảo	41
Hình 4.2. 10 Lệnh cài đặt môi trường ảo	41
Hình 4.2. 11 Lệnh cài đặt môi trường ảo cho Python	41
Hình 4.2. 12 Lệnh cài đặt môi trường ảo cho Python	41
Hình 4.2. 13 Lệnh xem môi trường ảo đã đưuọc ài đặt chưa	42
Hình 4.2. 14 Môi trường ảo đã được cài đặt	42
Hình 4.2. 15 Lệnh cài đặt Numpy	42
Hình 4.2. 16 Lệnh cài đặt Numpy	42
Hình 4.2. 17 Kiểm tra các gói cài đặt	43
Hình 4.2. 18 Biên dịch	43
Hình 4.2. 19 Lệnh biên dịch	44
Hình 4.2. 20 Cài đặt OpenCV	44
Hình 4.2. 21 Đoạn code kiểm tra việc nhận diện khuôn mặt	44
Hình 4.2. 22 Kết quả nhận diện	45
Hình 4.2. 23 Kết quả nhận diện	45
Hình 4.2. 24 Python	47
Hình 4.2. 25 ArduinoIDE	48

Hình 4.3. 1 Lệnh cài đặt MySQL	49
Hình 4.3. 2 Lệnh tạo cơ sở dữ liệu và phân quyền truy cập	50
Hình 4.3. 3 Lệnh tạo cơ sở dữ liệu và phân quyền truy cập	50
Hình 4.3. 4 Đăng nhập vào MySQL	51
Hình 4.3. 5 Tạo bảng Detail	51
Hình 4.3. 6 Thêm dữ liệu vào cơ sở dữ liệu	52
Hình 4.3. 7 Xóa dữ liệu trong cơ sở dữ liệu	52
Hình 4.3. 8 Kết quả	53
Hình 4.3. 9 Lệnh cài đặt Apache web server	53
Hình 4.3. 10 Cài đặt thành công Apache web server	54

Hình 4.4. 1 PHPMyAdmin	55
Hình 4.4. 2 lệnh cài đặt PhpMyAdmin	55
Hình 4.4. 3 Lệnh khởi động lại Apache	55
Hình 4.4. 4 Tên miền để truy cập vào phpMyAdmin	55
Hình 4.4. 5 Cửa sổ đăng nhập vào cơ sở dữ liêu	56
Hình 4.4. 6 Cửa sổ chính trong phpMyAdmin	56

Hình 4.5. 1 Lệnh cài đặt RPi.GPIO	57
Hình 4.5. 2 Sử dụng thư viện RPi.GPIO	57

Hình 4.6. 1 Mạch sơ đồ kết nối các thiết bị	57
Hình 4.6. 6 Xốp Depron foam 5mm x 1m x 1m	58
Hình 4.6. 7 Bản lề 2 lỗ 27mm x 38mm	58
Hình 4.6. 8 Keo dán 25 gram EPO - EPP - Depron	59
Hình 4.6. 9 Dao rọc giấy hobby knife	59
Hình 4.6. 10 Mô hình sau khi đã lắp ráp	60
Hình 4.6. 11 Mô hình sau khi đã lắp ráp	60

Hình 4.7. 1 Kết quả hoạt động của sensor quang trở	61
Hình 4.7. 2 Camera bắt đầu phân tích khuôn mặt	61
Hình 4.7. 3 Chương trình báo sai	62
Hình 4.7. 4 Chương trình báo đúng và mở cửa	62

Hình 5.3. 1 Biểu tượng cho sự phát triển	65



 
Danh Mục Bảng Biểu

Bảng 2.2. 1 Bảng so sánh các chuẩn truyền thông không dây	16

Bảng 3.7. 1 Bảng dự trù kinh phí	30

Bảng phân công công việc 1	68

 
Danh mục các từ viết tắt (tiếng Anh)

STT	Từ viết tắt	Từ đầy đủ/Ngữ nghĩa
1	IoT	Internet of things.
2	Train/ Deep learning	Huấn luyện/Học sâu dựa trên tập hợp các thuật toán để cố gắng mô hình dữ liệu trừu tượng hóa ở mức cao bằng cách sử dụng nhiều lớp xử lý với cấu trúc phức tạp, hoặc bằng cách khác bao gồm nhiều biến đổi phi tuyến.
3	Open	Mở.
4	Mems	Micro Electro Mechanical Systems.
5	IP	Internet Protocol.
6	Id	Identification.
7	Device power	Công suất thiết bị.
8	Wi-Fi	Wireless Fide.
9	LAN	Local Area Network.
10	MQTT	Message Queue Telemetry Transport.
11	Message	Tin nhắn, thông điệp.
12	Broker	Trung gian.
13	TCP	Transmission Control Protocol.
14	Qos	Quality of Service.
15	Coap	Constrained application protocol.
16	Html	Hyper text markup language.
17	UDP	User Datagram Protoocol.
18	Ssl
Tls	Secure sockets layer.
Transport layer security.
19	AMQP	Advanced Message Queue Protocol.
20	DDS	Data Distribution Service
21	XMPP	Extensible Messaging và Presence Protocol.
22	XML	eXtensible Markup Language
23	Sensor Technology	Công nghệ cảm biến.
24	GPIO	General Purpose Input Output ( Cổng đầu vào và ra với mục đích cơ bản).
25	CDS	Quang trở.
26	OpAmp	Operational Amplifier, Mạch điện tử có chức năng khuyếch đại tín hiệu.
27	Terminal	Giao diện dòng lệnh (Command line Interface).
28	Username	Tên người dùng.
29	Password	Mật khẩu.
30	Download	Tải về.
31	List	Danh sách.
32	Ndarray	Các lớp trong dãnh Numpy.
33	Modules	Mô-đun
34	Apache	Web Server Apache.
35	GUI	Graphical User Interface.
36	PIL	Thư viện Imaging.
		
		
		
		

 
LỜI NÓI ĐẦU
1. Tổng quan tình hình nghiên cứu thuộc lĩnh vực Internet of things:
Internet of Things (IoT) là xu hướng đang được các doanh nghiệp trong lĩnh vực công nghệ quan tâm và đầu tư nghiên cứu. Cuộc đua IoT đã và đang diễn ra mạnh mẽ giữa các doanh nghiệp trên toàn thế giới.
Với đời sống đang phát triển theo hướng công nghệ hóa, hiện đại hóa, Internet of things(1) (IoT) được biết đến như một bước tiến mạnh mẽ trong nền công nghệ 4.0, các thiết bị đồ vật bình thường được IoT hóa giúp chúng ta thực hiện công việc một cách nhanh chóng, hiệu quả, tiện lợi. Ngay cả đối với công việc thủ công trước đây cũng dần được thay đổi bởi những công cụ có khả năng tính toán xử lý thông minh, thu thập dữ liệu, gửi, lưu trữ thông tin một cách nhanh chóng, tốn ít thời gian hơn,… Sự phối hợp của các thiết bị cùng đưa ra số liệu cần thiết, cung cấp thông tin từ đó giúp con người có thể phân tích tình trạng hiện tại nhằm đưa ra những thông báo, khả năng giao tiếp kết nới với những cỗ máy thiết bị, cảm biến và cả con người thông qua mạng lưới vạn vật kết nối Internet (IoT).
2. Ý nghĩa khoa học và thực tiễn của đề tài:
Hiện nay với sự phát triển vượt bậc của IoT, đặc biệt là trong phát triển smart home. Việc bảo mật ngôi nhà của bạn ngày càng được đề cao, trong đó đa số mọi người vẫn thường dùng những kiểu ổ khóa kiểu cũ cần dùng đến chìa khóa rất dễ dàng bị xâm nhập và bất tiện như việc quên chìa khóa hoặc đánh mất chìa khóa. Thay vào đó chúng ta có thể sử dụng các loại khóa thông minh có nhiều chức năng tiện lợi cho người sử dụng. Điển hình là mở khóa cửa bằng nhận diện khuôn mặt.
	Do tài liệu tham khảo hạn chế, trình độ có hạn và kinh nghiệm trong thực tiễn còn non kém,nên đề tài không tránh khỏi những thiếu sót. Rất mong nhận được những ý kiến đóng góp, giúp đỡ chân tình, quý báu của quý thầy cô cùng các bạn sinh viên. 
 
CHƯƠNG 1: GIỚI THIỆU
1.1 Tổng quan đề tài:
	Hiện nay, tình trạng kẻ gian đột nhập vào nhà trộm cắp tài sản ngày càng gia tăng trên khắp cả nước. Không chỉ trộm cắp tài sản, các đối tượng này càng ngày càng manh động, chống trả và xâm hại đến chủ nhà nếu như bị phát hiện. Đã có rất nhiều trường hợp người dân bị thương vong khi có kẻ trộm đột nhập vào nhà. (Theo báo Công An).
Ngôi nhà đã được trang bị các biện pháp bảo vệ, nhưng vẫn bị trộm đột nhập?
Trước thực trạng trên, người dân đã nâng cao ý thức bảo vệ ngôi nhà của mình bằng rất nhiều biện pháp khác nhau. Thông thường thì xây dựng các lối vào nhà kiên cố, có khoá chắc chắn,… Tuy nhiên kẻ gian vẫn dễ dàng vượt qua các biện pháp bảo vệ này để đột nhập vào gia đình trộm cắp. Tình trạng bẻ khoá cửa đột nhập vào nhà diễn ra ngày càng nhiều với thủ đoạn ngày càng tinh vi hơn. Việc trang bị các thiết bị an ninh cho ngôi nhà là hết sức cần thiết, nhưng đa số người dân đều chưa biết cách lắp đặt sử dụng, dẫn tới chưa phát huy được hiệu quả bảo vệ ngôi nhà.
“Cảnh báo sớm” là điều vô cùng quan trọng trong mọi biện pháp bảo vệ. Chính vì vậy, sự ra đời của khóa nhận diện khuôn mặt sẽ giúp chúng ta được cảnh báo sớm hơn khi có sự việc xảy ra, nhanh chóng báo cơ quan chức năng để xử lý,… 
1.2 Mục tiêu đề tài:
Mục tiêu đề tài: Xây dựng một sản phẩm mô hình mở khóa cửa bằng nhận diện khuôn mặt thông qua Raspberry pi và các thiết bị liên quan, nhằm bảo vệ tài sản, nhà cửa.
1.3 Phạm vi đề tài:
	Phạm vi đề tài: Phần lớn để phục vụ cho người lao động, công ty, doanh nghiệp,… Thời gian tối thiểu cần thiết để hoàn tất công trình nghiên cứu: 03 tháng. Phương tiện, thiết bị nghiên cứu: tự túc.
1.4 Mô tả đề tài:
Đầu tiên người dùng cần phải thiết lập mật khẩu bằng cách để webcam chụp gương mặt của người đó với nhiều biểu cảm khác nhau (khoảng 200 tấm hình) sau đó hệ thống sẽ tự động huấn luyện (train/deep learning(2)) về khuôn mặt người đó. 
Khi sử dụng, người dùng đứng trước webcam và nhấn nút bấm nhận diện để hệ thống bắt đầu tự động quét gương mặt sau đó nó sẽ so sánh với những tấm hình đã được huấn luyện trước đó (đèn vàng sáng để báo hiệu hệ thống đang hoạt động). Nếu đúng, khóa cửa sẽ mở cùng với đèn xanh bật lên báo hiệu khóa cửa đã mở, còn nếu sai thì trường hợp này là không đúng người thì nó sẽ báo hiệu bằng đèn đỏ và nó sẽ phát còi báo hiệu. 
Khi người dùng đã vào nhà và đóng cửa, hệ thống sẽ ghi nhận là cửa đã đóng và tự động khóa cửa lại, hệ thống nhận diện sẽ sẵn sàng cho đợt quét tiếp theo. Khi người ở trong muốn đi ra ngoài thì chỉ cần bấm nút Mở cửa (Open(3)) để cửa mở. 
CHƯƠNG 2: CƠ SỞ LÝ THUYẾT (TÌM HIỂU VỀ IOT).
2.1 Khái niệm IoT:
Internet of Things (IoT) là thuật ngữ dùng để chỉ các đối tượng có thể được nhận biết cũng như sự tồn tại của chúng trong một kiến trúc mang tính kết nối. Đây là một viễn cảnh trong đó mọi vật, mọi con vật hoặc con người được cung cấp các định danh và khả năng tự động truyền tải dữ liệu qua một mạng lưới mà không cần sự tương tác giữa con người-với-con người hoặc con người-với-máy tính. IoT tiến hoá từ sự hội tụ của các công nghệ không dây, hệ thống vi cơ điện tử (MEMS)(4) và Internet. Cụm từ này được đưa ra bởi Kevin Ashton vào năm 1999. Ông là một nhà khoa học đã sáng lập ra Trung tâm Auto-ID ở đại học MIT.
 
Hình 2.1 1 Internet of things (Internet vạn vật)
 “Thing” - sự vật - trong Internet of Things, có thể là một trang trại động vật với bộ tiếp sóng chip sinh học, một chiếc xe ô tô tích hợp các cảm biến để cảnh báo lái xe khi lốp quá non, hoặc bất kỳ đồ vật nào do tự nhiên sinh ra hoặc do con người sản xuất ra mà có thể được gán với một địa chỉ IP(5) và được cung cấp khả năng truyền tải dữ liệu qua mạng lưới. Một ví dụ điển hình cho IoT là tủ lạnh thông minh, nó có thể là một chiếc tủ lạnh bình thường nhưng có gắn thêm các cảm biến bên trong giúp kiểm tra được số lượng các loại thực phẩm có trong tủ lạnh, cảm biến nhiệt độ, cảm biến phát hiện mở cửa,…và các thông tin này được đưa lên internet. Với một danh mục thực phẩm được thiết lập trước bởi người dùng, khi mà một trong các loại thực phẩm đó sắp hết thì nó sẽ thông báo ngay cho chủ nhân nó biết rằng cần phải bổ sung gấp, thậm chí nếu các loại sản phẩm được gắn mã ID(6) thì nó sẽ tự động trực tiếp gửi thông báo cần nhập hàng đến siêu thị và nhân viên siêu thị sẽ gửi loại thực phẩm đó đến tận nhà.
 
Hình 2.1 2 Ứng dụng tủ lạnh thông minh.
 
2.2 Cơ sở kỹ thuật IoT:
 
Hình 2.2. 1 IoT Stack
– Sensor: Các cảm biến như cảm biến nhiệt độ, độ ẩm, cảm biến ánh sáng v.v…
– Local Processing: Các xử lý tín hiệu đầu vào cục bộ trước khi đẩy lên đám mấy.
– Local Storage: Lưu trữ cục bộ của dữ liệu cần xử lý.
– Network: Phần cứng kết nối mạng.
– Internet: Kết nối ra internet.
– Cloud Processing: Xử lý tính toán đám mây.
– Cloud Storage: Lưu trữ đám mây.
	2.2.1 Công suất thiết bị (Device Power)(7).
Các tiêu chí hình thức chính của thiết bị khi triển khai một ứng dụng IoT là phải giá thành thấp, mỏng, nhẹ…và như vậy phần năng lượng nuôi thiết bị cũng sẽ trở nên nhỏ gọn lại, năng lượng tích trữ cũng sẽ trở nên ít đi. Do đó đòi hỏi thiết bị phải tiêu tốn một công suất cực nhỏ (Ultra Low Power) để sử dụng nguồn năng lượng có hạn đó. Bên cạnh đó yêu cầu có những giao thức truyền thông không dây gọn nhẹ hơn, đơn giản hơn, đòi hỏi ít công suất hơn (Low Energy Wireless Technologies) như Zigbee, BLE (Bluetooth low energy), ANT/ANT+, NIKE+,..
	ZigBeeTM
802.15.4	BluetoothTM
802.15.1	Wi-FiTM
802.11b	GPRS/GSM
1XRTT/CDMA
Application Focus	Monitoring & Control	Cable Replacêmnt	Web, Video, Email	WAN, Voice/Data
System Resource	4KB-32KB	250KB+	1MB+	16MB+
Battery Life (days)	100-1000+	1-7	.1-5	1-7
Nodes Per Network	255/65K+	7	30	1,000
Bandwidth (kbps)	20/250	720	11,000+	64-128
Range (meters)	1-75+	1-10+	1-100	1,000
Key Attribute	Reliable, Low power, Cost Effective	Cost, Convenience	Speed, Flexibility	Reach, Quality
Bảng 2.2. 1 Bảng so sánh các chuẩn truyền thông không dây
Một số chuẩn truyền thông không dây thường được sử dụng:
	+ Bluetooth: BLE - Bluetooth Low Energy - hoặc Bluethooth Smart là một giao thức được sử dụng đáng kể cho các ứng dụng IoT. Quan trọng hơn, cùng với một khoảng cách truyền tương tự như Bluetooth, BLE được thiết kế để tiêu thụ công suất ít hơn rất nhiều.
 
Hình 2.2. 2 Bluetooth Low Energy
	+ Wifi(8): Wifi  (là viết tắt từ Wireless Fidelity hay mạng 802.11) là hệ thống mạng không dây sử dụng sóng vô tuyến, cũng giống như điện thoại di đông, truyền hình và radio. Kết nôi Wifi thường là sự lựa chọn hàng đầu của rất nhiều kỹ sư giải pháp bởi tính thông dụng và kinh tế của hệ thống wifi và mạng LAN(9) với mô hình kết nối trong một phạm vi địa lý có giới hạn.
 
Hình 2.2. 3 Wi-Fi
	+ Zigbee: Zigbee, giống như Bluetooth, là một loại truyền thông trong khoảng cách ngắn, hiện được sử dụng với số lượng lớn và thường được sử dụng trong công nghiệp. Điển hình, Zigbee Pro và Zigbee remote control (RF4CE) được thiết kế trên nền tảng giao thức IEEE802.15.4 - là một chuẩn giao thức truyền thông vật lý trong công nghiệp hoạt động ở 2.4Ghz thường được sử dụng trong các ứng dụng khoảng cách ngắn và dữ liệu truyền tin ít nhưng thường xuyên, được đánh giá phù hợp với các ứng dụng trong smarthome hoặc trong một khu vực đô thị/khu chung cư.
 
Hình 2.2. 4 Zigbee
2.2.2 Các giao thức truyền tải dữ liệu (IoT Protocol).
Để khai thác hết được tiềm năng của mô hình IoT, các thiết bị kết nối cần phải giao tiếp bằng các giao thức nhẹ mà không làm tiêu tốn quá nhiều tài nguyên của CPU. Dưới đây cung cấp tổng quan về 5 giao thức truyền tải dữ liệu phổ biến có thể được sử dụng trong các mô hình Internet of Things.
MQTT(10) (Message Queue Telemetry Transport)
MQTT là một giao thức mã nguồn mở để truyền các tin nhắn (messages)(11) giữa nhiều Client (Publisher và Subscriber) thông qua một trung gian (Broker)(12)    được thiết kế để đơn giản và dễ dàng triễn khai. Kiến trúc MQTT dựa trên Broker trung gian và sử dụng kết nối TCP(13) long-lived từ các Client đến Broker.
MQTT hỗ trợ tổ chức hệ thống theo các chủ đề có tính phân cấp, như một hệ thống tập tin (ví dụ: /Home/kitchen/humidity), cung cấp nhiều lựa chọn điều khiển và QoS(14) (Quality of Service).
 MQTT là một giao thức khá nhẹ nên có thể được sử dụng cho truyền thông hai chiều thông qua các mạng có độ trễ cao và độ tin cậy thấp, nó cũng tương thích với các thiết bị tiêu thụ điện năng thấp.
 
Hình 2.2. 5 Giao thức MQTT - Message Queue Telemetry Transport
CoAP(15) (Constrained Applications Protocol)
CoAP là một giao thức truyền tải tài liệu theo mô hình client/server dự trên internet tương tự như giao thức HTTP(16) nhưng được thiết kế cho các thiết bị ràng buộc. Giao thức này hỗ trợ một giao thức one-to-one để chuyển đổi trạng thái thông tin giữa client và server.
 CoAP sử dụng UDP(17) (User Datagram Protocol), không hỗ trợ TCP, ngoài ra còn hỗ trợ địa chỉ phát sóng (broadcast) và đa phát sóng (multicast), truyền thông CoAP thông qua các datagram phi kết nối (connectionless) có thể được sử dụng trên các giao thức truyền thông dựa trên các gói.
 UDP có thể dễ dàng triển khai trên các vi điều khiển hơn TCP nhưng các công cụ bảo mật như SSL/TSL(18) không có sẵn, tuy nhiên ta có thể sử dụng Datagram Transport Layer Security (DTLS) để thay thế.
 
Hình 2.2. 6 Giao thức CoAP - Constrained Applications Protocol
AMQP(19) (Advanced Message Queue Protocol)
AMQP là một giao thức làm trung gian cho các gói tin trên lớp ứng dụng với mục đích thay thế các hệ thống truyền tin độc quyền và không tương thích. Các tính năng chính của AMQP là định hướng message, hàng đợi, định tuyến (bao gồm point-to-point và publish-subscribe) có độ tin cậy và bảo mật cao. Các hoạt động sẽ được thực hiện thông qua broker, nó cung cấp khả năng điều khiển luồng (Flow Control).
 Một trong các Message Broker phổ biến là RabbitMQ, được lập trình bằng ngôn ngữ Erlang, RabbitMQ cung cấp cho lập trình viên một phương tiện trung gian để giao tiếp giữa nhiều thành phần trong một hệ thống lớn.
 Không giống như các giao thức khác, AMQP là một giao thức có dây (wire-protocol), có khả năng diễn tả các message phù hợp với định dạng dữ liệu, có thể triển khai với rất nhiều loại ngôn ngữ lập trình.
DDS(20) (Data Distribution Service)
DDS là một ngôn ngữ trung gian dựa vào dữ liệu tập trung được sử dụng để cho phép khả năng mở rộng, thời gian thực, độ tin cậy cao và trao đổi dữ liệu tương tác.
Đây là một giao thức phi tập trung (broker-less) với truyền thông ngang hàng trực tiếp theo kiểu peer-to-peer giữa các publishers và subscribers và được thiết kế để trở thành một ngôn ngữ và hệ điều hành độc lập. DDS gửi và nhận dữ liệu, sự kiện, và thông tin lệnh trên UDP nhưng cũng có thể chạy trên các giao thức truyền tải khác như IP Multicast, TCP / IP, bộ nhớ chia sẻ … DDS hỗ trợ các kết nối được quản lý many-to-many theo thời gian thực và ngoài ra còn hỗ trợ dò tìm tự động (automatic discovery). Các ứng dụng sử dụng DDS cho truyền thông được tách riêng và không yêu cầu sự can thiệp từ các ứng dụng của người dùng, có thể đơn giản hóa việc lập trình mạng phức tạp. Các tham số QoS được sử dụng để xác định các cơ chế tự dò tìm của nó được thiết lập một lần.
XMPP(21) (Extensible Messaging và Presence Protocol)
XMPP (trước đây gọi là “Jabber”) là giao thức truyền thông dùng cho định hướng tin nhắn trung gian dựa trên ngôn ngữ XML(22). 
XMPP là mô hình phân quyền client-server phi tập trung, được sử dụng cho các ứng dụng nhắn tin văn bản. Có thể nói XMPP gần như là thời gian thực và có thể mở rộng đến hàng trăm hàng nghìn nút. Dữ liệu nhị phân phải được mã hóa base64 trước khi nó được truyền đi trong băng tần. XMPP tương tự như MQTT, có thể chạy trên nền tảng TCP.
 
Hình 2.2. 7 Giao thức XMPP - Extensible Messaging và Presence Protocol
2.2.3 Công nghệ cảm biến (Sensor Technology)(23).
Trong Internet of Things, cảm biến đóng vai trò then chốt, nó đo đạt cảm nhận giá trị từ môi trường xung quanh rồi gửi đến bộ vi xử lý sau đó được gửi lên mạng. Chúng ta có thể bắt gặp một số loại cảm biến về cảnh báo cháy rừng, cảnh báo động đất, cảm biến nhiệt độ, cảm biến độ ẩm,.. 
Để giúp cho thiết bị kéo dài được thời gian sống hơn thì đòi hỏi cảm biến cũng phải tiêu hao một lượng năng lượng cực kỳ thấp. Bên cạnh đó độ chính xác và thời gian đáp ứng của cảm biến cũng phải nhanh. Để giá thành của thiết bị thấp thì đòi hỏi giá cảm biến cũng phải thấp. 
 
Hình 2.2. 8 Công nghệ cảm biến
2.3 Một số ứng dụng nổi bật của IoT:
Với những hiệu quả thông minh rất thiết thực mà IoT đem đến cho con người, IoT đã và đang được tích hợp trên khắp mọi thứ, mọi nơi xung quanh thế giới mà con người đang sống. Từ chiếc vòng đeo tay, những đồ gia dụng trong nhà, những mảnh vườn đang ươm hạt giống, cho đến những sinh vật sống như động vật hay con người…đều có sử dụng giải pháp IoT.
 
Hình 2.3. 1 Một số ứng dụng IoT
– Ứng dụng trong lĩnh vực vận tải: Theo dõi lộ trình đi của xe chở hàng,…
– Ứng dụng trong lĩnh vực sản xuất nông nghiệp: Theo dõi tình trạng sinh trưởng của cây trồng,…
 
Hình 2.3. 2 Ứng dụng IoT trong sản xuất nông nghiệp
– Ứng dụng nhà thông minh.
 
Hình 2.3. 3 Ứng dụng IoT Ngôi nhà thông minh
– Ứng dụng trong lĩnh vực y tế: Theo dõi tình trạng sức khỏe bệnh nhân,…
 Hình 2.3. 4 Ứng dụng IoT trong chăm sóc Y Tế
– Ứng dụng trong lĩnh vực giáo dục: Học trực tuyến,… 
 
CHƯƠNG 3. TÌM HIỂU VỀ PHẦN CỨNG.
3.1. Raspberry Pi 3.
 
Hình 3.1. 1 Raspberry Pi 3
	Máy tính Raspberry Pi 3 Model B (Made in UK/Japan) là bo mạch Mini Computer được sử dụng nhiều nhất hiện nay, ngoài việc sử dụng như một máy tính bình thường chạy hệ điều hành Linux hoặc Windows 10 IoT, máy còn có khả năng xuất tín hiệu ra 40 chân GPIO(24) giúp bạn có thể giao tiếp và điểu khiển vô số các board mạch và ngoại vi bên ngoài để thực hiện vô số các ứng dụng khác nhau.
Thông số kỹ thuật chi tiết:
•	Sản xuất tại: nhà máy Sony tại Anh (Made in UK) hoặc Sony tại Nhật (Made in Japan), chính hãng RS Components.
•	1.2GHz 64-bit quad-core ARM Cortex-A53 CPU (BCM2837).
•	1GB RAM (LPDDR2 SDRAM).
•	On-board Wireless LAN - 2.4 GHz 802.11 b/g/n (BCM43438).
•	On-board Bluetooth 4.1 + HS Low-energy (BLE) (BCM43438).
•	4 x USB 2.0 ports.
•	10/100 Ethernet.
•	40 GPIO pins.
•	Full size HDMI 1.3a port.
•	Combined 3.5mm analog audio and composite video jack.
•	Camera interface (CSI).
•	Display interface (DSI).
•	microSD slot.
•	VideoCore IV multimedia/3D graphics core @ 400MHz/300MHz.
 
Hình 3.1. 2 Chi tiết Raspberry Pi 3
3.2. Nguồn cho Raspberry Pi 3 5.1VDC 2.5A Micro USB.
 
Hình 3.2. 1 Nguồn Raspberry Pi 3
Nguồn chính hãng cho Raspberry Pi 5.1VDC 2.5A Micro USB được nhập khẩu từ RS Component là sản phẩm dành cho các bạn có nhu cầu có 1 bộ nguồn tốt và ổn định, đạt các tiêu chuẩn quốc tế dành riêng cho Raspberry Pi, nguồn có thiết kế bảo vệ cách ly, chống sét an toàn, nhiều chuẩn Jack cắm AC khác nhau.
Thông số kỹ thuật:
•	Điện áp đầu vào: 90~264VAC / 47~63Hz.
•	Điện áp đầu ra: 5.1 VDC.
•	Dòng đầu ra: 2.5A.
•	Jack cắm đầu vào: Nhiều kiểu Jack AC khác nhau chuẩn Quốc Tế.
•	Jack cắm đầu ra: Micro USB.
•	Công suất: 13W.
•	Chiều dài cáp: 1.5m.
•	Trọng lương: 150g.
3.3. Thẻ nhớ SanDisk MicroSDHC Ultra 16Gb 80MB/S.
Thẻ nhớ SanDisk MicroSDHC Ultra 16GB 80MB/s thuộc dòng sản phẩm Ultra microSDHC UHS-I Card của SanDisk với độ bền và độ ổn định cao, thẻ có chuẩn Class 10 và tốc độ đọc lên đến 80Mb/s, phù hợp cho các ứng dụng cần độ truy xuất nhanh như Máy tính nhúng, Camera, quay Video,...
3.4. Mạch còi Buzzer.
 
Hình 3.4. 1 Mạch còi Buzzer
Mạch còi buzzer được sử dụng để phát ra âm thanh khi kích tín hiệu, ứng dụng trong các hệ thống báo hiệu, báo trộm,..
Thông số kỹ thuật :
•	Điện áp sử dụng: 3.3~5VDC.
•	Tín hiệu kích: TTL mức thấp Low 0VDC.
•	Kích thước: 32 x 13 mm.
3.5. Sensor Cảm biến ánh sáng quang trở CDS(25).
 
Hình 3.5. 1 Quang trở
Cảm biến ánh sáng quang trở có tích hợp sẵn opamp(26) và biến trở so sánh mức tín hiệu giúp cho việc nhận biết tín hiệu trở nên dễ dàng, sử dụng để nhận biết hay bật tắt thiết bị theo cường độ ánh sáng môi trường.
3.6. Camera.
 
Hình 3.6. 1 Camera
USB Camera cho máy tính nhúng được sử dụng gắn với cổng USB của máy tính nhúng: Raspberry Pi, Orange Pi, Nano Pi, Beaglebone,..., để truyền hình ảnh hoặc âm thanh về máy, camera tương thích với hệ điều hành phổ biến trên máy tính nhúng là Linux hoặc có thể gắn với các máy chạy hệ điều hành Windows và không cần phải cài Driver.
3.7. Động cơ Servo.
Động cơ Digital RC Servo LD-1501 có hộp số bánh răng kim loại, tốc độ phản ứng nhanh với lực kéo khỏe theo thông số nhà sản xuất moment lên đến 17Kg.cm.
Thông số kỹ thuật:
•	Điện áp làm việc: 6~7.2VDC (Kiểm nghiệm thực tế).
•	Dòng tiêu thụ không tải: 100mA, có tải >1500mA.
•	Tốc độ: 0.16sec / 60 ° tại 7VDC.
•	Lực kéo moment: 13Kg.cm 6VDC; 15KG.cm 6.5VDC; 17KG.cm 7VDC.
•	Trọng lượng: 60g.
•	Kích thước: 40 x 20 x 40.5mm.
•	Chiều dài cáp: 30cm.
BẢNG DỰ TRÙ KINH PHÍ
STT	Tên thiết bị	Số lượng	Đơn giá (VND)	Thành tiền (VND)
1	Raspberry Pi 3 Model B (UK/Japan).	1	950.000 VND	950.000 VND
2	Nguồn cho Raspberry Pi 3 5.1VDC 2.5A Micro USB.	1	290.000 VND	290.000 VND
3	Thẻ nhớ SanDisk MicroSDHC Ultra 16Gb 80MB/S.	1	175.000 VND	175.000 VND
4	Màn hình hiển thị LCD Text.	1	110.000 VND	110.000 VND
5	Mạch còi Buzzer.	1	15.000 VND	15.000 VND
6	Bàn phím ma trận 4x4.	1	65.000 VND	65.000 VND
7	Sensor Cảm biến ánh sáng quang trở CDS.	1	18.000 VND	18.000 VND
8	Camera.	1	135.000 VND	135.000 VND
9	Động cơ Servo	1	110.000 VND	110.000 VND
10	Vỏ case cho Raspberry Pi	1	110.000 VND	110.000 VND
11	Depron foam 1m x 1m (Xốp dẻo)	1	95.000 VND	95.000 VND
12	Dao cắt xốp	1	35.000 VND	35.000 VND
13	Keo dán xốp và bản lề	1	30.000 VND	30.000 VND
14	Arduino UNO	1	145.000 VND	145.000 VND
15	Chi phí phát sinh (nếu có)		~	~100.000 VND
Tổng cộng:	~2.413.000 VND
Bảng 3.7. 1 Bảng dự trù kinh phí
 
CHƯƠNG 4. THIẾT KẾ VÀ THỰC HIỆN.
4.1. Hệ điều hành cho Raspberry Pi 3.
	4.1.1 Chuẩn bị hệ điều hành cho Raspberry Pi.
Các hệ điều hành hỗ trợ cho Raspberry Pi bao gồm : Raspbian, Arch Linux ARM, OSMC, OpenELEC, Snappy Ubuntu Core, Ubuntu MATE, Debian Jessie, Windows 10 IoT Core and Android,…
Trong đó Raspbian là một hệ điều hành thuận tiện cho việc cài đặt và sử dụng với sự hỗ trợ lớn từ cộng đồng mã nguồn mở trên thế giới. Raspbian là một hệ điều hành đơn giản và thân thiện.
 
Hình 4.1. 1 Raspberry Pi Desktop
Chúng ta có thể download và sử dụng Raspbian ở 2 dạng : NOOBS hoặc file Raspbian:
•	Với NOOBS (New Out of Box Software), khi thực hiện cài đặt ta sẽ được lựa chọn giữa các hệ điều hành khác nhau cho Raspberry Pi, khi đó ta cũng có thể lựa chọn Raspbian.
•	Với file Raspbian, khi đó sẽ không có quá trình lựa chọn giữa các hệ điều hành, mà Raspbarry Pi sẽ tự thực hiện nhiệm vụ của mình để chuyển tới việc khởi động của Linux kernel. (Hoạt động của Raspberry Pi sau khi cắm nguồn).
•	Download link ở trang chủ Raspberry Pi : 
https://www.raspberrypi.org/downloads/raspbian/ 
	4.1.2 Tiến hành cài đặt hệ điều hành Raspbian.
	- Đầu tiên chúng ta cần tải hệ điều hành Raspbian tại trang chủ.
- Format thẻ nhớ, ta cần format thẻ nhớ MicroSD (bằng phần mềm SDFormatter).
 
Hình 4.1. 2 Phần mềm format thẻ nhớ
- Sau khi đã format chúng ta tiến hành Write file .img đã được tải về vào thẻ nhớ. Có rất nhiều phần mềm hỗ trợ việc này, ở đây bọn em dùng Write32DiskImager.
 
Hình 4.1. 3 Write32DiskImager
- Sau khi đã Write xong thì chúng ta sẽ lắp thẻ nhớ vào và khởi động Raspberry Pi.
 
Hình 4.1. 4 Hình ảnh welcome khi khởi động Raspberry
- Tiếp theo chúng ta sẽ chọn Location cho Pi và timezone, và tạo mật khẩu cho Pi.
 
Hình 4.1. 5 Cửa sổ thiết lập ban đầu của hệ điều hành Raspberry
 
Hình 4.1. 6 Cài đặt mật khẩu
- Chọn 1 Wifi khả dụng, sau đó dùng Pi để kết nối.
- Bật SSH, Camera,…
 
Hình 4.1. 7 Raspberry Pi Configuration
	- Mở terminal(27) lên sau đó update hệ điều hành:
 
Hình 4.1. 8 Cửa sổ terminal
 
Hình 4.1. 9 Lệnh cập nhật hệ điều hành
 
Hình 4.1. 10 Lệnh nâng cấp hệ điều hành
	- Sau khi upgrade xong thì chúng ta có thể bắt đầu sử dụng.
	4.1.3 Sử dụng Raspberry Pi thông qua Laptop/Desktop.
	- Đầu tiên ở Raspberry Pi và Máy tính cần được kết nối cùng mạng với nhau.
	- Ở máy tính (Laptop/Desktop) chúng ta cài phần mềm Advanced Ip Scanner để quét ip của tất cả các máy đang được sử dụng chung mạng. Ở đây Raspberry có ip là: 192.168.1.11
 
Hình 4.1. 11 Quét IP của Raspberry Pi
	- Sau đó dùng phần mềm Remote Desktop Connection của Window ở máy tính để đăng nhập và bắt đầu Remote máy Raspberry Pi.
 
Hình 4.1. 12 Bảng kết nối điều khiển Remote Desktop
	- Ở máy tính, chúng ta điền địa chỉ IP của máy Raspberry Pi vào và nhấn Connect để kết nối. Sau đó điền Username(28) và Password(29) của máy Raspberry Pi vào để bắt đầu làm việc.
 
Hình 4.1. 13 Màn hình đăng nhập Raspberry Pi
4.2. Khái quát về các thư viện.
	4.2.1 Thư viện OpenCV.
 
Hình 4.2. 1 Open CV
	OpenCV là một thư viện mã nguồn mở hàng đầu cho lĩnh vực thị giác máy tính (computer vision), xử lý ảnh và máy học, và các tính năng tăng tốc GPU trong hoạt động thời gian thực. OpenCV được phát hành theo giấy phép BSD, do đó nó hoàn toàn miễn phí cho cả học thuật và thương mại. Nó có các interface C++, C, Python, Java và hỗ trợ Windows, Linux, Mac OS, iOS và Android. OpenCV được thiết kế để tính toán hiệu quả và với sự tập trung nhiều vào các ứng dụng thời gian thực. Được viết bằng tối ưu hóa C/C++, thư viện có thể tận dụng lợi thế của xử lý đa lõi. Được sử dụng trên khắp thế giới, OpenCV có cộng đồng hơn 47 nghìn người dùng và số lượng download(30) vượt quá 6 triệu lần. Phạm vi sử dụng từ nghệ thuật tương tác, cho đến lĩnh vực khai thác mỏ, bản đồ trên web hoặc công nghệ robot.
	OpenCV đang được sử dụng rộng rãi trong các ứng dụng bao gồm:
•	Giám sát giao thông.
•	Kiểm tra và giám sát tự động.
•	Robot và xe hơi tự lái.
•	Phân tích hình ảnh y tế.
•	Tìm kiếm và phục hồi hình ảnh/video.
•	Phim - cấu trúc 3D từ chuyển động.
•	Nghệ thuật sắp đặt tương tác.
OpenCV có thể thực hiện những tính năng như sau:
•	Image/video I/O, xử lý, hiển thị (core, imgproc, highgui).
•	Phát hiện các vật thể (objdetect, features2d, nonfree).
•	Geometry-based monocular or stereo computer vision (calib3d, stitching, videostab).
•	Computational photography (photo, video, superres).
•	Machine learning & clustering (ml, flann).
•	CUDA  acceleration (gpu).
Tham khảo thêm tại https://opencv.org
4.2.2 Thư viện Numpy (Nummerical Python).
 
Hình 4.2. 2 Thư viện Numpy
Numpy (viết tắt của Nummerical Python) là một thư viện không thể thiếu khi chúng ta xây dựng các ứng dụng máy học trên Python. Numpy cung cấp các đối tượng và phương thức để làm việc với mảng nhiều chiều và các phép toán đại số tuyến tính. Trong numpy, chiều của mảng gọi là axes; trong khi số chiều gọi là rank.
Thư viện chính trong numpy là các đối tượng mảng (array). Mảng (array) tương tự như list(31) ở Python với điều kiện là mọi phần tử trong array phải có cùng kiểu dữ liệu. Array có thể thao tác với số lượng lớn dữ liệu số, thường là float hay int, và hiệu quả hơn trên danh sách rất nhiều.  Lớp thường dùng trong numpy là ndarray(32) (n-dimentional array).
	4.2.3 Cài đặt thư viện.
	Sau khi đã update hệ điều hành raspbian mới nhất chúng ta cần phải cài đặt thêm một số developer tools, cùng với Cmake.
 
Hình 4.2. 3 Cài đặt Cmake và một số công cụ khác
Tiếp theo, chúng ta cần cài đặt I/O image packages (dùng để giúp chúng ta tải các định dạng tệp hình ảnh khác nhau từ đĩa. Ví dụ về các định dạng tệp như vậy bao gồm JPEG, PNG, TIFF,…).
 
Hình 4.2. 4 Lệnh cài đặt I/O image Packages

Cũng giống như chúng ta cần I/O image packages, chúng ta cũng cần I/O video packages. Các thư viện này cho phép chúng tôi đọc các định dạng tệp video khác nhau từ đĩa cũng như làm việc trực tiếp với các luồng video:
 
Hình 4.2. 5 Lệnh cài đặt I/O video packages

Tiếp theo cài đặt OpenCV phiên bản 3.1.0
 
Hình 4.2. 6 Lệnh cài đặt OpenCV 3.1.0

Trước khi chúng tôi có thể bắt đầu biên dịch OpenCV trên Raspberry Pi 3, trước tiên chúng tôi cần cài đặt pip, trình quản lý gói Python:
 
Hình 4.2. 7 Lệnh cài đặt pip
Cài đặt thêm môi trường ảo:
 
Hình 4.2. 8 Lệnh cài đặt môi trường ảo
 
Hình 4.2. 9 Lệnh cài đặt môi trường ảo
 
Hình 4.2. 10 Lệnh cài đặt môi trường ảo
Tạo môi trường ảo cho python:
 
Hình 4.2. 11 Lệnh cài đặt môi trường ảo cho Python
 
Hình 4.2. 12 Lệnh cài đặt môi trường ảo cho Python
 
Kiểm tra môi trường ảo đã được cài đặt hay chưa:
 
Hình 4.2. 13 Lệnh xem môi trường ảo đã đưuọc ài đặt chưa
 
Hình 4.2. 14 Môi trường ảo đã được cài đặt
Tại môi trường ảo chúng ta cài thêm Numpy, gói python để xử lý số:
 
Hình 4.2. 15 Lệnh cài đặt Numpy
 
Hình 4.2. 16 Lệnh cài đặt Numpy
Kiểm tra các gói cài đặt:
 
Hình 4.2. 17 Kiểm tra các gói cài đặt
Biên dịch CV (với khoảng thời gian thực hiện khá lâu 4 giờ đến 5 giờ):
 
Hình 4.2. 18 Biên dịch
 
Hình 4.2. 19 Lệnh biên dịch

Từ đó, việc cuối cùng chúng ta cần làm sau khi biên dịch thành công là cài đặt OpenCV.
 
Hình 4.2. 20 Cài đặt OpenCV
Chạy thử chương trình
Chạy thử đoạn code như hình dưới đây kiểm tra việc nhận diện khuôn mặt, nếu nhận diện được khuôn mặt sẽ được đóng khung lại:
 
Hình 4.2. 21 Đoạn code kiểm tra việc nhận diện khuôn mặt

Đây là kết quả:
 
Hình 4.2. 22 Kết quả nhận diện
 
Hình 4.2. 23 Kết quả nhận diện
4.2.4 Thư viện Imaging (PIL).
	Thư viện này hỗ trợ nhiều định dạng tập tin, và cung cấp khả năng xử lý hình ảnh và đồ hoạ mạnh mẽ. Hôm nay tôi sẽ hướng dẫn các bạn cách để thao tác và làm việc với thư viện Imaging (PIL).
Tạo ảnh: Imaging cho phép bạn tạo được một hình ảnh trong Python với đầy đủ kích thước,  màu sắc,...
Mở ảnh: Cho phép bạn mở một tấm ảnh đã có sẵn lên để thực hiện các thao tác khác như sao chép, chỉnh sửa,..
Hiển thị ảnh: Thao tác này chủ yếu được dùng cho mục đích gỡ lỗi trong quá trình làm việc với các tấm ảnh. Trên hệ điều hành windows, khi thực thi lệnh này nó lưu hình ảnh vào một tâp tin BMP tạm thời và sử dụng các tiện ích tiêu chuẩn để hiển thị hình ảnh lên.
Lưu ảnh: outfile: Tên tập tin hoặc đối tượng tập tin; Format: Định dạng tuỳ chọn. Nếu bỏ qua, các định được xác định từ phần mở rộng của tên tập tin. Trường hợp sử dụng đối tượng tập tin thay vì tên tập tin thì thông số này luôn được sử dụng; Options: Thông số bổ sung.
4.2.5 Thư  viện os.
	Thư viện os cung cấp những chức năng thuộc hệ điều hành. Ví dụ như để đọc thông tin từ tệp, thao tác với đường dẫn,…
4.2.6 Thư viện argparse.
	Thư viện này giúp giải quyết dễ dàng các giao diện dòng lệnh (terminal) với người dùng. Chương trình xác định những đối số mà nó yêu cầu và argparse sẽ tìm cách phân tích nhúng chúng ra khỏi sys.argv. Nó cũng tự động tạo thông báo trợ giúp, sử dụng và phát sinh lỗi khi người dùng đưa ra các đối tượng không hợp lẹ.
	4.2.7 Thư viện MySQLdb
	Thư viện Cơ sở dữ liệu MySQL (Sẽ được làm rõ hơn ở phần 4.3).
	4.2.8 Thư viện time
	Thư viện time cung cấp các chức năng liên quan đến thời gian.
4.2.9 Nền tảng Python
Python là ngôn ngữ lập trình hướng đối tượng, cấp cao, mạnh mẽ, được tạo ra bởi Guido van Rossum. Nó dễ dàng để tìm hiểu và đang nổi lên như một trong những ngôn ngữ lập trình nhập môn tốt nhất cho người lần đầu tiếp xúc với ngôn ngữ lập trình. Python hoàn toàn tạo kiểu động và sử dụng cơ chế cấp phát bộ nhớ tự động. Python có cấu trúc dữ liệu cấp cao mạnh mẽ và cách tiếp cận đơn giản nhưng hiệu quả đối với lập trình hướng đối tượng. Cú pháp lệnh của Python là điểm cộng vô cùng lớn vì sự rõ ràng, dễ hiểu và cách gõ linh động làm cho nó nhanh chóng trở thành một ngôn ngữ lý tưởng để viết script và phát triển ứng dụng trong nhiều lĩnh vực, ở hầu hết các nền tảng.
 
Hình 4.2. 24 Python
Tính năng của Python:
- Ngôn ngữ lập trình đơn giản, dễ học: Python có cú pháp rất đơn giản, rõ ràng. Nó dễ đọc và viết hơn rất nhiều khi so sánh với những ngôn ngữ lập trình khác như C++, Java, C#.
- Miễn phí, mã nguồn mở: Bạn có thể tự do sử dụng và phân phối Python, thậm chí là dùng cho mục đích thương mại.
- Khả năng di chuyển: Các chương trình Python có thể di chuyển từ nền tảng này sang nền tảng khác và chạy nó mà không có bất kỳ thay đổi nào.
- Khả năng mở rộng và có thể nhúng: Giả sử một ứng dụng đòi hỏi sự phức tạp rất lớn, bạn có thể dễ dàng kết hợp các phần code bằng C, C++ và những ngôn ngữ khác (có thể gọi được từ C) vào code Python.
- Ngôn ngữ thông dịch cấp cao: Không giống như C/C++, với Python, bạn không phải lo lắng những nhiệm vụ khó khăn như quản lý bộ nhớ, dọn dẹp những dữ liệu vô nghĩa,...
- Thư viện tiêu chuẩn lớn để giải quyết những tác vụ phổ biến: Python có một số lượng lớn thư viện tiêu chuẩn giúp cho công việc lập trình của bạn trở nên dễ thở hơn rất nhiều, đơn giản vì không phải tự viết tất cả code.
- Hướng đối tượng: Mọi thứ trong Python đều là hướng đối tượng.
4.2.10 ArduinoIDE
	Intergrated Development Environment (IDE) là công cụ được sử dụng để lập trình cho các board Arduino.
 
Hình 4.2. 25 ArduinoIDE
4.3. Cài đặt Cơ sở dữ liệu và cấu hình.
4.3.1 Giới thệu về My SQL.
MySQL là một loại cơ sở dữ liệu theo cấu trúc quan hệ (RDBMS – Relational Database Management System) dùng để lưu và quản lý khối lượng lớn dữ liệu. MySQL được gọi là cơ sở dữ liệu quan hệ vì nó sử dụng các cấu trúc bảng để lưu trữ dữ liệu, các bảng có mối quan hệ với nhau thông qua các khóa. 
MySQL là một hệ cơ sở dữ liệu theo cấu trúc quan hệ dễ dàng sử dụng và quản lý, MySQL thường được sử dụng cho nhiều công việc từ lớn tới nhỏ. Nó phổ biến vì nhiều lý do như sau: 
•	MySQL là mã nguồn mở, nó hoàn toàn miễn phí. 
•	MySQL là một chương trình rất mạnh mẽ. 
•	MySQL sử dụng một form chuẩn của ngôn ngữ dữ liệu nổi tiếng là SQL. 
•	MySQL làm việc được trên nhiều hệ điều hành cùng với nhiều ngôn ngữ phổ biến như PHP, PERL, C, C++, Java… 
•	MySQL làm việc nhanh và khỏe ngay cả với các tập dữ liệu lớn. 
•	MySQL rất thân thiện với PHP, một ngôn ngữ thường được dùng để phát triển web
4.3.2 Cài đặt
Cài đặt qua lệnh: 
 
Hình 4.3. 1 Lệnh cài đặt MySQL
Sau khi cài đặt xong, tạo thử một cơ sở dữ liệu và phân quyền cho tài khoản truy cập. Tạo một cơ sở dữ liệu mới (USER database). Tạo tài khoản: monitor@localhost và phân quyền ALL ( tất cả mọi quyền) cho tài khoản này.

 
Hình 4.3. 2 Lệnh tạo cơ sở dữ liệu và phân quyền truy cập
 
Hình 4.3. 3 Lệnh tạo cơ sở dữ liệu và phân quyền truy cập
 
Đăng nhập vào MySQL với tài khoản monitor. 
 
Hình 4.3. 4 Đăng nhập vào MySQL
Sau đó tạo bảng Detail bao gồm các thuộc tính ID, tên người sử dụng (Name), ngày sử dụng(tdate), giờ sử dụng (ttime).
 
Hình 4.3. 5 Tạo bảng Detail
Thêm và xóa dử liệu vào CSDL thông qua python.
 
Hình 4.3. 6 Thêm dữ liệu vào cơ sở dữ liệu

 
Hình 4.3. 7 Xóa dữ liệu trong cơ sở dữ liệu
 
Kết quả:
 
Hình 4.3. 8 Kết quả
4.4. Cài đặt Web server (Apache web server) và phpMyAdmin:
4.4.1 Cài đặt Apache Web server:
Apache là một ứng dụng web server phổ biến nhất trên thế giới và có thể cài đặt trên Raspberry Pi, cho phép bạn public một hoặc nhiều website ra Internet
Mặc định, Apache chỉ hỗ trợ các file HTML, tuy nhiên với một vào modules(33) bổ sung, chúng ta có thể chạy được Apache(34) với các file PHP.
Thực hiện câu lệnh sau đây để tiến hành cài đặt Apache trên Raspberry Pi:
 
Hình 4.3. 9 Lệnh cài đặt Apache web server
Mặc định, Apache sẽ chạy một file test HTML sau khi cài đặt xong. Ta chỉ cần mở trình duyệt lên, gõ địa chỉ IP của Raspberry Pi hoặc gõ localhost. 
Nếu Apache cài đặt thành công bạn sẽ nhìn thấy như hình dưới:
 
Hình 4.3. 10 Cài đặt thành công Apache web server
4.4.2 Cài đặt phpMyAdmin:
phpMyAdmin là một ứng dụng web miễn phí cung cấp GUI(35) sử dụng kết hợp với hệ thống quản lý cơ sở dữ liệu MySQL. Đây là công cụ quản trị MySQL phổ biến nhất được sử dụng bởi hàng triệu người dùng trên toàn thế giới và đã giành được nhiều giải thưởng.
Với phpMyAdmin, bạn có thể:
 + Tạo và xóa người dùng, quản lý quyền người dùng.
 + Tạo, thay đổi và xóa cơ sở dữ liệu, bảng, trường và hàng.
 + Tìm kiếm đối tượng trong toàn bộ cơ sở dữ liệu hoặc trong bảng.
 + Nhập và xuất dữ liệu theo các định dạng khác nhau, bao gồm SQL, XML và CSV.
 + Giám sát quá trình và theo dõi hiệu suất của các truy vấn khác nhau.
 + Thực hiện các truy vấn SQL tùy chỉnh.
 + Sao lưu cơ sở dữ liệu MySQL của bạn ở chế độ thủ công.
 
Hình 4.4. 1 PHPMyAdmin
Để cài đặt phpMyAdmin chúng ta thực hiện câu lệnh dưới đây:
 
Hình 4.4. 2 lệnh cài đặt PhpMyAdmin
Sau đó, khởi động lại Apache để các thay đổi của bạn được thực thi:
 
Hình 4.4. 3 Lệnh khởi động lại Apache
Sau khi đã cài đặt thành công thì chúng ta có thể sử dụng phpMyAdmin bằng cách vào trình duyệt và đăng nhập vào tài khoản của MySQL:
 
Hình 4.4. 4 Tên miền để truy cập vào phpMyAdmin
 
Hình 4.4. 5 Cửa sổ đăng nhập vào cơ sở dữ liêu
 
Hình 4.4. 6 Cửa sổ chính trong phpMyAdmin
 
4.5. Tiến hành cài đặt các thư viện liên quan khác:
	4.5.1. RPi.GPIO.
	- Lệnh cài đặt RPi.GPIO.
 
Hình 4.5. 1 Lệnh cài đặt RPi.GPIO
	- Sử dụng RPi.GPIO trong python bằng cách:
 
Hình 4.5. 2 Sử dụng thư viện RPi.GPIO
	4.5.2. Thư viện Imaging (PIL(36))
	Đôi lúc bạn sẽ gặp phải các vấn đề về xử lý hình ảnh trong công việc của mình. Python cho phép bạn thực hiện điều đó dễ dàng thông qua thư viện Imaging (PIL). Thư viện này hỗ trợ nhiều định dạng tập tin, và cung cấp khả năng xử lý hình ảnh và đồ hoạ mạnh mẽ.
	- Lệnh cài đặt thư viện PIL: “sudo python3 setup.py install”.
	4.5.3. Kết nối các thiết bị theo mạch sơ đồ.
 
Hình 4.6. 1 Mạch sơ đồ kết nối các thiết bị
4.6. Tiến hành lắp ráp mô hình:
	4.6.1. Chuẩn bị dụng cụ. 
	- Xốp Depron foam 5mm x 1m x 1m.
 
Hình 4.6. 6 Xốp Depron foam 5mm x 1m x 1m
	- Bản lề 2 lỗ 27mm x 38mm.
 
Hình 4.6. 7 Bản lề 2 lỗ 27mm x 38mm
- Keo dán 25 gram EPO – EPP – Depron.
 
Hình 4.6. 8 Keo dán 25 gram EPO - EPP - Depron
- Dao rọc giấy hobby knife.
 
Hình 4.6. 9 Dao rọc giấy hobby knife
- Các dụng cụ phụ khác như thước kẻ, bút, băng keo.
4.6.2. Thực hiện.
Kết quả sau khi dựng mô hình và lắp ráp thiết bị:
 
Hình 4.6. 10 Mô hình sau khi đã lắp ráp
 
Hình 4.6. 11 Mô hình sau khi đã lắp ráp
4.7. Tiến hành code và chạy thử:
	Sau khi đã thực hiện nối các thiết bị theo đúng các cổng trong sơ đồ ở mục 4.6.1 thì chúng ta tiến hành code để thực hiện các chức năng.
[Link Code]: https://github.com/thanghuynh2608/KLTN---Robot-face-recognizer
	Kết quả: 
	- Đèn LED trắng (tượng trung bóng đèn) phát sáng trong điều kiện môi tường xung quanh thiếu sáng.
 
Hình 4.7. 1 Kết quả hoạt động của sensor quang trở
	- Đèn màu vàng phát sáng là khi chúng ta nhấn nút nhận diện và camera đang phân tích khuôn mặt.
 
Hình 4.7. 2 Camera bắt đầu phân tích khuôn mặt
	- Nếu sai người đã được máy học trước đó thì đèn màu đỏ sẽ sáng và mạch còi Buzzer sẽ phát ra âm thanh.
 
Hình 4.7. 3 Chương trình báo sai
	- Nếu chương trình nhận đúng người thì đèn màu xanh lục phát sáng và đồng thời chốt khóa cửa sẽ tự động quay 45 độ và lúc đó chúng ta có thể mở cửa.
 
Hình 4.7. 4 Chương trình báo đúng và mở cửa
 
CHƯƠNG 5: KẾT LUẬN.
5.1. Kết quả đạt được.
	- Kết nối được các thiết bị như là đèn LED, camera, còi buzzer, nút bấm, servo, sensor, mạch arduino uno vào Raspberry Pi 3.
	- Cài đặt được các thư viện cần thiết như: OpenCV, MySQL, phpMyAdmin, RPi.GPIO, Imaging (PIL), cùng các thư viện và chương trình hỗ trợ khác.
	- Tạo cơ sở dữ liệu người dùng và thao tác thêm xóa sửa dữ liệu người dùng.
	- Điều khiển các đèn LED, servo bằng code python.
	- Thực hiện được việc chụp và lấy dữ liệu người dùng để huấn luyện máy tự học và phân tích khuôn mặt người.
	- Nhận diện được người dùng đã được máy học từ những dữ liệu hình ảnh đã thu thập.
5.2. Những chắc năng chưa thực hiện được.
	Trong khi thực hiện đồ án, có những lỗi và sự cố xảy ra khiến nhóm vẫn chưa thể hoàn thành được chức năng mà nhóm mong muốn. Các chức năng mà nhóm vẫn chưa thực hiện được là: 
	- Bàn phím mật khẩu. (Chức năng năng của bàn phím số là thực hiện nhập mật khẩu để mở khóa cửa thay cho nhận diện khuôn mặt trong những lúc chương trình nhận diện bị lỗi.)
	- Màn hình Led LCD hiển thị thông tin. (Chức năng của màn hình Led là hiển thị thông báo đúng sai cũng như hiện thông báo chương trình đang chạy hay đang ngừng hoạt đông.)
5.3. Hướng phát triển.
	Hệ thống có thể được phát triển thêm với chức năng sử dụng bàn phím để nhập mật khẩu bằng tay và hiển thị lên màn hình LCD. Phát triển nguồn điện dự phòng để tránh trường hợp mất điện khi khẩn cấp. Gửi và nhận thông tin thông qua điện thoại di động (SMS hoặc Email). Kết hợp phát triển với mô hình nhà thông minh.
 
Hình 5.3. 1 Biểu tượng cho sự phát triển
 
Bảng phân công công việc.
Tuần	Nội dung thực hiện	Người thực hiện
1	Thu thập thông tin về nhu cầu sử dụng thiết bị IoT.
Tìm hiểu về những trang thiết bị đã có về nhận diện khuôn mặt.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
2	Lập bảng kế hoạch dự định, vạch ra hướng đi cụ thể từng tuần.
Mô tả dự án cho giảng viên hướng dẫn.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
3	Tìm hiểu về mô hình IoT và ứng dụng.
Tìm hiểu về các giao thức truyền tải dữ liệu.
Tiến hành viết báo cáo.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
4	Tìm hiểu về các hiểu về thiết bị phần cứng và chức năng.
Tìm hiểu về hệ điều hành dành cho Raspberry Pi (cách cài đặt và sử dụng).
Tiến hành viết báo cáo.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
5	Tiến hành mua các thiết bị cần thiết (Raspberry Pi, Camera, Động cơ Servo,… ).
Tiến hành cài đặt hệ điều hành và Raspberry và chương trình cần thiết để kết nối Pi với thiết bị và điều khiển bằng máy tính.
Tiến hành viết báo cáo.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
6	Tìm hiểu về các thư viện cần thiết (OpenCV,…) dùng cho dự án.
Tiến hành cài đặt thư viện.
Demo thử nhận diện khuôn mặt.
Tiến hành viết báo cáo.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
7	Tìm hiểu về Web Server và Cơ sở dữ liệu (MySQL), phpMyAmin.
Tiến hành cài đặt Apache web server, MySQL, phpMyAdmin. Dùng MySQL để lưu lại thông tin người sử dụng.
Thêm xóa dữ liệu vào cơ sở dữ liệu khi nhận diện được.
Tiến hành viết báo cáo.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
8	Tối ưu hệ thống nhận diện khuôn mặt.
Kết hợp sử dụng động cơ RC để khóa cửa, các nút bấm để sử dụng đóng/mở và điều khiển các đèn led báo hiệu.
Tiến hành viết báo cáo.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
9	Mua thiết bị để xây dựng mô hình. Tiến hành xây dựng bản thảo cho hệ thống, kết nối thiết bị.
Kết hợp xử lí cơ sở dữ liệu, lưu ảnh người nhận diện đúng/sai.
Tiến hành viết báo cáo.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
10	Dựa theo bản thảo hệ thống đã hoàn thành, tiến hành lắp ráp thiết bị cần thiết.
Thêm còi thông báo buzzer cho hệ thống..
Tiến hành viết báo cáo.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
11	Hoàn thiện mô hình.
Thêm cảm biến ánh sáng (quang trở) cho hệ thống để phát đèn khi không đủ ánh sáng.
Tiến hành viết báo cáo.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
12	Chỉnh sửa mô hình.
Tối ưu lại những đoạn mã (code) của nhận diện.
Tiến hành viết báo cáo tổng hợp.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
13	Chỉnh sửa những lỗi phát sinh.
Làm poster cho hệ thống.
Tiến hành viết báo cáo tổng hợp.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
14	Chỉnh sửa những lỗi phát sinh.
Làm poster, làm slide trình chiếu.
Tiến hành viết báo cáo tổng hợp.
Báo cáo tổng quan cho giảng viên hướng dẫn.	Nguyễn Trung Tú
Huỳnh Quốc Thắng
15	Hoàn thiện chương trình, mô hình, các phần liên quan như word, powerpoint.
Hoàn thành viết báo cáo tổng hợp.
Báo cáo cho giảng viên hướng dẫn.	Huỳnh Quốc Thắng
Nguyễn Trung Tú
Bảng phân công công việc 1 
Tài liệu tham khảo.
	Tiếng Việt
	[1]. MLAB (2017), “Lập trình web-server trên Raspberry pi”, http://mlab.vn/24025-bai-10-lap-trinh-web-server-tren-raspberry-pi-%E2%80%93-phan-1.html
	[2]. raspberrypi.vn (2018), “Cài đặt Web server và PHP, MySQL trên Raspbian”, https://raspberrypi.vn/thu-thuat-raspberry-pi/cai-dat-web-server-va-php-mysql-tren-raspbian-847.pi
	[3]. Dandientu.com (06-10-2018), “Hướng dẫn điều khiển động cơ Servo bằng Raspberry Pi dùng ngôn ngữ Python”, http://dandientu.com/lap-trinh-nhung/huong-dan-dieu-khien-dong-co-servo-bang-raspberry-pi-dung-ngon-ngu-python.html
	[4]. MLAB (2019), “Lập trình cơ bản Raspberry Pi với GPIO”, http://mlab.vn/13456-bai-1-lap-trinh-co-ban-raspberry-pi-voi-gpio.html
	[5]. arduino.vn (22-06-2014), “Cách đọc dữ liệu từ quang trở và xây dựng cảm biến ánh sáng”, http://arduino.vn/bai-viet/208-cach-doc-du-lieu-tu-quang-tro-va-xay-dung-cam-bien-anh-sang
[6]. Bkaii.com.vn (2018) “IoT - Internet Of Thing: 5 giao thức dùng để "nói chuyện" mà bạn cần biết”, http://bkaii.com.vn/tin-tuc/175-iot-internet-of-thing-5-giao-thuc-dung-de-noi-chuyen-ma-ban-can-biet
[7]. Stdio.vn (05/08/2015) “Làm quen với thư viện Imaging (PIL)” https://www.stdio.vn/articles/lam-quen-voi-thu-vien-imaging-pil-phan-1-co-ban-333
[8]. Raspberrypi.vn (13/03/2017) “Hướng dẫn cài hệ hành cho Raspberry Pi”, https://raspberrypi.vn/thu-thuat-raspberry-pi/huong-dan-cai-dieu-hanh-cho-raspberry-pi-2457.pi
Tiếng Anh
	[9]. Adrian Rosebrock (Jun.  2018), “Raspberry Pi Face Recognition”, https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/?fbclid=IwAR1uk40CYCwBogqDF80qRtqO9a9DCl23F3mKJ53S0CyQViGi6hyas3DvAhQ
	[10]. Adrian Rosebrock (Jun. 2018), “Face recognition with OpenCV, Python, and deep learning”, https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/?fbclid=IwAR0MjyXQRnxJvB6bO5JESpdY_D4EJcq6AhoKmHA0o6Agl0pudAuTMxgKHMs
	[11]. Adam Geitgey (2017), “face_recognition”, https://github.com/ageitgey/face_recognition?fbclid=IwAR0MSPz36qaiw6lkqayzhYIXE8YBduX8wOuJgFj8Wz9bYaZHbKrwomvMoSo
	[12]. Ardumotive_com (2018), “Raspberry Pi Tutorial: How to Use a Buzzer”, https://www.instructables.com/id/Raspberry-Pi-Tutorial-How-to-Use-a-Buzzer/
	[13]. Python Software Foundation [US] (2018), “os — Miscellaneous operating system interfaces”, https://docs.python.org/3/library/os.html
	[14]. Python Software Foundation [US] (2018), “argparse — Parser for command-line options, arguments and sub-commands”, https://docs.python.org/3/library/argparse.html
	[15]. Andy Dustman (2017), “MySQLdb User's Guide”, http://mysql-python.sourceforge.net/MySQLdb.html 
	[16]. Python Software Foundation [US] (2018), “time — Time access and conversions”, https://docs.python.org/3/library/time.html

