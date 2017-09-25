dart_firefox:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=firefox projects/dart/features

dart_chrome:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=chrome projects/dart/features

dart_ie:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=ie projects/dart/features

dart_edge:
		behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=edge projects/dart/features

dart_phantomjs:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=phantomjs projects/dart/features

dart_opera:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=opera projects/dart/features

dart_safari:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=safari projects/dart/features

dart:
	make dart_chrome
	make dart_firefox

dart_docker:
	behave -D instance_url=${STAGE_URL} -D browser=phantomjs -D docker projects/dart/features

courselets_docker:
	behave -D instance_url=${STAGE_URL} -D browser=phantomjs -D docker projects/courselets/features
