# kaggle-NeurIPS-2024

## フォルダ構造
```
kaggle-NeurIPS-2024/
│
├── configs/
│   ├── __init__.py
│   ├──
│   ├── notebook2.py
│   └── ... (追加のノートブック)
│
├── notebooks/
│   ├── __init__.py
│   ├── notebook1.py
│   ├── notebook2.py
│   └── ... (追加のノートブック)
│
├── src/
│   ├── __init__.py
│   │
│   ├── core  # 全ノートブック共通の処理
│   │    ├── module1.py
│   │    ├── module2.py
│   │    └──  ... (追加のモジュールおよびパッケージ)
│   │
│   ├── pipeline  # モデル学習時に必要な処理のまとまり
│   │    ├── module1.py
│   │    ├── module2.py
│   │    └──  ... (追加のモジュールおよびパッケージ)
│   │
│   └── utils  # 上記に該当しないパッケージ
│        ├── module1.py
│        ├── module2.py
│        └──  ... (追加のモジュールおよびパッケージ)
│
│
└── README.md
```
---
## kaggle notebookからリポジトリ上のパッケージを利用する方法
```python
!curl -O https://raw.githubusercontent.com/{username}/{repository}/{branch}/{filename}.py

import sys
sys.path.append('/kaggle/working')

import filename  # or
from filename import ~~
```

