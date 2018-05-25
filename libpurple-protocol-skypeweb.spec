Summary:	SkypeWeb API Plugin for Pidgin/libpurple/Adium
Name:		libpurple-protocol-skypeweb
Version:	1.5
Release:	1
License:	GPL v3
Group:		Applications/Communications
Source0:	https://github.com/EionRobb/skype4pidgin/archive/%{version}.tar.gz
# Source0-md5:	8f524b4090b0d2c2fc4878477c61140f
URL:		https://github.com/EionRobb/skype4pidgin/tree/master/skypeweb
BuildRequires:	cmake >= 2.8
BuildRequires:	glib2-devel
BuildRequires:	json-glib-devel
BuildRequires:	libpurple-devel
BuildRequires:	pkgconfig
Provides:	libpurple-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a SkypeWeb Plugin for Pidgin/libpurple/Adium. It lets you view
and chat with all your Skype buddies from within Pidgin/Adium.

%prep
%setup -qn skype4pidgin-%{version}

%build
cd skypeweb
%cmake

%install
rm -rf $RPM_BUILD_ROOT

cd skypeweb
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc skypeweb/README.md
%attr(755,root,root) %{_libdir}/purple-2/libskypeweb.so
%dir %{_pixmapsdir}/pidgin/emotes/skype
%{_pixmapsdir}/pidgin/emotes/skype/theme
%{_pixmapsdir}/pidgin/protocols/*/skype.png
%{_pixmapsdir}/pidgin/protocols/*/skypeout.png
