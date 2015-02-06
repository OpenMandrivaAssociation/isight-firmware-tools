%define Werror_cflags   %{nil}


Summary:	Firmware extraction tools for Apple Built-in iSight camera
Name:		isight-firmware-tools
Version:	1.6
Release:	3
License:	GPLv2+
Group:		System/Base
URL:		http://launchpad.net/isight-firmware-tools/
Source0:	http://launchpad.net/isight-firmware-tools/main/1.6/+download/%{name}-%{version}.tar.gz
Patch0:		isight-firmware-tools-ift-load-path.patch
Requires:	udev
BuildRequires:	gettext
BuildRequires:	glib2-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libusb-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool

%description
iSight Firmware Tools provide tools to manipulate firmware for Built-in iSight
cameras found on Apple machines since iMac G5 (November 2005).

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_infodir}/dir

# Use doc instead.
rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%config %{_sysconfdir}/udev/rules.d/isight.rules
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc HOWTO
%doc NEWS
%doc README
%{_bindir}/ift-export
%{_bindir}/ift-extract
%{_infodir}/ift-export.info.*
%{_infodir}/ift-extract.info.*
%{_mandir}/man1/ift-export.1.*
%{_mandir}/man1/ift-extract.1.*
/lib/udev/ift-load


%changelog
* Thu Jun 14 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6-2
+ Revision: 805551
- Drop some legacy junk

* Sun Dec 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.6-1
+ Revision: 743631
- imported package isight-firmware-tools

