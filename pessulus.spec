Summary:	Lockdown editor for GNOME
Summary(pl.UTF-8):	Edytor blokad dla GNOME
Name:		pessulus
Version:	2.30.4
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pessulus/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	3a66250af602b8baf378c9cf28b5b8ce
URL:		http://live.gnome.org/Pessulus
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-desktop-devel >= 2.24.0
BuildRequires:	python-gnome-devel >= 2.22.0
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	python-gnome-desktop >= 2.24.0
Requires:	python-gnome-gconf >= 2.22.0
%pyrequires_eq	python-modules
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

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not supported
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{bal,en@shaw}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pessulus
%dir %{py_sitescriptdir}/Pessulus
%{py_sitescriptdir}/Pessulus/*.py[co]
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/pessulus
%{_desktopdir}/*.desktop
