%define upstream_name    Test-Portability-Files
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check file names portability
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module is used to check the portability across operating systems of
the names of the files present in the distribution of a module. The tests
use the advices given in the perlport/"Files and Filesystems" manpage. The
author of a distribution can select which tests to execute.

To use this module, simply copy the code from the synopsis in a test file
named _t/portfs.t_ for example, and add it to your _MANIFEST_. You can
delete the call to 'options()' to enable only most common tests.

By default, not all tests are enabled because some are judged too
cumbersome to be practical, especially since some of the most limited
platforms (like MS-DOS) seem to be no longer supported. Here are the
default options:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654315
- rebuild for updated spec-helper

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 527962
- import perl-Test-Portability-Files


* Sat Mar 27 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
