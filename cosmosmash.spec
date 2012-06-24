Summary: 	Cosmosmash.
Name:		cosmosmash
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
URL:		http://sarrazip.com/dev/cosmosmash.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	gengameng-devel >= 4.1
Requires: 	gengameng >= 4.1
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Cosmosmash is a game where you control a base that must
destroy rocks before they hit the ground, or you lose points.
You must also prevent "spinners" from touching the ground,
or your base will explode. This game is a clone of the 1981
Astrosmash video game by Mattel Electronics.
 
%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomedesktopentrydir=%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING THANKS NEWS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_applnkdir}/Games/Arcade/%{name}.desktop
%{_mandir}/man6/%{name}.6*
