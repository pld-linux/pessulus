Summary:	Lockdown editor for GNOME
Summary(pl.UTF-8):	Edytor blokad dla GNOME
Name:		pessulus
Version:	2.16.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pessulus/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	b423065aeddb6ed416e6eafa36a4aab9
URL:		http://www.gnome.org/~vuntz/pessulus/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.36.2
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.22.0
BuildRequires:	python-pygtk >= 2:2.12.0
%pyrequires_eq	python-modules
Requires:	python-gnome >= 2.22.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pessulus is a lockdown editor for GNOME, written in Python. Pessulus
enables administrators to set mandatory settings in GConf. The users
can not change these settings. Use of pessulus can be useful on
computers that are open to use by everyone, e.g. in an internet cafe.

%description -l pl.UTF-8
Pessulus jest napisanym w pythonie edytorem blokad dla GNOME.
Umożliwia administratorowi wprowadzenie obowiązkowych ustawień w
GConfie, które nie będą mogły być zmienione przez użytkownika. Użycie
pessulusa może być przydatne na ogólnodostępnych komputerach, np. w
kawiarenkach internetowych.

%prep
%setup -q

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/Pessulus/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/Pessulus
%{py_sitedir}/Pessulus/*.py[co]
%{_datadir}/pessulus
%{_desktopdir}/*.desktop
