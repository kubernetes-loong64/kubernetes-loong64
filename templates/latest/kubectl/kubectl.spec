%global debug_package %{nil}

Name: kubectl
#Version: {{ .RPMVersion }}
#Release: {{ .Revision }}
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Command-line utility for interacting with a Kubernetes cluster

%if "%{_vendor}" == "debbuild"
Group: admin
%endif

#Packager: Kubernetes Authors <dev@kubernetes.io>
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>
License: Apache-2.0
#URL: https://kubernetes.io
URL: https://github.com/kubernetes-loong64/kubernetes-loong64
BugURL: https://github.com/kubernetes-loong64/kubernetes-loong64/issues
# Source0: name_version.orig.tar.gz

%description
%{summary}.

%prep
#%setup -q -c
# No source tarball — binaries are provided externally

%build
# Nothing to build

%install
# Detect host arch
KUBE_ARCH="$(uname -m)"

# Install binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ${KUBE_ARCH}/kubectl %{buildroot}%{_bindir}/kubectl

%files
%{_bindir}/kubectl
%license LICENSE
%doc README.md

%changelog
