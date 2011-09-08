Summary: Fake Oracle client packagee
Name: oracle-fake-client
Version: 11.1
Release: 1
Source: oracle-fake-client-%{version}.tar.bz2
License: LGPL
Group: Clients
URL: https://github.com/pvanek/oracle-fake-client
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: libclntsh.so.11.1

%description
This package contains fake oracle client. It does not mean you can run any SW with it. You
need to download at least instant client from Oracle website. Yes, it's closed source
but free-as-a-beer.
http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html


%prep 
%setup -q -n "oracle-fake-client-%{version}"


%build
cmake -DCMAKE_VERBOSE_MAKEFILE=TRUE -DCMAKE_INSTALL_PREFIX="%{_prefix}" .
make

%install
%__make install DESTDIR="%buildroot"


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}


%files
%defattr(-,root,root)
%_libdir/libclntsh.*
%doc AUTHORS COPYING README


%changelog
* Thu Sep 8 2011 Petr Vanek <petr@scribus.info> - 11.1
- initial spec file revision

