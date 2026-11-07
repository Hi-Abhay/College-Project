import io, os, glob
import app as flaskapp

client = flaskapp.app.test_client()

def test_home():
    r = client.get('/')
    assert r.status_code == 200, r.status_code
    assert b'<html' in r.data.lower() or b'<!doctype' in r.data.lower()
    print("PASS home GET -> 200, HTML served")

def test_upload_get_redirects():
    r = client.get('/upload/')
    assert r.status_code in (301, 302), r.status_code
    print("PASS /upload/ GET -> redirect", r.status_code, "->", r.headers.get('Location'))

def test_predict():
    sample = sorted(glob.glob('uploadimages/*.jpg') + glob.glob('uploadimages/*.JPG'))[0]
    with open(sample, 'rb') as f:
        data = {'img': (io.BytesIO(f.read()), 'leaf.jpg')}
    r = client.post('/upload/', data=data, content_type='multipart/form-data')
    assert r.status_code == 200, r.status_code
    body = r.data.decode('utf-8', 'ignore')
    assert 'name' in body.lower() or 'cause' in body.lower() or 'cure' in body.lower()
    print("PASS predict POST -> 200; sample:", os.path.basename(sample))

def test_uploaded_images_route():
    sample = os.path.basename(sorted(glob.glob('uploadimages/*.jpg'))[0])
    r = client.get('/uploadimages/' + sample)
    assert r.status_code == 200, r.status_code
    print("PASS serve uploaded image -> 200")

if __name__ == '__main__':
    for t in [test_home, test_upload_get_redirects, test_predict, test_uploaded_images_route]:
        try:
            t()
        except Exception as e:
            print("FAIL", t.__name__, "->", repr(e))
