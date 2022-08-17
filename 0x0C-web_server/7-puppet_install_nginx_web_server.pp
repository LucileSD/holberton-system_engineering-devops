#Create Nginx configuratio server via puppet

file { 'html':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World\n',
}

file_line { 'redirection':
  ensure => present;
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  =>'running',
  require => Package['nginx'],
}
