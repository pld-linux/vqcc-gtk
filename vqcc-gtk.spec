# - Change Summary (temporary taken from vyqchat.spec)
# - write description pl
# - check BR, R, url
# - check .desktop file

Summary:	Real-time, text-based, serverless LAN chat program
Summary(pl):	Dzia³aj±cy w czasie rzeczywistym, tekstowy, bezserwerowy program do pogawêdek sieciowych
Name:		vqcc-gtk
Version:	0.5
Release:	0.1
License:	GPL	
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	88c2beaa96b58b380147a1d24c90349d
URL:		http://vqcc-gtk.sf.net/	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 2.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vqcc-gtk is a chat application written in C for the GTK+ toolkit, primarily
used in small LAN's. Based on quickChat/Vypress Chat (TM) for Windows
(from Vypress Research) and is licensed under the GPL.

The application supports both quickChat and Vypress Chat(TM) protocols and
hopefully is compatible enough to substitute those applications when using
Linux, FreeBSD or any other *NIX desktop. You need no server to run, however
it is not possible to communicate outside your LAN (or subnet).


%description -l pl

%prep
%setup -q

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
%doc ChangeLog README COPYING
%_bindir/*
%_datadir/pixmaps/*
%_datadir/applications/*
