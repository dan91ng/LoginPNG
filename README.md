# login-voice

登录失败时使用笔记本摄像头进行拍照

## 用法

1. 添加两个计划任务，一个用于拍照，在登录失败时触发(python main.py)；另一个用于发送邮件，5分钟执行一次(python sendmail.py)

2. main.py拍照脚本会将照片存储在D:\code\python\video下；邮件发送脚本在识别到上述路径下有png文件时，将自动发送，发送成功后删除照片

3. 拍照脚本触发器：发生事件时，日志：Security，事件ID：4625；邮件发送脚本触发器：一次，在某个时间时-触发后，无限期的没隔5分钟重复运行一次

4. 要悄悄拍照记得用黑胶带贴住笔记本摄像头的灯

[![](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrQ2xVZlBsTEJJV3hkazhOVzdZYTRTVT0=)](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrQ2xVZlBsTEJJV3hkazhOVzdZYTRTVT0=)

[![](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrT1ZLd3l5VnMwdm1SUWtiUEI3ZzlNTT0=)](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrT1ZLd3l5VnMwdm1SUWtiUEI3ZzlNTT0=)

[![](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrR3FENkR6YUczbDFqM2hCOE5sTXFiVT0=)](https://img.gouka.la/application/hide.php?key=blBlcVhOaUhreEg1K3EybFA5dTFrR3FENkR6YUczbDFqM2hCOE5sTXFiVT0=)