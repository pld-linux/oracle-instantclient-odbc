#
# NOTE:
# - see "URL:" for download links
# - if you want to build 32-bit version, you don't have to download Source1.
#   Just comment it out.
# - if you want to build 64-bit version, comment out Source0

%define		i386rel		0.1
%define		x8664rel	0.1.0-1
Summary:	ODBC for Oracle Database Instant Client
Name:		oracle-instantclient-odbc
Version:	11.2
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications
Source0:	instantclient-odbc-linux32-%{version}.%{i386rel}.zip
# NoSource0-md5:	55a09a9ba803dbc3f9d053a9cba8af2d
Source1:	oracle-instantclient%{version}-odbc-%{version}.%{x8664rel}.x86_64.zip
# NoSource1-md5:	5bb55794190d4131133c92adfba57f8a
NoSource:	0
NoSource:	1
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
BuildRequires:	unzip
Requires(post):	/usr/bin/odbcinst
Requires:	unixODBC
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		srcdir	instantclient_%(echo %{version} | tr . _)

%description
Oracle Database Instant Client Package - ODBC.
Additional libraries for enabling ODBC applications.

%prep
%ifarch %{ix86}
%setup -q -c -T -b 0
%endif

%ifarch %{x8664}
%setup -q -c -T -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install %{srcdir}/*.so* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# install Orcale driver
/usr/bin/odbcinst -i -d -r <<EOF
[Oracle 11g]
Description = Oracle ODBC driver for Oracle 11g
Driver = %{_libdir}/libsqora.so.11.1
Setup = 
EOF

%files
%defattr(644,root,root,755)
%doc %{srcdir}/*.htm*
%attr(755,root,root) %{_libdir}/*.so*
