%define upstream_name    Test-Portability-Files
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Check file names portability
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


