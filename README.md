Project Overview
此项目专注于实现物联网(IoT)环境下的PM2.5数据采集、处理、预测与可视化。具体包括从传感器收集数据、通过EMQX服务器将数据发布到边缘虚拟机，然后清洗和计算每日平均数据，并将这些清洗后的数据发送到云虚拟机进行可视化和未来数值的预测。

Key Achievements
Data Collection: 收集了2023年6月1日至2023年8月31日之间的PM2.5数据。
Data Processing: 在边缘端执行了数据清洗与初步处理，包括过滤异常值并计算PM2.5的平均值。
Machine Learning: 利用Prophet模型进行时间序列分析，预测了未来的PM2.5浓度趋势。
Visualization: 使用Matplotlib创建图表来展示历史数据和预测结果。
Implementation Details
项目通过以下步骤实现目标：

数据注入组件设计：
通过Docker拉取并运行EMQX消息代理服务器。
编写发布者程序，该程序从Urban Observatory平台获取PM2.5数据并通过EMQX服务器发送。
清洗数据，只保留PM2.5相关的数据。
启动发布者程序并将数据发送至EMQX服务器。
数据预处理操作设计：
在边缘虚拟机上编写订阅者程序接收PM2.5数据，并打印至控制台。
清洗数据，计算平均PM2.5值。
编写Dockerfile和docker-compose配置文件，用于构建并运行数据预处理服务。
拉取并运行RabbitMQ消息队列服务。
编写生产者程序，将数据发送至云端的RabbitMQ服务器。
时间序列数据预测与可视化：
编写消费者程序从RabbitMQ获取数据。
使用图表工具对RabbitMQ中的数据进行可视化。
将数据传入机器学习组件进行预测。
图形显示预测结果。
Technologies Used
Docker: 实现组件的容器化部署。
EMQX: MQTT协议的消息队列服务。
RabbitMQ: 云与边缘之间可靠高效的数据通信。
Python: 数据处理与机器学习脚本语言。
Prophet: 时间序列预测模型。
Matplotlib: 数据可视化库。
![PM25_data](https://github.com/user-attachments/assets/fc65ad72-6e69-42a4-916e-9e72726e7de6)
![prediction](https://github.com/user-attachments/assets/a02bb296-337e-4c29-8175-06e042a8e79c)

