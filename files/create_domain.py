domain_path = '/u02/app/fmw/weblogic/Weblogic12C/user_projects/domains/mydomain'
admin_password = 'Welcome1'

readTemplate('/u02/app/fmw/weblogic/wlserver/common/templates/wls/wls.jar')
cd('Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', 7001)

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_password)

setOption('OverwriteDomain', 'true')
writeDomain(domain_path)
closeTemplate()
exit()

