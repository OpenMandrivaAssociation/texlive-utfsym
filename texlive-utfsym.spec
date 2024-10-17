Name:		texlive-utfsym
Version:	63076
Release:	2
Summary:	Provides various Unicode symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/utfsym
License:	cc0
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utfsym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utfsym.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides various symbols from the Unicode in order
to be able to use them originally in a school setting such as
on worksheets.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/utfsym
%doc %{_texmfdistdir}/doc/latex/utfsym

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
