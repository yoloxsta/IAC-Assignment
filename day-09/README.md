### Day-09 (Password base auth (AWS))

```
- sudo adduser soetintaung
- sudo passwd soetintaung


root@ip:/etc/ssh# grep -Ri passwordauthentication /etc/ssh/sshd_config*
/etc/ssh/sshd_config:PasswordAuthentication yes
/etc/ssh/sshd_config:# PasswordAuthentication.  Depending on your PAM configuration,
/etc/ssh/sshd_config:# PAM authentication, then enable this but set PasswordAuthentication
/etc/ssh/sshd_config.d/60-cloudimg-settings.conf:PasswordAuthentication no
/etc/ssh/sshd_config.d/movieuat.conf:    PasswordAuthentication yes
root@ip:/etc/ssh#


```