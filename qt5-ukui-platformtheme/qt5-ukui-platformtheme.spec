Name:           qt5-ukui-platformtheme
Version:        master
Release:        1%{?dist}
Summary:        Qt5 QPA platform theme of UKUI


License:         LGPL-3.0 License
URL:            https://github.com/ukui/qt5-ukui-platformtheme
Source0:        https://github.com/ukui/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  glib2-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qttools-devel
BuildRequires: gsettings-qt-devel
Requires: qt5-ukui-platformtheme-styles
Requires: qt5-ukui-platformtheme-styles-libs



%description
 qt5-ukui-platformtheme is official platform theme of UKUI desktop
 environment. It also provides the common metadatas for ukui-styles
 and platform theme using. The library provided many convenient API
 for changing a qt widgets style, such as buttons color, tabwidget
 animation, etc.
 .
 This package provides a qt5 qpa platform theme plugin.


%package styles
Summary: QStyle plugins provided by ukui
Requires: qt5-ukui-platformtheme-styles-libs
%description styles
 qt5-ukui-platformtheme is official platform theme of UKUI desktop
 environment. It also provides the common metadatas for ukui-styles
 and platform theme using. The library provided many convenient API
 for changing a qt widgets style, such as buttons color, tabwidget
 animation, etc.
 .
 This package provides several qstyle plugins which as default
 styles in ukui. For now, fusion is the base style of ukui-styles.

%package styles-libs
Summary: UKUI platform theme and styles' shared library

%description styles-libs
 qt5-ukui-platformtheme is official platform theme of UKUI desktop
 environment. It also provides the common metadatas for ukui-styles
 and platform theme using. The library provided many convenient API
 for changing a qt widgets style, such as buttons color, tabwidget
 animation, etc.

%package styles-devel
Summary: Development files of qt5-ukui-platformtheme-styles-libs
Requires: qt5-ukui-platformtheme-styles-libs

%description styles-devel
 qt5-ukui-platformtheme is official platform theme of UKUI desktop
 environment. It also provides the common metadatas for ukui-styles
 and platform theme using. The library provided many convenient API
 for changing a qt widgets style, such as buttons color, tabwidget
 animation, etc.
 .
 This package provides the development files of qt5-ukui-platformtheme-styles-libs.


%prep

%setup -q
 
%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..
%{make_build}
pushd 
%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd

%files
%doc debian/changelog  debian/copyright
%{_libdir}/qt5/plugins/platformthemes/libqt5-ukui-platformtheme.so

%files styles-devel
%{_libdir}/pkgconfig/qt5-ukui.pc


%files styles-libs
%{_libdir}/libqt5-ukui-style.so
%{_libdir}/libqt5-ukui-style.so.1
%{_libdir}/libqt5-ukui-style.so.1.0
%{_libdir}/libqt5-ukui-style.so.1.0.0
%{_datadir}/glib-2.0/schemas/org.ukui.style.gschema.xml


%files styles
%{_libdir}/qt5/plugins/styles/libqt5-style-ukui.so
%{_libdir}/qt5/plugins/styles/libukui-proxy-style.so
