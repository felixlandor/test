@echo off
echo 正在启动iSCSI服务
sc start MSiSCSI
echo.
echo.
if %errorlevel%==0 (
    echo iSCSI服务启动成功。
) else (
	sc stop MSiSCSI
	sc start MSiSCSI
	if %errorlevel%==0 (echo iSCSI服务启动成功。) else (echo 启动iSCSI服务失败。)
)
pause
