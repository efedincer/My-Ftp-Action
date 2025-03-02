# My-Ftp-Action
its a light ftp action for github actions CI/CD yml

# FTP Deploy Action

Bu GitHub Action, belirtilen FTP sunucusuna dosya yüklemenize yardımcı olur.

## Kullanım

```yaml
name: FTP Deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: FTP Deploy
        uses: efedincer/my-ftp-action@v1
        with:
          ftp_server: ${{ secrets.FTP_SERVER }}
          ftp_username: ${{ secrets.FTP_USERNAME }}
          ftp_password: ${{ secrets.FTP_PASSWORD }}
          local_dir: './dist'
          remote_dir: '/public_html'
