# Build the project
echo "Installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
