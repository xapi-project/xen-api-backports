Name:           ocaml-bytes
Version:        1.4
Release:        1%{?extrarelease}
Summary:        Bytes module for ocaml <= 4.02
License:        ISC
Group:          Development/Other
URL:            https://github.com/chambart/ocaml-bytes
Source0:        https://github.com/chambart/ocaml-bytes/archive/ocaml-bytes.1.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc ocaml-re-devel ocaml-compiler-libs
Requires:       ocaml ocaml-findlib

%description
Bytes module for ocaml <= 4.02

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}.%{version}

%build
./configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml/bytes
make install LIBDIR=%{buildroot}/%{_libdir}/ocaml/bytes

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md
%{_libdir}/ocaml/bytes/*

%changelog
* Thu May 26 2016 Phus Lu <phus.lu@citrix.com>
- Initial package

