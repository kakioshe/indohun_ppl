# Generated by Django 3.0.6 on 2020-06-11 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200514_0509'),
        ('blog', '0009_auto_20200610_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_dua',
            new_name='keterangan_APD_personel',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_empat',
            new_name='keterangan_GMT_peralatan',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_enam',
            new_name='keterangan_GMT_personel',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_lima',
            new_name='keterangan_dekontaminasi_dan_disinfeksi_peralatan',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_satu',
            new_name='keterangan_general_safety',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='keterangan_tiga',
            new_name='keterangan_identifikasi_hazard',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_dua',
            new_name='keterangan_identifikasi_perencanaan_dan_respon_keadaan_darurat',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_empat',
            new_name='keterangan_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_enam',
            new_name='keterangan_infrastruktur_dan_operasional',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_lima',
            new_name='keterangan_inspeksi_dan_audit',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_satu',
            new_name='keterangan_inventarisasi_informasi_dan_pencatatan',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='rekomendasi_tiga',
            new_name='keterangan_investigasi_kecelakaan_dan_insiden',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_dua',
            new_name='nilai_no_1',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_empat',
            new_name='nilai_no_10',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_enam',
            new_name='nilai_no_11',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_lima',
            new_name='nilai_no_12',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_satu',
            new_name='nilai_no_13',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='nilai_tiga',
            new_name='nilai_no_14',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='afiliasi_penilai',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='jenis_penilaian',
            field=models.CharField(blank=True, choices=[('Penilaian Mandiri (Self Assessment)', 'Penilaian Mandiri (Self Assessment)'), ('Penilaian Pendampingan (Technical Assessment)', 'Penilaian Pendampingan (Technical Assessment)')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kalibrasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_keamanan_fisik_dan_pengendalian_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_keamanan_informasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kebijakan_sistem_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kedaruratan_medik',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_komunikasi_dan_konsultasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_kontraktor_dan_suplier_purchasing',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_latar_belakang_sdm',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_manajemen_pemeliharaan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_monitoring_peralatan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pelabelan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pemeliharaan_dan_dekontaminasi_reusable_apd',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pencatatan_dokumen_dan_pengendalian_dokumen',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengadaan_alat_pelindung_diri',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengembangan_berkelanjutan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_dan_monitoring',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_ketidaksesuaian_dan_perbaikan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengendalian_risiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_peran_dan_tanggung_jawab',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_perencanaan_dan_program_kerja',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_persyaratan_legal_aturan_atau_izin',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_perubahan_terkait_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_program_kesehatan_kerja',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_rekrutmen_pelatihan_dan_kompetensi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_review_dan_perbaikan_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_ruang_lingkup_dan_penjadwalan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_sertifikasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_simulasi_dan_pelatihan_tanggap_darurat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_suksesi_dan_eksklusi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_tanggung_jawab_dan_wewenang',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_tujuan_dan_program_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_vaksinasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='keterangan_validasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='laboratorium_yang_dinilai',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_15',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_16',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_17',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_18',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_19',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_2',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_20',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_21',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_22',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_23',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_24',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_25',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_26',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_27',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_28',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_29',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_3',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_30',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_31',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_32',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_33',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_34',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_35',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_36',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_37',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_38',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_39',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_4',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_40',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_41',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_42',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_43',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_44',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_45',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_46',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_47',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_48',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_49',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_5',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_50',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_51',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_52',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_53',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_54',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_6',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_7',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_8',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nilai_no_9',
            field=models.IntegerField(choices=[(4, 4), (3, 3), (2, 2), (1, 1)], default=4),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='penilai',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='personel_yang_diwawancarai',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_APD_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_GMT_peralatan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_GMT_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_dekontaminasi_dan_disinfeksi_peralatan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_general_safety',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_identifikasi_hazard',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_identifikasi_perencanaan_dan_respon_keadaan_darurat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_infrastruktur_dan_operasional',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_inspeksi_dan_audit',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_inventarisasi_informasi_dan_pencatatan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_investigasi_kecelakaan_dan_insiden',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kalibrasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_keamanan_fisik_dan_pengendalian_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_keamanan_informasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kebijakan_sistem_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kedaruratan_medik',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_komunikasi_dan_konsultasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_kontraktor_dan_suplier_purchasing',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_latar_belakang_sdm',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_manajemen_pemeliharaan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_monitoring_peralatan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pelabelan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pemeliharaan_dan_dekontaminasi_reusable_apd',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pencatatan_dokumen_dan_pengendalian_dokumen',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengadaan_alat_pelindung_diri',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengembangan_berkelanjutan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_dan_monitoring',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_ketidaksesuaian_dan_perbaikan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_personel',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengendalian_risiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_peran_dan_tanggung_jawab',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_perencanaan_dan_program_kerja',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_persyaratan_legal_aturan_atau_izin',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_perubahan_terkait_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_program_kesehatan_kerja',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_rekrutmen_pelatihan_dan_kompetensi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_review_dan_perbaikan_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_ruang_lingkup_dan_penjadwalan',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_sertifikasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_simulasi_dan_pelatihan_tanggap_darurat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_suksesi_dan_eksklusi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_tanggung_jawab_dan_wewenang',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_tujuan_dan_program_manajemen_biorisiko',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_vaksinasi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='rekomendasi_validasi',
            field=models.TextField(blank=True),
        ),
    ]
