Summary:	Lockdown editor for GNOME
Summary(pl):	Edytor blokad dla GNOME
Name:		pessulus
Version:	0.10.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pessulus/0.10/%{name}-%{version}.tar.gz
# Source0-md5:	dad5445c56ad67af9e1c4b7d494667e2
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/~vuntz/pessulus/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	automake
BuildRequires:	intltool >= 0.35
BuildRequires:	python-gnome-devel >= 2.15.2
%pyrequires_eq	python-modules
Requires:	python-gnome >= 2.15.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pessulus is a lockdown editor for GNOME, written in python.
Pessulus enables administrators to set mandatory settings in GConf. The
users can not change these settings.
Use of pessulus can be useful on computers that are open to use by
everyone, e.g. in an internet cafe.

%description -l pl
Pessulus jest napisanym w pythonie edytorem blokad dla GNOME.
Umo¿liwia administratorowi wprowadzenie obowi±zkowych ustawieñ w GConf, 
które nie bêd± mog³y byæ zmienione przez u¿ytkownika.
U¿ycie pessulusa mo¿e byæ przydatne na ogólnodostêpnych komputerach, np. 
w kawiarenkach internetowych.

%prep
%setup -q
%patch0 -p1

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
