# Generated from chronic-0.3.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	chronic

Summary:	Natural language date/time parsing
Name:		rubygem-%{rbname}

Version:	0.3.0
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://github.com/mojombo/chronic
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Chronic is a natural language date/time parser written in pure Ruby.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(benchmark|test)'

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic/numerizer
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic/numerizer/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic/repeaters
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/chronic/repeaters/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.md
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/benchmark
%{ruby_gemdir}/gems/%{rbname}-%{version}/benchmark/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb


%changelog
* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1
+ Revision: 643536
- regenerate spec with gem2rpm5
- new release: 0.3.0

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.3-2mdv2011.0
+ Revision: 579738
- rebuild for new automatic provides/requires
- don't ship the gem archive with package

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 500303
- import rubygem-chronic


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.2.3-1
- initial release
