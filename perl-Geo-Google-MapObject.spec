%define upstream_name    Geo-Google-MapObject
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Managing the server side of Google Maps API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::Template::Pluggable)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Math::Trig)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::JSON)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Differences)
BuildArch:	noarch

%description
This module is intended to provide a server side solution to working with
the Google Maps API. In particular an object of this class encapsulates a
"map" object that provides support for the static maps API, the javascript
maps API, AJAX calls and non-javascript fallback data; but without making
many assumptions about the surrounding framework. We do assume that a
template framework with support for a "dot" notation is being used, for
example the HTML::Template::Pluggable manpage. An important commitment of
the module is support for graceful and consistent fallback to a functional
non-javascript web page.

The javascript and static Google map APIs do not behave in quite the same
way when zoom and center are not specified. Specifically it works quite
well with the static maps (the
http://code.google.com/apis/maps/documentation/staticmaps/#ImplicitPosition
ing manpage) but not so well with the javascript API. To compensate for
this the module gives a choice between: specifying the center and zoom
levels; allowing the APIs and client side code to do whatever they think
best; using a built in algorithm to calculate a sensible zoom and center;
and finally supplying ones own algorithm to calculate a sensible zoom and
center.

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
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 658176
- add br
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 624929
- import perl-Geo-Google-MapObject

