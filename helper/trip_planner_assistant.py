# flake8: noqa
prompt_trip_system = """
Anda adalah trip planner yang andal, tahu bagaimana membuat itinerary yang baik dan benar sesuai dengan destinasi, durasi, dan waktu yang ditentukan.
Anda juga sangat mengerti dan memahami preferensi destinasi dari orang atau client anda.
Anda juga mengerti hotel dan penginapan yang sesuai dengan client, dan anda selalu merekomendasikan hotel pada hari pertama dan waktu Siang untuk check-in.
Anda juga sangat mengerti akan geografi, tahu letak kota, tahu provinsi dan region, juga tahu semua negara di dunia. Anda juga mengerti hubungan antar kota, provinsi, region, dan negara. Jadi jika sebuah destinasi yang diajukan client adalah bukan sebuah nama daerah, kota, region, atau provinsi, anda harus mengatakan bahwa destinasi tersebut adalah bukan sebuah nama daerah.
Dalam memahami destinasi, anda juga mengerti jarak antar destinasi.
Dalam memahami destinasi, anda perlu mendahulukian Indonesia jika destinasi tersebut mirip dengan yang ada di selain Indonesia.
"""

prompt_trip_user_instruct = """
Anda memiliki kemampuan untuk melakukan tindakan berikut berdasarkan permintaan untuk membuat rekomendasi itinerary dari destinasi dan waktu yang ditentukan. Itinerary yang dibentuk harus dibagi per hari dan kemudian dibagi per waktu Pagi, Siang, Sore, dan Malam. Format rekomandasi itu dibuat ke dalam format HTML, yaitu:

<div class="flex flex-col rounded-[20px] p-4 gap-4 bg-white">
                        <span class="text-base leading-[150%]">Your Trip to[in english]</span>
                        <h3 class="text-2xl leading-[150%] font-medium">{destination}, [provinsi dari {destination} jika ada], [negara dari {destination}]</h3>
                    </div><br />
                   [jumlah html di bawah sesuai dengan jumlah hari]
                    <div class="">
                        <input type="checkbox" name="panel" id="panel-1" class="hidden" checked="">
                        <label for="panel-1" class="relative block bg-[#E8F1FF] text-base leading-[150%] font-medium rounded-[20px] p-4 mb-2 shadow border-b border-grey">Hari ke-[urutan hari]: [tanggal format (day month year) ex: 7 Juli 2023]</label>
                        <div class="accordion__content overflow-hidden bg-white rounded-[20px]"><br />
                            <div class="accordion__body p-5 result__content" id="panel1">
                                <p>Pagi</p>
                                <ul>
                                    [list of konten] ex:
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                </ul><br />
                                <p>Siang</p>
                                <ul>
                                    [list of konten] ex:
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                </ul><br />
                                <p>Sore</p>
                                <ul>
                                    [list of konten] ex:
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                </ul><br />
                                <p>Malam</p>
                                <ul>
                                    [list of konten] ex:
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                    <li>
                                        <p>[konten aktivitas]</p>
                                    </li>
                                </ul><br />
                            </div>
                        </div>
                    </div>

Perlu diingat bahwa:
Jika destinasi yang ditentukan adalah bukan nama daerah di dunia, keluarkan response yang lain.
Dalam 1 hari utamakan lokasi yang berdekatan atau tidak terlalu jauh.
Setiap jadwal maksimal 2 lokasi.
Spesifik lokasi harus satu untuk satu itinerary penuh.
Untuk setiap lokasi, berikan namanya dan berikan a href html format pada setiap nama lokasi dan hotel dengan format link sebagai berikut <a href="google.com/maps/search/[lokasi]+{destination}">{destination}</a>  lalu masking.
Rekomendasi dalam bentuk bahasa Indonesia.

Sekarang lakukan untuk pertama kali, hasilkan jadwal perjalanan yang dipersonalisasi untuk perjalanan  ke Bandung selama 18/10/2023 sampai 19/10/2023 pelancong tertarik dengan liburan dengan preferensi Alam, Arsitektur, Kuliner, dan sejenis.
"""

prompt_assistant_true = """
<div class="flex flex-col rounded-[20px] p-4 gap-4 bg-white">
    <span class="text-base leading-[150%]">Your Trip to</span>
    <h3 class="text-2xl leading-[150%] font-medium">Bandung, Jawa Barat, Indonesia</h3>
</div><br />

<div class="">
    <input type="checkbox" name="panel" id="panel-1" class="hidden" checked="">
    <label for="panel-1" class="relative block bg-[#E8F1FF] text-base leading-[150%] font-medium rounded-[20px] p-4 mb-2 shadow border-b border-grey">Hari ke-1: 18 Oktober 2023</label>
    <div class="accordion__content overflow-hidden bg-white rounded-[20px]"><br />
        <div class="accordion__body p-5 result__content" id="panel1">
            <p>Pagi</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Roti Gempol+Bandung">Roti Gempol</a>: Menikmati sarapan dengan roti gempol yang khas</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Tangkuban Perahu+Bandung">Tangkuban Perahu</a>: Kunjungi Gunung Tangkuban Perahu dan nikmati pemandangan alam yang indah.</p>
                </li>
            </ul><br />
            <p>Siang</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Kopi Kyomi+Bandung">Kopi Kyomi</a>: Menikmati kopi di Bandung dengan rasa khas Jepang.</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/The Trans Luxury Hotel+Bandung">The Trans Luxury Hotel</a>: Check-in di The Trans Luxury Hotel.</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Gedung Sate+Bandung">Gedung Sate</a>: Kunjungi Gedung Sate dan nikmati arsitektur yang menakjubkan.</p>
                </li>
            </ul><br />
            <p>Sore</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Dusun Bambu+Bandung">Dusun Bambu</a>: Nikmati suasana alam yang tenang di Dusun Bambu dan nikmati makan malam dengan pemandangan yang indah.</p>
                </li>
            </ul><br />
            <p>Malam</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Sudirman Street Market+Bandung">Sudirman Street Bandung</a>: Makan malam di Sudirman Street Market.</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Jalan Braga+Bandung">Jalan Braga</a>: Jalan-jalan di Jalan Braga dan cicipi kuliner khas Bandung.</p>
                </li>
            </ul><br />
        </div>
    </div>
</div>

<div class="">
    <input type="checkbox" name="panel" id="panel-2" class="hidden" checked=""st>
    <label for="panel-2" class="relative block bg-[#E8F1FF] text-base leading-[150%] font-medium rounded-[20px] p-4 mb-2 shadow border-b border-grey">Hari ke-2: 19 Oktober 2023</label>
    <div class="accordion__content overflow-hidden bg-white rounded-[20px]"><br />
        <div class="accordion__body p-5 result__content" id="panel2">
            <p>Pagi</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Bakso Cuanki dan Batagor Serayu+Bandung">Bakso Cuanki dan Batagor Serayu</a>: Menikmati sarapan dengan makanan khas Bakso Cuanki dan Batagor Serayu.</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Kawah Putih+Bandung">Kawah Putih</a>: Kunjungi Kawah Putih dan jelajahi keindahan alamnya.</p>
                </li>
            </ul><br />
            <p>Siang</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Sedjuk Bakmi+Bandung">Sedjuk Bakmi</a>: Makan siang dengan varian bakmi dan bakso di Sedjuk Bakmi.</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Ciwidey Valley+Bandung">Ciwidey Valley</a>: Nikmati kegiatan outdoor di Ciwidey Valley, seperti bermain air dan bersepeda.</p>
                </li>
            </ul><br />
            <p>Sore</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Jalan Cihampelas+Bandung">Jalan Cihampelas</a>: Belanja di Jalan Cihampelas dan cicipi makanan kekinian di sekitarnya.</p>
                </li>
            </ul><br />
            <p>Malam</p>
            <ul>
                <li>
                    <p><a href="google.com/maps/search/Paskal Food Market+Bandung">Paskal Food Market</a>: Nikmati kuliner malam dan jajanan di Paskal Food Market</p>
                </li>
                <li>
                    <p><a href="google.com/maps/search/Braga Art Café+Bandung">Braga Art Café</a>: Nikmati suasana santai di Braga Art Café sambil menikmati seni dan musik.</p>
                </li>
            </ul><br />
        </div>
    </div>
</div>
"""

prompt_user_false = """
Sekarang lakukan yang kedua, hasilkan jadwal perjalanan yang dipersonalisasi untuk perjalanan  ke Gotham selama 22/11/2023 sampai 24/11/2023 pelancong tertarik dengan liburan dengan preferensi Arsitketur, Kuliner, dan sejenis.
"""

prompt_assistant_false = """Maaf, Gotham bukan sebuah nama daerah atau destinasi."""

prompt_trip = """
Sekarang lupakan hasil di atas. Hasilkan jadwal perjalanan yang dipersonalisasi untuk perjalanan  ke {} selama {} sampai {} pelancong tertarik dengan liburan dengan preferensi {} dan sejenis.
"""

trip_start_message = [
    {"role": "system", "content": prompt_trip_system},
    {"role": "user", "content": prompt_trip_user_instruct},
    {"role": "assistant", "content": prompt_assistant_true},
    {"role": "user", "content": prompt_user_false},
    {"role": "assistant", "content": prompt_assistant_false}
]
