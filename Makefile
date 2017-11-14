DART_DEV=https://dev.dart.harvard.edu
DART_STAGE=https://stage.dart.harvard.edu

dart_firefox:
	behave -D instance_url=${DART_DEV} -D browser=firefox projects/dart/features

dart_chrome:
	behave -D instance_url=${DART_DEV} -D browser=chrome projects/dart/features

dart_ie:
	behave -D instance_url=${DART_DEV} -D browser=ie projects/dart/features

dart_edge:
		behave -D instance_url=${DART_DEV} -D browser=edge projects/dart/features

dart_phantomjs:
	behave -D instance_url=${DART_DEV} -D browser=phantomjs projects/dart/features

dart_opera:
	behave -D instance_url=${DART_DEV} -D browser=opera projects/dart/features

dart_safari:
	behave -D instance_url=${DART_DEV} -D browser=safari projects/dart/features

dart:
	make dart_chrome
	make dart_firefox

dart_docker:
	behave -D instance_url=${DART_STAGE} -D browser=phantomjs -D docker projects/dart/features

courselets_docker:
	behave -D instance_url=${DART_STAGE} -D browser=phantomjs -D docker projects/courselets/features


dart_firefox_local:
	behave -D instance_url=http://localhost:8001 -D browser=firefox projects/dart/features
