<?php
# Этот файл был автоматически создан Ansible

$wgDBname = "{{ wikimedia_db_name }}";
$wgDBuser = "{{ wikimedia_db_user }}";
$wgDBpassword = "{{ wikimedia_db_password }}";
$wgDBhost = "localhost";

$wgScriptPath = "/mediawiki";
$wgServer = "http://{{ ansible_fqdn }}";

$wgSecretKey = "{{ lookup('password', '/dev/null length=64 chars=ascii_letters,digits') }}";
$wgUpgradeKey = "{{ lookup('password', '/dev/null length=64 chars=ascii_letters,digits') }}";

# Дополнительные настройки
$wgEnableUploads = true;
$wgUseInstantCommons = true;
$wgLanguageCode = "ru";
?>
