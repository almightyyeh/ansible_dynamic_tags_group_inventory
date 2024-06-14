
# Ansible Tags Group Dynamic Inventory

### 開發目的
Ansible 主機的群組管理，一直都是相當不容易的一個工作
透過hosts file 增加 tags 欄位，使得Ansible 可以動態的進行主機的分組

新增的 tags 欄位以 `,` 進行分組，可任意增加刪除。 

`hosts_tag_file` 範例：
```
192.168.1.1	test1    tags=web,nginx,開發二組,linux,ubuntu,系統管理組
192.168.1.2	test2    tags=web,httpd,開發一組,linux,redhat,系統管理組
192.168.1.3	test3    tags=web,tomcat,windows,windows2016,開發三組,系統管理組
192.168.1.4	test4    tags=cache,redis,linux,系統管理組
192.168.1.5	test5    tags=cache,memcache,linux,系統管理組
192.168.1.6	test6    tags=quene,kafka,linux,redhat,開發三組,系統管理組
192.168.1.7	test7    tags=quene,rabbitmq,linux,centos,開發一組,系統管理組
192.168.1.8	test8    tags=quene,zeromq,ubuntu,linux,開發二組,系統管理組
192.168.1.9	test9    tags=database,mariadb,centos,linux,開發一組,系統管理組
192.168.1.10	test10   tags=database,postgresql,linux,ubuntu,開發二組,系統管理組
192.168.1.11	test11   tags=database,mssql,windows,windows2022,開發三組,系統管理組
```

### 使用方法:

列出所有主機:
```
# ansible -i ansible_tags_inventory.py all --list-host
  hosts (11):
    test7
    test9
    test11
    test10
    test4
    test5
    test1
    test2
    test6
    test8
    test3
```

列出上述範例 `linux` 的主機
```
# ansible -i ansible_tags_inventory.py linux --list-host
  hosts (9):
    test1
    test2
    test4
    test5
    test6
    test7
    test8
    test9
    test10
```

列出上述範例 `開發二組` 的主機
```
# ansible -i ansible_tags_inventory.py 開發二組 --list-host
  hosts (3):
    test1
    test8
    test10
```

以此類推


### 配置 `hosts_tag_file` 位置

修改 `ansible_tags_inventory.py` 檔案路徑

```
(...)

# Settings Variable
hosts_tag_file_path = "hosts_tag_file"

(...)
```


