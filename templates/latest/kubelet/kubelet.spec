%global debug_package %{nil}

Name: kubelet
#Version: {{ .RPMVersion }}
#Release: {{ .Revision }}
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Node agent for Kubernetes clusters

%if "%{_vendor}" == "debbuild"
Group: net
%endif

#Packager: Kubernetes Authors <dev@kubernetes.io>
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>
License: Apache-2.0
#URL: https://kubernetes.io
URL: https://github.com/kubernetes-loong64/kubernetes-loong64
BugURL: https://github.com/kubernetes-loong64/kubernetes-loong64/issues
# Source0: name_version.orig.tar.gz

BuildRequires: systemd
Requires: iptables >= 1.4.21
# {{ range $dep := .Metadata.Dependencies }}
# Requires: {{ $dep.Name }} {{ $dep.VersionConstraint }}
# {{ end }}
%if "%{_vendor}" == "debbuild"
Requires: mount
%endif
Requires: util-linux

%if "%{_vendor}" == "debbuild"
BuildRequires: systemd-deb-macros
%else
BuildRequires: systemd-rpm-macros
%endif

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
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sharedstatedir}/kubelet/
mkdir -p %{buildroot}%{_sysconfdir}/kubernetes/manifests/

install -p -m 755 ${KUBE_ARCH}/kubelet %{buildroot}%{_bindir}/kubelet
install -p -m 644 kubelet.service %{buildroot}%{_unitdir}/kubelet.service

# Required because dpkg-deb doesn't keep empty directories
%if "%{_vendor}" == "debbuild"
touch %{buildroot}%{_sharedstatedir}/kubelet/.kubelet-keep
touch %{buildroot}%{_sysconfdir}/kubernetes/manifests/.kubelet-keep
%endif

%if "%{_vendor}" == "debbuild"
mkdir -p %{buildroot}%{_sysconfdir}/default/
install -p -m 644 -T kubelet.env %{buildroot}%{_sysconfdir}/default/kubelet
%else
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 644 -T kubelet.env %{buildroot}%{_sysconfdir}/sysconfig/kubelet
%endif

%files
%{_bindir}/kubelet
%{_unitdir}/kubelet.service
%dir %{_sharedstatedir}/kubelet
%dir %{_sysconfdir}/kubernetes
%dir %{_sysconfdir}/kubernetes/manifests
%if "%{_vendor}" == "debbuild"
%{_sharedstatedir}/kubelet/.kubelet-keep
%{_sysconfdir}/kubernetes/manifests/.kubelet-keep
%config(noreplace) %{_sysconfdir}/default/kubelet
%else
%config(noreplace) %{_sysconfdir}/sysconfig/kubelet
%endif
%license LICENSE
%doc README.md

%preun
%systemd_preun kubelet.service

%post
%systemd_post kubelet.service

%postun
%systemd_postun kubelet.service

%changelog
