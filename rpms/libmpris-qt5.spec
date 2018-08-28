%global repo qtmpris

Name:           libmpris-qt5
Summary:        Qt and QML MPRIS interface and adaptor
Version:        0.1.0
Release:        1%{?dist}
License:        LGPLv2.1
URL:            https://github.com/nemomobile/qtmpris
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dbusextended-qt5)

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so.*

%files devel
%{_qt5_includedir}/MprisQt/Mpris
%{_qt5_includedir}/MprisQt/MprisQt
%{_qt5_includedir}/MprisQt/MprisPlayer
%{_qt5_includedir}/MprisQt/MprisController
%{_qt5_includedir}/MprisQt/MprisManager
%{_qt5_includedir}/MprisQt/mpris.h
%{_qt5_includedir}/MprisQt/mprisqt.h
%{_qt5_includedir}/MprisQt/mprisplayer.h
%{_qt5_includedir}/MprisQt/mpriscontroller.h
%{_qt5_includedir}/MprisQt/mprismanager.h
%{_qt5_qmldir}/org/nemomobile/mpris/%{name}-qml-plugin.so
%{_qt5_qmldir}/org/nemomobile/mpris/plugins.qmltypes
%{_qt5_qmldir}/org/nemomobile/mpris/qmldir
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Tue Aug 28 2018 mosquito <sensor.wen@gmail.com> - 0.1.0-1
- Initial package build
