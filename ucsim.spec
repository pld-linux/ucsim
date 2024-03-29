Summary:	Microcontrollers simulator
Summary(pl.UTF-8):	Symulator mikrokontrolerów
Name:		ucsim
Version:	0.3.1
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://mazsola.iit.uni-miskolc.hu/~drdani/embedded/s51/download/unix/%{name}-%{version}.tar.gz
# Source0-md5:	9de42afa62a2f33263a3482547aa5d96
Patch0:		%{name}-make.patch
Patch1:		%{name}-newcmdcl.patch
URL:		http://mazsola.iit.uni-miskolc.hu/~drdani/embedded/s51/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uCsim can be used to simulate microcontrollers. It supports MCS51 family. AVR
and Z80 support is under development.

%description -l pl.UTF-8
uCsim może być używany do emulacji mikrokontrolerków. Wspiera on rodzinę
MCS51. Obsługa AVR oraz Z80 jest aktualnie rozwijana.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.{html,gif,jpg}
%attr(755,root,root) %{_bindir}/*
