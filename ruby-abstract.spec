%define pkgname abstract
Summary:	Allows you to define an abstract method in Ruby
Name:		ruby-%{pkgname}
Version:	1.0.0
Release:	2
License:	GPL v2 or Ruby
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	ea26d93f0a47a530631da430c9e9b7e5
URL:		http://rubyforge.org/projects/abstract
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small library that allows you to define an abstract method in Ruby.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
ruby test/test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt ChangeLog
%{ruby_vendorlibdir}/abstract.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if 0
%files doc
%defattr(644,root,root,755)
%endif
