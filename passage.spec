# SPDX-FileCopyrightText: The passage-rpm Authors
# SPDX-License-Identifier: 0BSD

Name:           passage
Summary:        A password manager using age
Version:        1.7.4a1
Release:        %autorelease
License:        GPLv2+
Url:            https://github.com/FiloSottile/passage
BuildArch:      noarch
Source:         https://github.com/FiloSottile/passage/archive/refs/tags/1.7.4a1.tar.gz

BuildRequires:  make
BuildRequires:  git-core
Recommends:     (wl-clipboard if libwayland-client else xclip)
Recommends:     (xclip if xorg-x11-server-Xorg else wl-clipboard)
Requires:       git-core
Requires:       age
Requires:       qrencode
Requires:       tree >= 1.7.0

%description
Stores, retrieves, generates, and synchronizes passwords securely using age
and git.

%prep
%setup -q -n passage-%{version}

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
     BINDIR=%{_bindir} SYSCONFDIR=%{_sysconfdir} \
     MANDIR=%{_mandir} WITH_ALLCOMP="yes" \
     install

%files
%doc README COPYING
%{_bindir}/passage
%{_datadir}/bash-completion/completions/passage
%{_datadir}/fish/vendor_completions.d/passage.fish
%{_datadir}/zsh/site-functions/_passage
%dir %{_prefix}/lib/passage
%dir %{_prefix}/lib/passage/extensions

%changelog
%autochangelog
