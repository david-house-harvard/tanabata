firefox:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=firefox

chrome:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=chrome

ie:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=ie

edge:
		behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=edge

phantomjs:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=phantomjs

opera:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=opera

safari:
	behave -D instance_url=https://dart-test-stage.raccoongang.com -D browser=safari

love:
	make chrome
	make firefox
