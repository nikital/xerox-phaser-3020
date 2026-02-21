Name:           xerox-phaser-3020
Version:        1.0
Release:        1%{?dist}
Summary:        CUPS driver for Xerox Phaser 3020

License:        Proprietary
URL:            https://www.support.xerox.com/support/phaser-3020
# (Also in ~/Saves)
Source:         https://download.support.xerox.com/pub/drivers/3020/drivers/linux/en_GB/Xerox_Phaser_3020_Linux-Driver.tar.gz

ExclusiveArch:  x86_64 i686 armv7hl

BuildRequires:  chrpath

Requires:       cups

%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

%description
CUPS driver for Xerox Phaser 3020

%prep
%setup -c

%build
# Pre-built binaries, nothing to build

%install
# Translate source architecture directory
%ifarch x86_64
%define archdir x86_64
%endif
%ifarch i686
%define archdir i386
%endif
%ifarch armv7hl
%define archdir arm
%endif

# Strip weird RPATH
chrpath -d uld/%{archdir}/smfpnetdiscovery
chrpath -d uld/%{archdir}/pstosecps
chrpath -d uld/%{archdir}/rastertospl

# Install binaries
install -D -m 0755 uld/%{archdir}/libscmssc.so %{buildroot}%{_libdir}/libscmssc.so
install -D -m 0755 uld/%{archdir}/smfpnetdiscovery %{buildroot}/usr/lib/cups/backend/smfpnetdiscovery
install -D -m 0755 uld/%{archdir}/pstosecps %{buildroot}/usr/lib/cups/filter/pstosecps
install -D -m 0755 uld/%{archdir}/rastertospl %{buildroot}/usr/lib/cups/filter/rastertospl

# PPD files
install -d %{buildroot}%{_datadir}/cups/model/uld-xerox/
for f in uld/noarch/share/ppd/*.ppd; do
    case "$f" in
        *_fr.ppd) ;;  # Skip French PPDs
        *) install -m 0644 "$f" %{buildroot}%{_datadir}/cups/model/uld-xerox/ ;;
    esac
done

# cts files (in cms dir)
install -d %{buildroot}%{_datadir}/cups/model/uld-xerox/cms/
for f in uld/noarch/share/ppd/cms/*; do
    install -D -m 0644 "$f" %{buildroot}%{_datadir}/cups/model/uld-xerox/cms/
done

%files
%{_libdir}/libscmssc.so
/usr/lib/cups/backend/smfpnetdiscovery
/usr/lib/cups/filter/pstosecps
/usr/lib/cups/filter/rastertospl
%{_datadir}/cups/model/uld-xerox

%changelog
* Thu Jan 29 2026 Nikita Leshenko <nikita@leshenko.net>
- Initial RPM package for Fedora
