Summary:	Microcontrollers simulator
Summary(pl.UTF-8):	Symulator mikrokontrolerów
Name:		ucsim
Version:	0.8.6
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Emulators
#Source0Download: https://github.com/danieldrotos/ucsim/releases
Source0:	https://github.com/danieldrotos/ucsim/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9c907cb140c2482d542dadb5d36436ff
URL:		https://www.ucsim.hu/
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ncurses-ext-devel >= 5.2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uCsim can be used to simulate microcontrollers. It supports Intel
MCS51 family, 8080, 8085, XA, Z80, Rabbit, SM83, TLCS90, ST7, STM8,
PDK, MC6800, M68HC08, MC6809, M68HC11, M68HC12, MOS6502, PicoBlaze,
F8, p1516/p2223 and some AVR processors.

%description -l pl.UTF-8
uCsim służy do symulowania mikrokontrolerów. Obsługuje rodzinę
procesorów Intel MCS51, 8080, 8085, XA, Z80, Rabbit, SM83, TLCS90,
ST7, STM8, PDK, MC6800, M68HC08, MC6809, M68HC11, M68HC12, MOS6502,
PicoBlaze, F8, p1516/p2223 i niektóre procesory AVR.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%configure \
	STRIP=/bin/true
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src/apps/serio.src local_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C src/apps/ucsim.src local_install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ucsim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md docs/{stm8,*.html,*.jpg,*.png,*.svg,*.txt}
%attr(755,root,root) %{_bindir}/s51
%attr(755,root,root) %{_bindir}/serialview
%attr(755,root,root) %{_bindir}/ucsim
%attr(755,root,root) %{_bindir}/ucsim_*
%{_mandir}/man1/ucsim.1*
%{_mandir}/man1/serialview.1*
