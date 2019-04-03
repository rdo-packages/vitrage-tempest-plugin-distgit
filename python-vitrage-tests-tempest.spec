# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global service vitrage
%global plugin vitrage-tempest-plugin
%global module vitrage_tempest_plugin
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the Vitrage project. \
Additionally it provides a plugin to automatically load these \
tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    2.2.1
Release:    1%{?dist}
Summary:    Tempest Integration of Vitrage Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python%{pyver}-%{service}-tests-tempest}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools

Obsoletes:   python-vitrage-tests < 2.2.0

Requires:   python%{pyver}-tempest >= 1:18.0.0
Requires:   python%{pyver}-pbr >= 3.1.1
Requires:   python%{pyver}-oslo-config >= 2:5.2.0
Requires:   python%{pyver}-oslo-log >= 3.36.0
Requires:   python%{pyver}-oslo-serialization >= 2.18.0
Requires:   python%{pyver}-keystoneclient
Requires:   python%{pyver}-heatclient
Requires:   python%{pyver}-ceilometerclient
Requires:   python%{pyver}-cinderclient
Requires:   python%{pyver}-neutronclient
Requires:   python%{pyver}-novaclient
Requires:   python%{pyver}-mistralclient
Requires:   python%{pyver}-glanceclient
Requires:   python%{pyver}-aodhclient
Requires:   python%{pyver}-six => 1.10.0
Requires:   python%{pyver}-dateutil
Requires:   python%{pyver}-testtools
Requires:   python%{pyver}-oslotest
Requires:   python%{pyver}-vitrageclient
Requires:   python%{pyver}-vitrage
Requires:   python%{pyver}-gnocchiclient >= 3.3.1
Requires:   python%{pyver}-oslo-utils >= 3.36.0

# Handle python2 exception
%if %{pyver} == 2
Requires:   python-networkx
Requires:   PyYAML
%else
Requires:   python%{pyver}-networkx
Requires:   python%{pyver}-PyYAML
%endif


%description -n python%{pyver}-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{service}-tests-tempest-doc
Summary:        python-%{service}-tests-tempest documentation

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme

%description -n python-%{service}-tests-tempest-doc
It contains the documentation for the vitrage tempest plugin.
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{pyver_build}

# Generate Docs
%if 0%{?with_doc}
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}

%files -n python%{pyver}-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{service}-tests-tempest-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Apr 03 2019 RDO <dev@lists.rdoproject.org> 2.2.1-1
- Update to 2.2.1

