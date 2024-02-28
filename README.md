# README

## Cheat sheet dos comandos

Para clonar um repositório:

``` bash
git clone <url do repositório>
```

Para criar uma branch:

``` bash
git checkout -b <nome da branch>
```

Para adicionar arquivos ao index:

``` bash
git add <nome do arquivo>
```

Para remover arquivos do index:

``` bash
git reset
```

Para "commitar" arquivos

``` bash
git commit
```

Para enviar as mudanças para o servidor

``` bash
git push
```

Para trazer as mudanças do servidor

``` bash
git pull
```

Para mesclar a branch main com a branch atual:

``` bash
git merge origin/main
```

Depois de resolver um conflito de merge, para termina-lo:

``` bash
git merge --continue
```

Para ver o histórico:

``` bash
git log
```

Para desfazer um commit:

``` bash
git revert <hash_do_commit:
```
