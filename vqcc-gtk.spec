Summary:	Chat application for GTK+ based on quickChat/Vypress Chat
Summary(pl.UTF-8):	Program do pogawędek internetowych dla GTK+ oparty na quickChat/Vypress Chat
Name:		vqcc-gtk
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/vqcc-gtk/%{name}-%{version}.tar.gz
# Source0-md5:	88c2beaa96b58b380147a1d24c90349d
Patch0:		%{name}-desktop.patch
URL:		http://vqcc-gtk.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vqcc-gtk is a chat application written in C for the GTK+ toolkit,
primarily used in small LANs. Based on quickChat/Vypress Chat (TM) for
Windows (from Vypress Research) and is licensed under the GPL.

The application supports both quickChat and Vypress Chat(TM) protocols
and hopefully is compatible enough to substitute those applications
when using Linux, FreeBSD or any other *NIX desktop. You need no
server to run, however it is not possible to communicate outside your
LAN (or subnet).

%description -l pl.UTF-8
Vqcc-gtk jest programem do pogawędek internetowych dla GTK+,
pierwotnie używany w małych sieciach LAN. Oparto go na
quickChat/Vypress Chat dla Windowsa. Jest licencjonowany na GNU GPL.

Aplikacja wspiera zarówno protokół quickChat jak i Vypress Chat.
Możliwe, że zastąpi w niedalekiej przyszłości te aplikacje podczas
używania systemów uniksowych. Do jego uruchomienia nie jest potrzebny
serwer, jakkolwiek nie jest możliwe komunikowanie się poza siecią LAN.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
