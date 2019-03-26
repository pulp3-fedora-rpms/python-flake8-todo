# Created by pyp2rpm-3.3.2
%global pypi_name flake8-todo

Name:           python-%{pypi_name}
Version:        0.7
Release:        1%{?dist}
Summary:        TODO notes checker, plugin for flake8

License:        MIT
URL:            https://github.com/schlamar/flake8-todo
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Flake8 TODO plugin Check for TODO notes.This module provides a plugin for
flake8, the Python code checker. Installation You can install or upgrade
flake8-todo with these commands:: $ pip install flake8-todo $ pip install
--upgrade flake8-todo Plugin for Flake8 --When both flake8 2.0 and flake8-todo
are installed, the plugin is available in flake8:: $ flake8 --version 2.0
(pep8: 1.4.5, mccabe:...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pycodestyle) < 3.0.0
Requires:       python3dist(pycodestyle) >= 2.0.0
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Flake8 TODO plugin Check for TODO notes.This module provides a plugin for
flake8, the Python code checker. Installation You can install or upgrade
flake8-todo with these commands:: $ pip install flake8-todo $ pip install
--upgrade flake8-todo Plugin for Flake8 --When both flake8 2.0 and flake8-todo
are installed, the plugin is available in flake8:: $ flake8 --version 2.0
(pep8: 1.4.5, mccabe:...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flake8_todo.py
%{python3_sitelib}/flake8_todo-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.7-1
- Initial package.