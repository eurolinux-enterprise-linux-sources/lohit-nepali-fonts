%global fontname lohit-nepali
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        2%{?dist}
Summary:        Free Nepali font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
This package provides a free Nepali truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog OFL.txt COPYRIGHT AUTHORS README ChangeLog.old

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.5.3-2
- Mass rebuild 2013-12-27

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1.1-1
- first release after lohit-devanagari split into nepali specific shapes
