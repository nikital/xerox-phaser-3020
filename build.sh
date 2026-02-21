#!/bin/bash

set -e

rm -rf out/RPMS
rm -f out/rpms.tar.gz

# Download sources
spectool --define "_topdir %(pwd)/out" -g -R *.spec
# Build RPM
rpmbuild --define "_topdir %(pwd)/out" --target x86_64 -ba *.spec
rpmbuild --define "_topdir %(pwd)/out" --target i686 -ba *.spec
rpmbuild --define "_topdir %(pwd)/out" --target armv7hl -ba *.spec

tar -czf out/rpms.tar.gz -C out/RPMS .
