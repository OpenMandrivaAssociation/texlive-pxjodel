%global tl_name pxjodel
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3a
Release:	%{tl_revision}.1
Summary:	Help change metrics of fonts from japanese-otf
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxjodel
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjodel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjodel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package changes the setup of the japanese-otf package so that the
TFMs for direct input are all replaced by new ones with prefixed names;
for example, nmlminr-h will be replaced by foo--nmlminr-h, where foo is
a prefix specified by the user. This function will assist users who want
to use the japanese-otf package together with tailored TFMs of Japanese
fonts. The "jodel" part of the package name stands for "japanese-otf
deluxe". Here "deluxe" is the name of japanese-otf's option for
employing multi-weight Japanese font families. This option is probably
the most likely reason for using japanese-otf. So pxjodel is really
about japanese-otf's "deluxe" option, hence the name. It is not related
to yodel singing, although some sense of word-play is intended.

