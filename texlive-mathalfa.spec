# revision 26209
# category Package
# catalog-ctan /macros/latex/contrib/mathalfa
# catalog-date 2012-04-28 17:53:25 +0200
# catalog-license lppl1.3
# catalog-version 1.06
Name:		texlive-mathalfa
Version:	1.06
Release:	1
Summary:	General package for loading maths alphabets in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathalfa
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalfa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalfa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides means of loading maths alphabets (such as
are normally addressed via macros \mathcal, \mathbb, \mathfrak
and \mathscr), offering various features normally missing in
existing packages for this job.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathalfa/mathalfa.sty
%doc %{_texmfdistdir}/doc/latex/mathalfa/README
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.pdf
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.06-1
+ Revision: 804939
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.05-1
+ Revision: 787686
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.04-2
+ Revision: 753771
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.04-1
+ Revision: 718965
- texlive-mathalfa
- texlive-mathalfa
- texlive-mathalfa
- texlive-mathalfa

