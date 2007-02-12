Summary:	Cosmosmash game
Summary(pl.UTF-8):   Gra Cosmosmash
Name:		cosmosmash
Version:	1.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
# Source0-md5:	85f7ea8d961a4c407fb99f07dee006c1
URL:		http://sarrazip.com/dev/cosmosmash.html
BuildRequires:	flatzebra-devel >= 0.1.1
Requires:	flatzebra >= 0.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cosmosmash is a game where you control a base that must destroy rocks
before they hit the ground, or you lose points. You must also prevent
"spinners" from touching the ground, or your base will explode. This
game is a clone of the 1981 Astrosmash video game by Mattel
Electronics.

%description -l pl.UTF-8
Cosmosmash to gra, w której steruje się bazą, która musi zniszczyć
głazy zanim uderzą w ziemię - w przeciwnym wypadku traci się punkty.
Trzeba także zapobiec dotknięciu ziemi przez obracające się obiekty -
w przeciwnym wypadku baza eksploduje. Cosmosmash jest klonem gry wideo
Astrosmash, stworzonej w 1981 roku przez Mattel Electronics.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/sounds/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/%{name}.6*
