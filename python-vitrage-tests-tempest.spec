%global service vitrage
%global plugin vitrage-tempest-plugin
%global module vitrage_tempest_plugin
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
# Disabling python3 subpackage as python3-vitrage is not available.
# Once available, we will enable it.
%global with_python3 0
%endif

%global common_desc \
This package contains Tempest tests to cover the Vitrage project. \
Additionally it provides a plugin to automatically load these \
tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Vitrage Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Obsoletes:   python-vitrage-tests < 2.2.0

Requires:   python2-tempest >= 1:18.0.0
Requires:   python2-pbr >= 3.1.1
Requires:   python2-oslo-config >= 2:5.2.0
Requires:   python2-oslo-log >= 3.36.0
Requires:   python2-oslo-serialization >= 2.18.0
Requires:   python2-keystoneclient
Requires:   python2-heatclient
Requires:   python2-ceilometerclient
Requires:   python2-cinderclient
Requires:   python2-neutronclient
Requires:   python2-novaclient
Requires:   python2-mistralclient
Requires:   python2-glanceclient
Requires:   python2-aodhclient
Requires:   python2-six => 1.10.0
Requires:   python2-dateutil
Requires:   python2-testtools
Requires:   python2-oslotest
%if 0%{?fedora}
Requires:   python2-networkx
%else
Requires:   python-networkx
#TODO(chandankumar): python2 and python3 subpackages needs to be added
Requires:   python-vitrage
%endif


%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-pbr >= 3.1.1
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-keystoneclient
Requires:   python3-heatclient
Requires:   python3-ceilometerclient
Requires:   python3-cinderclient
Requires:   python3-neutronclient
Requires:   python3-novaclient
Requires:   python3-mistralclient
Requires:   python3-glanceclient
Requires:   python3-aodhclient
Requires:   python3-six => 1.10.0
Requires:   python3-dateutil
Requires:   python3-testtools
Requires:   python3-oslotest
Requires:   python3-networkx

%description -n python3-%{service}-tests-tempest
%{common_desc}
%endif


%if 0%{?with_doc}
%package -n python-%{service}-tests-tempest-doc
Summary:        python-%{service}-tests-tempest documentation

BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme

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
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

# Generate Docs
%if 0%{?with_doc}
%{__python2} setup.py build_sphinx -b html
# remove the sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info
%endif

%if 0%{?with_doc}
%files -n python-%{service}-tests-tempest-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
