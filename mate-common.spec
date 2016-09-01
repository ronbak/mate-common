Name:           mate-common
Summary:        mate common build files
Version:        1.15.0
Release:        1%{?dist}
License:        GPLv3+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.15/mate-common-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  automake autoconf
Requires:       automake 
Requires:       autoconf 
Requires:       gettext 
Requires:       intltool 
Requires:       libtool 
Requires:       glib2-devel 
Requires:       gtk-doc 
Requires:       itstool 
Requires:       yelp-tools

%description
binaries for building all MATE desktop sub components

%prep
%setup -q

%build
%configure

make %{?_smp_mflags} V=1


%install
%{make_install}


%files
%{_bindir}/mate-*
%{_datadir}/aclocal/mate-*.m4
%{_datadir}/mate-common
%{_mandir}/man1/*

%changelog
* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Tue Apr 05 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Wed Oct 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- bump version

* Wed Oct 21 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-0
- update to 1.11.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Tue Jan 27 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release

* Mon Jan 12 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release

* Sat Jul 12 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0.1
- update to 1.9.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Feb 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90 release

* Sun Feb 09 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3

* Sat Jan 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-1
- update to 1.7.2 release

* Fri Dec 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.1-2
- Add yelp-tools to hard requires

* Sat Oct 05 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Mon Sep 09 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-1
- update to 1.6.2 release
- remove %%defattr(-,root,root,-)
- use modern make install macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.6.1-1
- Update to 1.6.1 release

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.6.0-1
- Update to 1.6.0 final release

* Mon Mar 18 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.2-1
- Update to latest upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.1-1
- Update to latest upstream release.

* Mon Jan 14 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.0-2
- Add patch for latest autoconf and automake on rawhide

* Thu Oct 11 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.0-1
- New upstream release 1.5

* Thu Aug 2 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-8
- Re add requires with proper required packages for dependent packages.

* Thu Aug 2 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-7
- Remove requires field as it is not necessary.

* Tue Jul 24 2012 Dan Mashal <dan.mashal@gmail.com> 1.4.0-6
- Update requires/buildrequires field.

* Mon Jul 16 2012 Dan Mashal <dan.mashal@gmail.com> 1.4.0-5
- Update license, description and requires field.

* Mon Jul 16 2012 Dan Mashal <dan.mashal@gmail.com> 1.4.0-4
- Clean up requirements fields

* Sat Jul 14 2012 Dan Mashal <dan.mashal@gmail.com> 1.4.0-3
- incorporate Rex's changes, clean up spec file.

* Fri Jul 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-2
- omit Group: tag
- fix URL, Source0
- use %%configure macro
- BuildArch: noarch

* Thu Jul 12 2012 Dan Mashal <dan.mashal@gmail.com> 1.4.0-1
- Initial build
