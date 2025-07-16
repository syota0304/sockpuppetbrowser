#!/bin/sh

while true; do
  echo "[clean-tmp] start"

  find /tmp -type d -name "chrome-puppeteer-proxy*" -atime +0 -exec rm -rf {} +

  echo "[clean-tmp] done"
  sleep 6h
done