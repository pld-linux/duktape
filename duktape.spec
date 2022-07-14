Summary:	Embeddable JavaScript engine with a focus on portability and compact footprint
Summary(pl.UTF-8):	Osadzalny silnik JavaScriptu, rozwijany z myślą o przenośności i małych wymaganiach
Name:		duktape
Version:	2.7.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://duktape.org/download.html
Source0:	https://duktape.org/%{name}-%{version}.tar.xz
# Source0-md5:	b3200b02ab80125b694bae887d7c1ca6
Patch0:		%{name}-build.patch
URL:		https://duktape.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duktape is an embeddable JavaScript engine, with a focus on
portability and compact footprint.

Main features:
- Embeddable, portable, compact
- ECMAScript E5/E5.1 compliant, with some semantics updated from
  ES2015+
- Partial support for ECMAScript 2015 (E6) and ECMAScript 2016 (E7),
  Post-ES5 feature status, kangax/compat-table
- ES2015 TypedArray and Node.js Buffer bindings
- WHATWG Encoding API living standard
- Built-in debugger
- Built-in regular expression engine
- Built-in Unicode support
- Minimal platform dependencies
- Combined reference counting and mark-and-sweep garbage collection
  with finalization
- Custom features like coroutines
- Property virtualization using a subset of ECMAScript ES2015 Proxy
  object
- Bytecode dump/load for caching compiled functions
- Distributable includes and optional logging framework,
  CommonJS-based module loading implementations, CBOR bindings, etc

%description
Duktape to osadzony silnik JavaScriptu, którego rozwój skupia się na
przenośności i niewielkich wymaganiach.

Główne cechy:
- osadzalny, przenośny, niewielki
- zgodny z ECMAScript E5/E5.1 z niektórymi elementami składni ES2015+
- częściowa obsługa ECMAScript 2015 (E6) i ECMAScript 2016 (E7),
  elementów Post-ES5, tablic kangax/compat
- wiązania ES2015 TypedArray i Node.js Buffer
- żywy standard WHATWG Encoding API
- wbudowany debugger
- wbudowany silnik wyrażeń regularnych
- wbudowana obsługa Unicode
- minimalne wymagania dla platformy
- odśmiecanie kombinowane ze zliczaniem referencji i mark-and-sweep
- dodatkowa funkcjonalność, taka jak korutyny
- wirtualizacja własności przy użyciu podzbioru obiektów ECMAScript
  ES2015 Proxy
- zrzucanie/ładowanie bajtkodu do zapamiętywania skompilowanych
  funkcji
- rozprowadzalne pliki dołączane, opcjonalny szkielet logowania,
  implementacje ładowalnych modułów oparte na CommonJS, wiązania CBOR
  itd.

%package devel
Summary:	Header files for Duktape library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Duktape
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Duktape library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Duktape.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f Makefile.sharedlibrary \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	INSTALL_PREFIX=%{_prefix} \
	LIBDIR="/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f Makefile.sharedlibrary install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PREFIX=%{_prefix} \
	LIBDIR="/%{_lib}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst README.rst
%attr(755,root,root) %{_libdir}/libduktape.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libduktape.so.207

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libduktape.so
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_pkgconfigdir}/duktape.pc
