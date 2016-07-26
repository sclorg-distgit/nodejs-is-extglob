%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name is-extglob

Summary:       Returns true if a string has an extglob
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.0
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-extglob
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Returns true if a string has an extglob.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable scl macros

* Tue Dec 15 2015 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Initial package
