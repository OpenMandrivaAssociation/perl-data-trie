%define module	data-trie
%define Module	Data-Trie
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An implementation of a letter trie
License:	GPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/H/HA/HAMMOND/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
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
%setup -q -n %{Module}-%{version}

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

