"""
Misalkan Anda berada di tim desain untuk pembaca e-book baru. apa itu?
kelas dan metode utama yang akan dilakukan oleh perangkat lunak Python untuk pembaca Anda
perlu? Anda harus menyertakan diagram pewarisan untuk kode ini, tetapi Anda
tidak perlu menulis kode yang sebenarnya. Arsitektur perangkat lunak Anda harus
setidaknya sertakan cara bagi pelanggan untuk membeli buku baru, melihat daftar mereka
membeli buku, dan membaca buku yang mereka beli.


Book class --> get_price(), get_id(), get_author(), num_of_pages(), get_summary()
	Book(title, author, price, unique_id, summary, pages)
Nested in Book will be a Page class --> read_text(), highlight_chars(seq_of_chars), 
get_page_number(), next_page(), go_to_page(n)
	Page(page_number, text)
Customer Class --> get_account_info(), see_shelf(), read_book(title), buy_book(title)
	Customer(account_info, shelf)
""
