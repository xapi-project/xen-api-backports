%global debug_package %{nil}

Name:           ocaml-nbd
Version:        1.0.3
Release:        1
Summary:        Pure OCaml implementation of the Network Block Device protocol
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/djs55/nbd
Source0:        https://github.com/djs55/nbd/archive/%{version}/nbd-%{version}.tar.gz
Patch0:         nbd-dont-install-nbd-tool.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-cstruct-devel ocaml-lwt-devel ocaml-camlp4-devel ocaml-camlp4 cmdliner-devel ocaml-ocplib-endian-devel ocaml-rpc-devel ocaml-type-conv
Requires:       ocaml ocaml-findlib

%description
An implementation of the Network Block Device protocol for both
regular Unix and Lwt in OCaml. This library allows applications to
access remote block devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n nbd-%{version}
%patch0 -p1 -b ~nbd-dont-install-nbd-tool.patch

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{_libdir}/ocaml/nbd
%exclude %{_libdir}/ocaml/nbd/*.a
%exclude %{_libdir}/ocaml/nbd/*.cmx
%exclude %{_libdir}/ocaml/nbd/*.cmxa
%exclude %{_libdir}/ocaml/nbd/*.ml
%exclude %{_libdir}/ocaml/nbd/*.mli

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/nbd/META
%{_libdir}/ocaml/nbd/*.a
%{_libdir}/ocaml/nbd/*.cmx
%{_libdir}/ocaml/nbd/*.cmxa
%{_libdir}/ocaml/nbd/*.mli

%changelog
* Mon Feb 27 2017 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 17 2014 John Else <john.else@citrix.com> 1.0.2-1
- Update to 1.0.2
- Switch build to OASIS
- Fix incomplete pattern matches
- Result type is now a polymorphic variant

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

