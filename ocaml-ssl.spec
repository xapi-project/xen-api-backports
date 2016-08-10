Name:           ocaml-ssl
Version:        0.5.2
Release:        1%{?extrarelease}
Summary:        Use OpenSSL from OCaml
License:        LGPL
Group:          Development/Other
URL:            http://downloads.sourceforge.net/project/savonet/ocaml-ssl
Source0:        http://downloads.sourceforge.net/project/savonet/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib openssl-xs-devel openssl-wrapper autoconf automake ocaml-bytes-devel
Requires:       ocaml ocaml-findlib openssl-xs openssl-wrapper

%description
Use OpenSSL from OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./bootstrap
./configure
# --disable-ldconf
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc CHANGES COPYING README.md
%{_libdir}/ocaml/ssl/*
%{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_stubs.so.owner

%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so.owner

%changelog
* Tue May 24 2016 Phus Lu <phus.lu@citrix.com> - 0.5.2-1
- Upgrade to ocaml-ssl-0.5.2 for TLSv1.2

* Mon Dec 14 2015 Si Beaumont <simon.beaumont@citrix.com> - 0.4.6-2
- Recompile against openssl-xs

* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

