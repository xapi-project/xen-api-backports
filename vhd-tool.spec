# -*- rpm-spec -*-

Summary: command-line tools for manipulating and streaming .vhd format files
Name:    vhd-tool
Version: 0.7.2
Release: 1
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: https://github.com/xapi-project/vhd-tool/archive/%{version}/vhd-tool-%{version}.tar.gz
Source1: vhd-tool-sparse_dd-conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml ocaml-findlib ocaml-camlp4-devel ocaml-ocamldoc
BuildRequires: ocaml-ocplib-endian-devel
BuildRequires: ocaml-xcp-idl-devel ocaml-vhd-devel ocaml-obuild
BuildRequires: ocaml-nbd-devel ocaml-cstruct-devel ocaml-lwt-devel
BuildRequires: ocaml-ounit-devel ocaml-rpc-devel ocaml-ssl-devel ocaml-stdext-devel
BuildRequires: ocaml-tapctl-devel
BuildRequires: ocaml-xenstore-devel git cmdliner-devel ocaml-oclock-devel
BuildRequires: ocaml-xenstore-clients-devel message-switch-devel
BuildRequires: openssl openssl-devel
BuildRequires: xmlm-devel ocaml-uuidm-devel ocaml-uri-devel ocaml-type-conv ocaml-re-devel forkexecd-devel ocaml-fd-send-recv-devel ocaml-cohttp-devel

%description
Simple command-line tools for manipulating and streaming .vhd format file.

%prep 
%setup -q
cp %{SOURCE1} vhd-tool-sparse_dd-conf


%build
./configure --bindir %{buildroot}/opt/xensource/libexec --libexecdir %{buildroot}/opt/xensource/libexec --etcdir %{buildroot}/etc
make

%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/xapi
mkdir -p %{buildroot}/etc
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/xensource/libexec/vhd-tool
/etc/sparse_dd.conf
/opt/xensource/libexec/sparse_dd

%changelog
* Wed Nov 6 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.4-2
- Compiled against updated ocaml-vhd 0.6.4

* Tue Nov 5 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.4-1
- Update to 0.6.4
- Fixes for opening VHD files RW for vhd-tool serve

* Fri Nov 1 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.3-1
- Update to 0.6.3
- Fixes for opening RO VHD files

* Thu Oct 31 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.2-1
- Update to 0.6.2
- Fixes for 32-bit machines

* Wed Oct 30 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.1-1
- Update to 0.6.1
- Get from xapi-project Github instead of djs55

* Thu Oct 24 2013 Si Beaumont <simon.beaumont@citrix.com> - 0.6.0-2
- Backport package (install to /opt/xensource/libexec/)

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Update to 0.6.0

* Fri Sep 27 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.1-1
- Update to 0.5.1

* Mon Sep 23 2013 David Scott <dave.scott@eu.citrix.com> - 0.5.0-1
- Initial package
