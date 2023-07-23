# Setup server for serving web_static page

exec {'configure_server':
  provider => shell,
  command => 'git clone https://github.com/Juliusmwash/AirBnb_clone_v2.git ; sudo mv AirBnb_clone_v2/0-setup_web_static.sh . ; sudo ./0-setup_web_static.sh,
  path => '/usr/bin:/bin',
}
