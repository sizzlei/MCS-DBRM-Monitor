# MCS-DBRM-Monitor
MariaDB Columnstore의 DBRM이 ReadOnly Mode로 변경되는 것을 모니터링 하기 위한 간단한 스크립트 입니다. 
모니터링 서버와 대상 서버간 SSH KEY 가 등록되어야 합니다.패스워드를 이용할 경우 변수 추가 및 SSH 접근 구문 변경이 필요합니다. 
알림은 runTelegram 모듈을 활용합니다. 

## Crontab
<code>
# DBRM Checker
*/5 * * * * /usr/local/bin/python3 /project/DBRMChecker
</code>
