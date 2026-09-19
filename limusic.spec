Name:           limusic
Version:        %{limusic_version}
Release:        1%{?dist}
Summary:        Limusic — desktop YouTube Music client
License:        GPL-3.0-or-later
URL:            https://github.com/SimoHypers/limusic
Source0:        https://github.com/SimoHypers/limusic/releases/download/v%{limusic_version}/limusic-%{limusic_version}-1.x86_64.rpm

ExclusiveArch:  x86_64

Requires:       mpv-libs
Requires:       libappindicator-gtk3
Requires:       libwebkit2gtk-4.1.so.0()(64bit)
Requires:       libgtk-3.so.0()(64bit)

%description
Limusic is a desktop YouTube Music client written with Tauri, Rust and SvelteKit — ad-free, with no Electron. This COPR package redistributes upstream's official GitHub Release RPM.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
rpm2cpio %{SOURCE0} | (cd %{buildroot} && cpio -idm)

%files
/usr/bin/limusic-app
/usr/share/applications/*
/usr/share/icons/hicolor/*/apps/limusic-app.png

%changelog
* CHANGELOG_DATE_PLACEHOLDER Oguz <oguzkarayemis@gmail.com> - %{limusic_version}-1
- Upstream release v%{limusic_version} repackaged.
