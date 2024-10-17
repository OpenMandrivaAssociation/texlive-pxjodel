Name:		texlive-pxjodel
Version:	64072
Release:	2
Summary:	Help change metrics of fonts from japanese-otf
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pxjodel
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjodel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjodel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package changes the setup of the japanese-otf package so
that the TFMs for direct input are all replaced by new ones
with prefixed names; for example, nmlminr-h will be replaced by
foo--nmlminr-h, where foo is a prefix specified by the user.
This function will assist users who want to use the
japanese-otf package together with tailored TFMs of Japanese
fonts. The "jodel" part of the package name stands for
"japanese-otf deluxe". Here "deluxe" is the name of
japanese-otf's option for employing multi-weight Japanese font
families. This option is probably the most likely reason for
using japanese-otf. So pxjodel is really about japanese-otf's
"deluxe" option, hence the name. It is not related to yodel
singing, although some sense of word-play is intended.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pxjodel
%{_texmfdistdir}/fonts/vf/public/pxjodel
%{_texmfdistdir}/fonts/tfm/public/pxjodel
%doc %{_texmfdistdir}/doc/latex/pxjodel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
