
%define		qtver	4.6.0
%define		origname	YDPDict

Summary:	DE 4.X plasma interface for YDP Collins and Langenscheidt dictionaries
Name:		kde4-kdeplasma-addons-YDPDict
Version:	0.7.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kde-look.org/CONTENT/content-files/107700-%{origname}_%{version}.tar.gz
# Source0-md5:	a9b7f0b1ec13a7fb3889ae065fa8c7d7
URL:		http://www.kde-look.org/content/show.php/YDPDict?content=107700
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libydpdict-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DE 4.X plasma interface for YDP Collins and Langenscheidt dictionaries
on Linux platform.
- Collins polish/english and english/polish dictionary
- Langenscheidt polish/german and german/polish dictionary

%prep
%setup -q -n %{origname}_%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang plasma_applet_ydpdict --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f plasma_applet_ydpdict.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_ydpdict.so
%{_datadir}/kde4/services/plasma-applet-ydpdict.desktop
