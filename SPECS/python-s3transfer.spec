%if 0%{?rhel} && 0%{?rhel} <= 7
# Minimum nose version is 1.3.3, while EL7 has 1.3.0
%bcond_with tests
%else
%bcond_without tests
%endif

%global pypi_name s3transfer

Name:           python-%{pypi_name}
Version:        0.1.13
Release:        1%{?dist}
Summary:        An Amazon S3 Transfer Manager

License:        ASL 2.0
URL:            https://github.com/boto/s3transfer
Source0:        https://pypi.io/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
S3transfer is a Python library for managing Amazon S3 transfers.

%package -n     python3-%{pypi_name}
Summary:        An Amazon S3 Transfer Manager
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-wheel
BuildRequires:  python3-botocore
BuildRequires:  python3-coverage
BuildRequires:  python3-unittest2
%endif # tests
Requires:       python3-botocore
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
S3transfer is a Python library for managing Amazon S3 transfers.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove online tests (see https://github.com/boto/s3transfer/issues/8)
rm -rf tests/integration

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
nosetests-%{python3_version} --with-coverage --cover-erase --cover-package s3transfer --with-xunit --cover-xml -v tests/unit/ tests/functional/
%endif # tests

%files -n python3-%{pypi_name} 
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Jun 11 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 0.1.13-1
- Update to 0.1.13
- Remove python2 package

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-2
- Rebuild for Python 3.6

* Thu Oct 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.7-1
- Uodate to 0.1.7

* Sun Oct 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Thu Aug 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Tue Aug 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-3
- Cleanup the spec a little bit
- Remove patch

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-2
- Add patch to remove tests needing web connection

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.0.1-1
- Initial package.
