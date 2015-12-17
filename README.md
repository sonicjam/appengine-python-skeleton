appengine-python-skeleton
=========================

Google App Engine Python アプリケーションの骨組。

準備
----

Google Cloud SDK をインストール:

```
curl https://sdk.cloud.google.com | bash
```

- [Cloud SDK — Google Cloud Platform](https://cloud.google.com/sdk/)

インストール後、SDK の PATH が通った状態にしておく。

PyPI から必要な Python パッケージを `./lib` ディレクトリにインストール:

```
pip install -t ./lib -r ./requirements.txt
```


開発
----

テストサーバーの起動:

```
dev_appserver.py ./
```

次の URL から確認:

- http://localhost:8080/ (app)
- http://localhost:8000/ (dashboard)

テストランナーの実行:

```
GAE_SDK_PATH=/path/to/google-cloud-sdk/platform/google_appengine python ./test/runner.py
```


メンテナ
--------

Yu Inao &lt;yu.inao@sonicjam.co.jp&gt;


License
-------

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```
