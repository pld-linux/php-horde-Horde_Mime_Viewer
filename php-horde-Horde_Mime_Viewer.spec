# TODO
# - compress .js/.css
%define		status		stable
%define		pearname	Horde_Mime_Viewer
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde MIME Viewer Library
Name:		php-horde-Horde_Mime_Viewer
Version:	1.0.2
Release:	1
License:	LGPL (PHP code), MIT and GPL (syntaxhighlighter)
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	8fe0c1943ebcb64f7547aa298ceb2136
URL:		https://github.com/horde/horde/tree/master/framework/Mime_Viewer/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-horde-Horde_Role
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Browser < 2.0.0
Requires:	php-horde-Horde_Compress < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Text_Filter < 2.0.0
Requires:	php-horde-Horde_Text_Flowed < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hordedir	/usr/share/horde

%description
Provides rendering drivers for MIME data.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/www/horde .

# common licenses
%{__rm} horde/js/syntaxhighlighter/LGPL-LICENSE
%{__rm} horde/js/syntaxhighlighter/MIT-LICENSE

# sources not needed runtime
%{__rm} -r horde/js/syntaxhighlighter/src

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{hordedir}}
%pear_package_install

cp -a horde/* $RPM_BUILD_ROOT%{hordedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Mime/Viewer
%{php_pear_dir}/Horde/Mime/Viewer.php
%{php_pear_dir}/data/Horde_Mime_Viewer

%dir %{hordedir}/js/syntaxhighlighter
%dir %{hordedir}/js/syntaxhighlighter/scripts
%{hordedir}/js/syntaxhighlighter/scripts/*.js
%dir %{hordedir}/js/syntaxhighlighter/styles
%{hordedir}/js/syntaxhighlighter/styles/*.css
