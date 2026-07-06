%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name: kubernetes-cni
#Version: {{ .RPMVersion }}
#Release: {{ .Revision }}
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Binaries required to provision kubernetes container networking

%if "%{_vendor}" == "debbuild"
Group: net
%endif

#Packager: Kubernetes Authors <dev@kubernetes.io>
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>
License: Apache-2.0
#URL: https://kubernetes.io
URL: https://github.com/kubernetes-loong64/kubernetes-loong64
BugURL: https://github.com/kubernetes-loong64/kubernetes-loong64/issues
# Source0: %{name}_%{version}.orig.tar.gz

%description
%{summary}.

%prep
#%setup -q -c
# No source tarball — binaries are provided externally

%build
# Nothing to build

%install
# Detect host arch
#KUBE_ARCH="$(uname -m)"
KUBE_ARCH="%{kube_arch}"

# Install files
mkdir -p %{buildroot}/opt/cni/bin
mkdir -p %{buildroot}%{_sysconfdir}/cni/net.d/

cp -a ${KUBE_ARCH}/* %{buildroot}/opt/cni/bin/

%if "%{_vendor}" == "debbuild"
touch %{buildroot}%{_sysconfdir}/cni/net.d/.kubernetes-cni-keep
%endif

%files
/opt/cni/
%dir %{_sysconfdir}/cni
%dir %{_sysconfdir}/cni/net.d
%if "%{_vendor}" == "debbuild"
%{_sysconfdir}/cni/net.d/.kubernetes-cni-keep
%endif
%license LICENSE
%doc README.md

%changelog
