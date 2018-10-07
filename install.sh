#!/bin/bash

#install recent version of lrelease
mkdir qt5
wget -q -O qt5.zip http://utils.musescore.org.s3.amazonaws.com/qt542.zip
unzip -qq qt5.zip -d qt5
export PATH="${PWD}/qt5/bin:$PATH"
lrelease -version

pip install transifex-client

cat >~/.transifexrc <<EOL
[https://www.transifex.com]
hostname = https://www.transifex.com
password = ${TRANSIFEX_PASSWORD}
token =
username = ${TRANSIFEX_USER}
EOL

pip install s3cmd

cat >~/.s3cfg <<EOL
[default]
access_key = ${S3_KEY}
bucket_location = US
cloudfront_host = cloudfront.amazonaws.com
cloudfront_resource = /2010-07-15/distribution
default_mime_type = binary/octet-stream
delete_removed = False
dry_run = False
encoding = UTF-8
encrypt = False
follow_symlinks = False
force = False
get_continue = False
gpg_command = None
gpg_decrypt = %(gpg_command)s -d --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
gpg_encrypt = %(gpg_command)s -c --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
gpg_passphrase =
guess_mime_type = True
host_base = s3.amazonaws.com
host_bucket = %(bucket)s.s3.amazonaws.com
human_readable_sizes = False
list_md5 = False
log_target_prefix =
preserve_attrs = True
progress_meter = True
proxy_host =
proxy_port = 0
recursive = False
recv_chunk = 4096
reduced_redundancy = False
secret_key = ${S3_SECRET}
send_chunk = 4096
simpledb_host = sdb.amazonaws.com
skip_existing = False
socket_timeout = 300
urlencoding_mode = normal
use_https = False
verbosity = WARNING
EOL


