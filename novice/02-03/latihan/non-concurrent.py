#!/usr/bin/python3

import request
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

'''concurrency itu menjalankan 2 proses yang berbeda sekaligus, ngocok telur, ganti ngaduk sayur, single thread

    beda sama paralelism menggunakan multithreading(aplikasi satu processnya banyak), ngocok telur sambil ngaduk sayur, multithread
    
    persamaan mereka : sama2 u/ melakukan proses secara banyak dalam waktu berlebihan
    
'''