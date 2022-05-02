# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message

exec {'replace-hard:
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-soft'], 
}

exec {'replace-soft':
  provider => shell,
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 40000/" /etc/security/limits.conf',  
}
