Summary:	Microcontrollers simulator.
Summary(pl):	Symulator mikrokontrolerów.
Name:		ucsim
Version:	0.2.38
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://mazsola.iit.uni-miskolc.hu/~drdani/embedded/s51/download/unix/%{name}-%{version}.tar.gz
Patch0:		ucsim-make.patch
URL:		http://mazsola.iit.uni-miskolc.hu/~drdani/embedded/s51/
BuildRequires:	mawk
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
uCsim can be used to simulate microcontrollers. It supports MCS51 family. AVR
and Z80 support is under development.          

%description -l pl
uCsim mo¿e byæ u¿ywany do emulacji mikrokontrolerków. Wspiera on rodzinê
MCS51. Obs³uga AVR oraz Z80 jest aktualnie rozwijana.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples
%attr(755,root,root) %{_bindir}/*
