#!/bin/bash

set -e

rpmdev-setuptree

cp *.spec ~/rpmbuild/SPECS/
# Download sources
spectool -g -R ~/rpmbuild/SPECS/*.spec
# Build RPM
rpmbuild --target x86_64 -bb ~/rpmbuild/SPECS/*.spec
rpmbuild --target i686 -bb ~/rpmbuild/SPECS/*.spec
rpmbuild --target armv7hl -bb ~/rpmbuild/SPECS/*.spec

cp -r ~/rpmbuild/RPMS/* out/
tar -czf out/rpms.tar.gz -C out/ x86_64 i686 armv7hl
