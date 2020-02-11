#RESPOSIBILITTIES
1. Konsumen bisa melakukan      => beliBarang, beliMakanan, negosiasiHarga, pesanBarang, pesanMakanan
2. Distributor bisa melakukan   => beliBarang, beliMakanan, negosiasiHarga, pesanBarang, pesanMakanan, dapatCashback
                                   jualBarang, jualMakanan, dropBarang, dropMakanan  
3. Produsen bisa melakukan      => jualBarang, jualMakanan, negosiasiHarga, menolakPesanan

#COLLABORATORS
beliBarang, beliMakanan, negosiasiHarga, pesanBarang, pesanMakanan == Konsumen & Distributor

beliBarang, beliMakanan, negosiasiHarga, pesanBarang, pesanMakanan, jualBarang, jualMakanan == Distributor & Produsen