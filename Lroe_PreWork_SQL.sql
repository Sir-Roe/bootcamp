Drop Schema if exists boxbiz;
CREATE DATABASE `boxbiz`; 

DROP TABLE IF EXISTS boxbiz.`Accounts`;

CREATE TABLE boxbiz.`Accounts` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `name` varchar(255) default NULL,
  `region` varchar(50) default NULL,
  `City` varchar(255),
  `address` varchar(255) default NULL,
  `Subscriber` varchar(255) default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO boxbiz.`Accounts` (`name`,`region`,`City`,`address`,`Subscriber`)
VALUES
  ("Christian Clements","Florida","Pavlohrad","Ap #676-4227 Lacinia Ave","Y"),
  ("Shay Sullivan","Arizona","Thabazimbi","Ap #633-1696 Et St.","Y"),
  ("Libby Robles","Wisconsin","Volgograd","358-832 Eu Road","N"),
  ("Clarke Vaughan","Colorado","Montería","104-2988 Malesuada Av.","N"),
  ("Berk Boyd","Oregon","Funtua","P.O. Box 240, 5552 Est Avenue","Y"),
  ("Justin Nguyen","Ohio","Toledo","Ap #882-685 Nunc Avenue","Y"),
  ("Clinton Bowman","Colorado","Barranca","312-8138 Eleifend St.","N"),
  ("Yetta Duran","Maine","Columbus","Ap #803-6367 Sapien. Rd.","N"),
  ("Samantha Aguirre","Texas","Quimper","P.O. Box 232, 5481 Nisl St.","Y"),
  ("Stella Griffith","Virginia","Xuân Trường","P.O. Box 471, 8340 Aliquam Avenue","Y"),
  ("Reuben Richardson","Kentucky","Seletar","868-2064 Neque. Rd.","N"),
  ("Conan Walter","Pennsylvania","Colchane","4682 Duis Road","N"),
  ("Cara Ashley","Kansas","Siedlce","995-5119 Sed St.","N"),
  ("Shelby Browning","Missouri","Mukachevo","239-6419 Curabitur Road","Y"),
  ("Brenna Mccullough","Maine","Musina","3177 Magna. Ave","N"),
  ("Ryder Lowe","Wyoming","Hà Tĩnh","Ap #713-3664 Egestas Road","Y"),
  ("Unity Santana","Idaho","Madiun","Ap #126-3318 Quis Road","Y"),
  ("Len Mcneil","Vermont","Christchurch","Ap #705-8744 Nisi. Street","N"),
  ("Kirsten Kramer","Idaho","Campofelice di Fitalia","2724 Suspendisse Av.","N"),
  ("Meredith Sharp","Texas","Limón (Puerto Limón]","Ap #445-2807 Suspendisse St.","Y"),
  ("Jerry Lowe","Illinois","Calapan","386 Mi Rd.","N"),
  ("Zenia Hanson","Illinois","Bremen","Ap #433-2671 Tincidunt. Road","N"),
  ("Galena Wagner","Delaware","Aizwal","825-478 Consequat Rd.","Y"),
  ("Courtney Delaney","Maryland","Singkawang","7371 Cursus Rd.","Y"),
  ("Macon Freeman","Florida","San José de Alajuela","150-2029 Ac Rd.","Y"),
  ("Camilla Short","Utah","Tczew","Ap #307-9622 Mauris Avenue","Y"),
  ("Octavia Strong","Montana","Lim Chu Kang","184-3810 Quisque Road","N"),
  ("Jack Foley","Minnesota","Brandon","Ap #827-2456 Sapien, Road","N"),
  ("Eliana Conner","Wisconsin","Alajuela","Ap #795-4638 Tellus. Road","Y"),
  ("Wynne Carrillo","Oklahoma","Argyle","504-8259 Vel, St.","Y"),
  ("Kerry Hickman","Illinois","Agartala","P.O. Box 724, 8748 Nunc Av.","N"),
  ("Cherokee Christian","Iowa","Canberra","Ap #755-6195 Quis, St.","N"),
  ("Savannah Booth","Mississippi","Almere","717-3575 Enim Avenue","N"),
  ("Constance Gregory","Kansas","Belfast","633-2519 Vitae Ave","Y"),
  ("Octavius Hoover","Washington","Laramie","1869 Risus. Av.","Y"),
  ("Halee Glass","Colorado","Cupar","521-5623 Cum Road","N"),
  ("Ivan Bond","Ohio","Baardegem","443-8254 Suspendisse Rd.","Y"),
  ("Oliver Macdonald","Washington","Besançon","P.O. Box 658, 3794 Quisque Street","N"),
  ("Duncan Dyer","Illinois","Shaki","Ap #166-5784 Sagittis Road","N"),
  ("Florence Manning","Ohio","Anchorage","Ap #329-1564 Imperdiet Ave","Y"),
  ("Hasad Gross","Kentucky","Meppel","4267 Quis, Avenue","N"),
  ("Leslie Dale","Utah","Saravena","586-8759 Vehicula Ave","N"),
  ("Quynn Green","Wisconsin","Nelson","7571 Sociis Rd.","N"),
  ("Ginger Moran","Nevada","Berdychiv","P.O. Box 503, 4034 Montes, Rd.","Y"),
  ("Melyssa Montoya","Wyoming","Bharatpur","Ap #115-6466 Lorem Avenue","N"),
  ("Tashya Boyle","Kansas","Galway","770-349 Ac Road","N"),
  ("Dorian Weber","Oklahoma","Meerhout","9847 Ipsum Rd.","Y"),
  ("Ginger James","Ohio","Vidnoye","701-3618 Pellentesque Road","N"),
  ("Irma Saunders","Hawaii","Kimberley","Ap #611-4836 Ac St.","Y"),
  ("Warren Clayton","Kentucky","Bydgoszcz","690-5515 Suscipit Av.","Y");
  
  Select * from boxbiz.accounts where Subscriber = 'Y' and region <> 'Illinois';
