Dell Server Oil Cooling Transformation Temperature Monitoring Fan Speed Control Script  
戴尔服务器油冷改造温度监控风扇转速控制脚本

我们公司提供专业企业信息化及SAAS服务，以下是公司产品网站，欢迎大家使用：  
主页: http://www.gzdaodao.cn  
医疗器械GSP云: http://www.gspsys.cn  
关务云: http://www.guanwuyun.cn  
企业互联云: http://www.b2blinks.cn  


【注意】此脚本需要安装ipmi工具,并且只能用在戴尔服务器上
此脚本通过ipmi工具检查服务器温度，当温度低于脚本中的设定值时，脚本会将服务器风扇转速设为固定值，默认是20%  
当温度大于设定值时，脚本会将服务器风扇调回自动模式，让服务器控制风扇转速降温。   

此改造保留原风冷系统，作为油冷系统故障备份，  
油冷冷却液采用10号变压器油。
以下是1U服务器又冷改造照片：  

![image](images/1.jpg)  
![image](images/2.jpg)  
