# Dcard - demo
### 這是使用 Django 框架建立的個人部落格專案，旨在提供一個簡單且清晰的部落格平台，讓使用者能夠閱讀文章、發表評論並瀏覽不同的內容。本專案展示了如何使用 Django 建立一個完整的部落格，並涵蓋了文章創建和管理的基本功能。

## 主要功能
### 使用者認證：註冊、登入、登出功能。
### 部落格文章：創建、編輯、刪除部落格文章。
### 評論功能：讀者可以在文章下方發表評論。
### 分類功能：將文章按類別分類，方便瀏覽。
### 分頁功能：支持文章分頁，便於瀏覽大量文章。
### 管理界面：使用 Django 內建的管理界面來管理使用者、文章和評論。
## 技術架構
### 後端：Django
### 前端：HTML、CSS（使用 Bootstrap 進行樣式設計）
### 資料庫：SQLite（默認）
### 認證系統：使用 Django 內建的認證系統
### 部署：hebur
## 前置條件
### 在本地運行本專案之前，請確保已安裝以下工具：

Python 3.x
pip（Python 的包管理工具）
Django（版本 3.x 或以上）
SQLite 或 PostgreSQL（可選）
安裝步驟
克隆專案到本地：

bash
複製程式碼
git clone https://github.com/yourusername/my-personal-blog.git
cd my-personal-blog
創建虛擬環境（建議使用虛擬環境）：


python3 -m venv venv
source venv/bin/activate  # Windows 上使用：venv\Scripts\activate
安裝依賴包：


pip install -r requirements.txt
執行資料庫遷移：


python manage.py migrate
創建超級使用者，以便進入 Django 管理界面：


python manage.py createsuperuser
啟動開發伺服器：

python manage.py runserver
開發伺服器將在 http://127.0.0.1:8000 運行。

使用說明
訪問首頁可以查看最新的部落格文章。
點擊文章標題可進入文章詳情頁，並可以發表評論。
註冊或登入帳號後，可以管理自己的文章與評論。
管理員用戶可以進入 /admin 頁面來管理網站的內容。
