# GDSC YZU Bot

GDSC YZU DC server 御用~~奴隸~~管家

## 使用設定

請於根目錄新增 `token.txt` ，放入 bot 的 token ，如：

```
ODY5NTU4OTY1MjY3MTAEI2VBL0A3.G3Gs5n.BGvAKCI2WW8xAzliyEKiekfDMBPYwOdOp-Q56tww 
```

## 功能

在聊天室中輸入 `.help` 獲得指令列表

```
一般成員可用：
.help: 呼叫此訊息
.code: 取得bot的程式碼
.website: 取得社團所有網站的網址
.ver: 獲得當前版本資訊
.ver <不為0之數字>: 獲得完整歷史版本資訊

管理員專用：
reload: 上線某個更新過後的檔案
unload: 下架某個檔案
load: 上架某個被unloaded的檔案
delete_message <數字>: 刪除<數字>條訊息（beta）
```

##  檔案

- `announcement.py` : 每隔兩天在 #機器人公告 中發布公告
- `event.py` : 監聽 server 中的每一則訊息並做出反應，如有人說「早安」，機器人就會回「安呀」
- `react.py` : 放指令的地方，只對`.`開頭的訊息有反應
- `role_reaction.py` : 當有人在 #身分組認領 中點擊表情符號時，給他身分組
