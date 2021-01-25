LINKS=../knocqueue/links
BASE=../../
cd $LINKS
rm -rf ./dist ./build *.egg-info
python setup.py sdist bdist_wheel
pip install --upgrade  \
            --ignore-installed \
            --target=$BASE/venv/lib/python3.8/site-packages \
            --no-index \
            -f ./dist/ \
            knocqueue-utils-KNOCQUEUE
rm -rf ./dist ./build *.egg-info
