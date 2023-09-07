# ch3
- python version 3.7.16<br/>
- pip list<br/>
  ><b>Package           Version</b><br/><br/>
      asgiref           3.7.2<br/>
      Django            3.2.20<br/>
      mod-wsgi          4.9.4<br/>
      pip               23.2.1<br/>
      pytz              2023.3<br/>
      setuptools        65.5.1<br/>
      sqlparse          0.4.4<br/>
      typing_extensions 4.7.1<br/>
      uWSGI             2.0.22<br/>
      wheel             0.38.4

<br/><br/>

## 웹 서버 연동
### 1. apache2(http) 설정
* 'mysite/settings.py' 수정
* apache(httpd) 설정 파일 수정<br/>
  \- 위치: /usr/local/etc/httpd/httpd.conf<br/>
  \- 참고: 'docs/config_apache.txt'

### 2. nginx 설정
* 