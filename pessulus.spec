Summary:	Lockdown editor for GNOME
Summary(pl.UTF-8):	Edytor blokad dla GNOME
Name:		pessulus
Version:	2.16.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pessulus/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	cc6fc71e8e79a2d6ec778b10f1ca730d
URL:		http://www.gnome.org/~vuntz/pessulus/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	python-gnome-devel >= 2.16.2
%pyrequires_eq	python-modules
Requires:	python-gnome >= 2.16.2
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

%build
cp -f /usr/share/automake/config.sub .
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
