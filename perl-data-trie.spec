%define upstream_name	 data-trie
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	An implementation of a letter trie
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAMMOND/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements a letter trie data structure. This is a linked set of
nodes representing a set of words. Starting from the root, each letter of an
included word is a daughter node of the trie. Hence, if a word is in the trie,
there will be a path from root to leaf for that word. If a word is not in the
trie, there will be no such path.

This structure allows for a relatively compact representation of a set of
words. This particular implementation allows each word to be stored alone or
with some associated data item.

Note that the remove() method does not prune nodes and thus a Trie can only
grow in size.

%prep
%setup -q -n Data-Trie-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Data
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 403089
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-5mdv2009.0
+ Revision: 256483
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.01-3mdv2008.1
+ Revision: 135831
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdv2008.0
+ Revision: 86330
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2007.0
- Rebuild

* Tue Oct 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdk
- first mdk release

