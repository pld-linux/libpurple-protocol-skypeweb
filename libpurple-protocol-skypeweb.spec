Summary:	SkypeWeb API Plugin for Pidgin/libpurple/Adium
Name:		libpurple-protocol-skypeweb
Version:	1.7
Release:	5
License:	GPL v3
Group:		Applications/Communications
Source0:	https://github.com/EionRobb/skype4pidgin/archive/%{version}.tar.gz
# Source0-md5:	6af9359c55f4644fc8848389df582848
Patch0:		login.patch
Patch1:		bitlbee_img_url.patch
Patch2:		xhtml.patch
Patch3:		video_attachemnt.patch
URL:		https://github.com/EionRobb/skype4pidgin/tree/master/skypeweb
BuildRequires:	cmake >= 2.8
BuildRequires:	glib2-devel
BuildRequires:	json-glib-devel
BuildRequires:	libpurple-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
Provides:	libpurple-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a SkypeWeb Plugin for Pidgin/libpurple/Adium. It lets you view
and chat with all your Skype buddies from within Pidgin/Adium.

%prep
%setup -qn skype4pidgin-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

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
