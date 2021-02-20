from datetime import datetime
from transfer.data.connoracle.connection import ConnOracle


class ExtractData(ConnOracle):

    def __init__(self, server=str, port=int, service_name=str, user=str, password=str):
        ConnOracle.__init__(self, server, port, service_name, user, password)

    def get_transactions(self, start=datetime, end=datetime):
        cursor = self.execute_query(f"""
            SELECT
                a.event_number,                                                 --numeroevento                    
                a.id_gare,                                                      --idgare                    
                a.shift_number,                                                 --turnoid                    
                a.voie,                                                         --lineacarril                    
                a.id_paiement,                                                  --tipopagoid
                a.mode_reglement,                                               --tipopagodesc
                a.matricule,                                                    --numerogea
                to_char(a.date_debut_poste, 'YYYY-MM-DD')             AS fechainic,         --fechaaperturaturno
                to_char(a.date_debut_poste, 'HH24:MI:SS')              AS horainic,           --horainicioturno
                to_char(a.date_transaction, 'YYYY-MM-DD')             AS fecha,             --fecha
                to_char(a.date_transaction, 'HH24:MI:SS')              AS hora,               --hora
                a.folio_ect,                                                    --folio
                a.indice_suite,                                                 --indicereclasificacion
                a.id_classe,                                                    --pre
                a.tab_id_classe,                                                --cajero
                a.acd_class,                                                    --post
                a.id_obs_tt,                                                    --observacionestt
                a.id_obs_mp,                                                    --observacionesmp
                a.id_obs_sequence,                                              --observacionessecuencia
                a.id_obs_passage,                                               --observacionespaso
                a.code_grille_tarif,                                            --numeroejes
                0                                                     AS anualado,                                                  --anualado
                ''                                                    AS comentarios,                                              --comentarios
                0                                                     AS capturado,                                                 --capturado
                a.contenu_iso,                                                  --numiave
                a.id_mode_voie,                                                 --carrilmodoid
                b.chemin_fichier                                      AS url_imagen,                                 --url_imagen
                b.information                                         AS placa,                                         --placa
                to_char(b.date_image, 'YYYY-MM-DD HH24:MI:SS')        AS fecha_imagen, --fechaimagen
                a.prix_total                                                    --prixtotal
            FROM
                transaction      a
                LEFT JOIN img_video_image  b ON ( a.voie = b.voie
                                                AND a.id_gare = b.id_gare
                                                AND to_char(a.date_transaction, 'YYYY-MM-DD HH24:MI:SS') = to_char(b.date_image, 'YYYY-MM-DD HH24:MI:SS') )
            WHERE
                a.date_transaction BETWEEN TO_DATE('22-10-2020 00:00:00', 'dd-mm-yyyy hh24:mi:ss') AND TO_DATE('04-12-2020 00:00:00', 'dd-mm-yyyy hh24:mi:ss')
                AND a.id_paiement = 15
                AND ( a.id_voie = '1'
                    OR a.id_voie = '2'
                    OR a.id_voie = '3'
                    OR a.id_voie = '4'
                    OR a.id_voie = 'X' )
            ORDER BY
                a.date_transaction ASC """)

        return cursor.fetchall()
