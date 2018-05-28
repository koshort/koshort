# Deployment instructions
# 1. Check translations at docs/locale/ko/LC_MESSAGES/*.po
# 2. Check version at setup.py
# 3. $ make testpypi
# 4. $ make pypi 
# 5. Document update at RTD (latest)
# 6. Push tag

build_package:
	del dist\*.egg  # These code is only for windows
	del dist\*.whl
	del dist\*.tar.gz
	python setup.py sdist --formats=gztar,zip

build_docs:
	del docs\koshort*.rst
	sphinx-apidoc -F -o docs koshort/ --separate
	docs\make.bat html

check:
	pyroma .
	pycodestyle koshort --ignore E501

fix:
	autopep8 koshort --recursive --in-place --pep8-passes 2000 --verbose --ignore E501

testpypi:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*.tar.gz

pypi:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*.tar.gz

test:
	python -m pytest --cov=koshort tests/

extract_i18n:
	cd docs\
	    && make gettext\
	    && sphinx-intl update -p _build/locale -l ko

update_i18n:
	cd docs\
	    && sphinx-intl build\
	    && make -e SPHINXOPTS="-D language='ko'" html
