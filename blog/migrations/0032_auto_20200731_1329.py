# Generated by Django 3.0.6 on 2020-07-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200730_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_APD_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_GMT_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_GMT_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_dekontaminasi_dan_disinfeksi_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_general_safety',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_identifikasi_perencanaan_dan_respon_keadaan_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_infrastruktur_dan_operasional',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_investigasi_kecelakaan_dan_insiden',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kalibrasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_keamanan_fisik_dan_pengendalian_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_keamanan_informasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kedaruratan_medik',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_latar_belakang_sdm',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_manajemen_pemeliharaan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_monitoring_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pelabelan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pemeliharaan_dan_dekontaminasi_reusable_apd',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengadaan_alat_pelindung_diri',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_program_kesehatan_kerja',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_rekrutmen_pelatihan_dan_kompetensi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_sertifikasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_simulasi_dan_pelatihan_tanggap_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_suksesi_dan_eksklusi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_vaksinasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_validasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_23',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_24',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_25',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_26',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_27',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_28',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_29',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_30',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_31',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_32',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_33',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_34',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_35',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_36',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_37',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_38',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_39',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_40',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_41',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_42',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_43',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_44',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_45',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_46',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_47',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_48',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_49',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_50',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_51',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_52',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_53',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_54',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_APD_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_GMT_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_GMT_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_dekontaminasi_dan_disinfeksi_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_general_safety',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_identifikasi_perencanaan_dan_respon_keadaan_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_infrastruktur_dan_operasional',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_investigasi_kecelakaan_dan_insiden',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kalibrasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_keamanan_fisik_dan_pengendalian_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_keamanan_informasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kedaruratan_medik',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_latar_belakang_sdm',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_manajemen_pemeliharaan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_monitoring_peralatan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pelabelan',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pemeliharaan_dan_dekontaminasi_reusable_apd',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengadaan_alat_pelindung_diri',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_personel',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_program_kesehatan_kerja',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_rekrutmen_pelatihan_dan_kompetensi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_sertifikasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_simulasi_dan_pelatihan_tanggap_darurat',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_suksesi_dan_eksklusi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_vaksinasi',
            field=models.TextField(default='Isi Laporan'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_validasi',
            field=models.TextField(default='Isi Laporan'),
        ),
    ]
