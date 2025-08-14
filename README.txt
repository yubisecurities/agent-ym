#High level Instructions. Understand and Execute!

python3.12 -m venv adk_venv
source adk_venv/bin/activate
pip install -r requirements.txt
cat Forward_Cred_Trust.cer >> $(python3 -m certifi)
cat Forward-Trust-Cred-ECDSA.cer >> $(python3 -m certifi)
cat Root_Cred_CA.cer >> $(python3 -m certifi)
cd tg_agent
cp dummy_dot_env .env

Edit .env to add your own Key

cd ..
adk web

Point your browser to http://localhost:8000

Enjoy!
