%define upstream_name	 data-trie
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	An implementation of a letter trie
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAMMOND/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Data
%{_mandir}/*/*
