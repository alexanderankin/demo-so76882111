from app import app

def test_some_func():
    print('running test: test_some_func')
    assert app.some_func() == 'abcd'

if __name__ == '__main__':
    test_some_func()
