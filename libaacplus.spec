Name:           libaacplus
Version:        2.0.2
Release:        1%{?dist}
Summary:        3GPP HE-AAC+ v2 Encoder Shared Library

License:        3GPP Commercial license
URL:            http://tipok.org.ua/node/17
Source0:        http://tipok.org.ua/downloads/media/aacplus/%{name}/%{name}-%{version}.tar.gz
Source1:        http://www.3gpp.org/ftp/Specs/archive/26_series/26.410/26410-800.zip

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fftw-devel
BuildRequires:  libtool

%description
3GPP AAC+ High Efficiency Advanced Audio Codec v2 (HE-AAC+) Encoder Shared
Library.

HE-AAC audio v2 (with SBR + PS) is the superb audio encoder used to encode high
quality audio at really low bitrates (32 kbit/s). This package contains the
HE-AAC+ v2 library, based on the reference implementation from 3GPP.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     aacplusenc
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n aacplusenc
3GPP AAC+ High Efficiency Advanced Audio Codec v2 (HE-AAC+) Encoder.

%prep
%setup -q
cp %{SOURCE1} src

%build
# This makes build stop if any download is attempted
export http_proxy=http://127.0.0.1

autoreconf -vif
%configure --disable-static

# Parallel make breaks 3GPP source unpacking.
make

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/aacplus.pc

%files -n aacplusenc
%{_bindir}/aacplusenc
%{_mandir}/man1/aacplusenc.1*

%changelog
* Sun Dec 13 2015 Simone Caronni <negativo17@gmail.com> - 2.0.2-1
- First build.
