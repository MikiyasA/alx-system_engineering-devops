# config the ssh file using puppet
exec { 'echo':
    path    => 'usr/bin:/bin',
    command => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
    returns => [0, 1],
}