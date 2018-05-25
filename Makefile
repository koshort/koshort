# Deployment instructions
# 1. Check translations at docs/locale/ko/LC_MESSAGES/*.po
# 2. Check version at setup.py
# 3. $ make testpypi
# 4. $ make pypi 
# 5. Document update at RTD (latest)
# 6. Push tag

build:
	python setup.py sdist --formats=gztar,zip

build_docs:
	docs/build.bat
	cd docs\
		&& sphinx-apidoc -o docs/

check:
	pyroma .
	pylint --ignore=E501 koshort

fix:
	autopep8 koshort --recursive --in-place --pep8-passes 2000 --verbose --ignore E501

testpypi:
	sudo python setup.py register -r pypitest
	sudo python setup.py sdist --formats=gztar,zip upload -r pypitest
	sudo python setup.py bdist_wheel upload -r pypitest

pypi:
	sudo python setup.py register -r pypi
	sudo python setup.py sdist --formats=gztar,zip upload -r pypi
	sudo python setup.py bdist_wheel upload -r pypi

testall:
	python -m pytest --cov=koshort test/

extract_i18n:
	cd docs\
	    && make gettext\
	    && sphinx-intl update -p _build/locale -l ko

update_i18n:
	cd docs\
	    && sphinx-intl build\
	    && make -e SPHINXOPTS="-D language='ko'" html
