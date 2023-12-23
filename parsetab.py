
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BREAK COMA DIVISION DO ELSE FALSE FLOAT GE GT ID IF IGUAL IGUALES INT LCORCHETE LE LLLAVE LPAREN LT MAS MENOS MULTIPLICACION NE NOT NUMERO OR PUNTOYCOMA RCORCHETE REAL RLLAVE RPAREN TRUE WHILE programa : bloque  bloque : LLLAVE decls instrs RLLAVE \n    decls : decls decl\n          | epsilon\n\n    epsilon : \n    decl : tipo ID PUNTOYCOMA\n\n    \n    tipo : tipo LCORCHETE NUMERO RCORCHETE\n         | basico\n\n    \n    basico : INT\n           | FLOAT\n\n    \n    instrs : instrs instr\n           | epsilon\n\n    \n    instr : loc IGUAL bool PUNTOYCOMA\n         | IF LPAREN bool RPAREN instr\n         | IF LPAREN bool RPAREN instr ELSE instr\n         | WHILE LPAREN bool RPAREN instr\n         | DO instr WHILE LPAREN bool RPAREN PUNTOYCOMA\n         | BREAK PUNTOYCOMA\n         | bloque\n\n    \n    loc : loc LCORCHETE bool RCORCHETE\n        | ID\n\n    \n    bool : bool OR comb\n         | comb\n\n    \n    comb : comb AND igualdad\n         | igualdad\n\n    \n    igualdad : igualdad IGUALES rel\n             | igualdad NE rel\n             | rel\n\n    \n    rel : expr LT expr\n        | expr LE expr\n        | expr GE expr\n        | expr GT expr\n        | expr\n\n    \n    expr : expr MAS term\n         | expr MENOS term\n         | term\n\n    \n    term : term MULTIPLICACION unario\n         | term DIVISION unario\n         | unario\n\n    \n    unario : NOT unario\n           | MENOS unario\n           | factor\n           \n    \n    factor : LPAREN bool RPAREN\n           | loc\n           | NUMERO\n           | REAL\n           | TRUE\n           | FALSE\n    '
    
_lr_action_items = {'LLLAVE':([0,3,4,5,6,7,8,13,14,18,20,29,30,53,70,71,86,87,89,91,92,],[3,-5,-5,-4,3,-3,-12,-2,-11,3,-19,-18,-6,-13,3,3,-14,-16,3,-15,-17,]),'$end':([1,2,13,],[0,-1,-2,]),'INT':([3,4,5,7,30,],[-5,11,-4,-3,-6,]),'FLOAT':([3,4,5,7,30,],[-5,12,-4,-3,-6,]),'RLLAVE':([3,4,5,6,7,8,13,14,20,29,30,53,86,87,91,92,],[-5,-5,-4,13,-3,-12,-2,-11,-19,-18,-6,-13,-14,-16,-15,-17,]),'IF':([3,4,5,6,7,8,13,14,18,20,29,30,53,70,71,86,87,89,91,92,],[-5,-5,-4,16,-3,-12,-2,-11,16,-19,-18,-6,-13,16,16,-14,-16,16,-15,-17,]),'WHILE':([3,4,5,6,7,8,13,14,18,20,28,29,30,53,70,71,86,87,89,91,92,],[-5,-5,-4,17,-3,-12,-2,-11,17,-19,51,-18,-6,-13,17,17,-14,-16,17,-15,-17,]),'DO':([3,4,5,6,7,8,13,14,18,20,29,30,53,70,71,86,87,89,91,92,],[-5,-5,-4,18,-3,-12,-2,-11,18,-19,-18,-6,-13,18,18,-14,-16,18,-15,-17,]),'BREAK':([3,4,5,6,7,8,13,14,18,20,29,30,53,70,71,86,87,89,91,92,],[-5,-5,-4,19,-3,-12,-2,-11,19,-19,-18,-6,-13,19,19,-14,-16,19,-15,-17,]),'ID':([3,4,5,6,7,8,9,10,11,12,13,14,18,20,24,25,26,27,29,30,39,41,43,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,86,87,89,91,92,],[-5,-5,-4,21,-3,-12,22,-8,-9,-10,-2,-11,21,-19,21,21,21,21,-18,-6,21,21,21,-7,-13,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-14,-16,21,-15,-17,]),'LCORCHETE':([9,10,11,12,15,21,32,52,69,],[23,-8,-9,-10,25,-21,25,-7,-20,]),'ELSE':([13,20,29,53,86,87,91,92,],[-2,-19,-18,-13,89,-16,-15,-17,]),'IGUAL':([15,21,69,],[24,-21,-20,]),'LPAREN':([16,17,24,25,26,27,39,41,43,51,54,55,56,57,58,59,60,61,62,63,64,65,72,],[26,27,43,43,43,43,43,43,43,72,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'PUNTOYCOMA':([19,21,22,32,33,34,35,36,37,38,40,42,44,45,46,47,66,67,69,73,74,75,76,77,78,79,80,81,82,83,84,85,90,],[29,-21,30,-44,53,-23,-25,-28,-33,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,-22,-24,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,92,]),'MULTIPLICACION':([21,32,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,64,-39,-42,-45,-46,-47,-48,-41,-40,-20,64,64,-37,-38,-43,]),'DIVISION':([21,32,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,65,-39,-42,-45,-46,-47,-48,-41,-40,-20,65,65,-37,-38,-43,]),'LT':([21,32,37,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,58,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,-34,-35,-37,-38,-43,]),'LE':([21,32,37,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,59,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,-34,-35,-37,-38,-43,]),'GE':([21,32,37,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,60,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,-34,-35,-37,-38,-43,]),'GT':([21,32,37,38,40,42,44,45,46,47,66,67,69,81,82,83,84,85,],[-21,-44,61,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,-34,-35,-37,-38,-43,]),'MAS':([21,32,37,38,40,42,44,45,46,47,66,67,69,77,78,79,80,81,82,83,84,85,],[-21,-44,62,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,62,62,62,62,-34,-35,-37,-38,-43,]),'MENOS':([21,24,25,26,27,32,37,38,39,40,41,42,43,44,45,46,47,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,72,77,78,79,80,81,82,83,84,85,],[-21,39,39,39,39,-44,63,-36,39,-39,39,-42,39,-45,-46,-47,-48,39,39,39,39,39,39,39,39,39,39,39,39,-41,-40,-20,39,63,63,63,63,-34,-35,-37,-38,-43,]),'IGUALES':([21,32,35,36,37,38,40,42,44,45,46,47,66,67,69,74,75,76,77,78,79,80,81,82,83,84,85,],[-21,-44,56,-28,-33,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,56,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,]),'NE':([21,32,35,36,37,38,40,42,44,45,46,47,66,67,69,74,75,76,77,78,79,80,81,82,83,84,85,],[-21,-44,57,-28,-33,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,57,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,]),'AND':([21,32,34,35,36,37,38,40,42,44,45,46,47,66,67,69,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-21,-44,55,-25,-28,-33,-36,-39,-42,-45,-46,-47,-48,-41,-40,-20,55,-24,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,]),'OR':([21,32,33,34,35,36,37,38,40,42,44,45,46,47,48,49,50,66,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,88,],[-21,-44,54,-23,-25,-28,-33,-36,-39,-42,-45,-46,-47,-48,54,54,54,-41,-40,54,-20,-22,-24,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,54,]),'RCORCHETE':([21,31,32,34,35,36,37,38,40,42,44,45,46,47,48,66,67,69,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-21,52,-44,-23,-25,-28,-33,-36,-39,-42,-45,-46,-47,-48,69,-41,-40,-20,-22,-24,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,]),'RPAREN':([21,32,34,35,36,37,38,40,42,44,45,46,47,49,50,66,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,88,],[-21,-44,-23,-25,-28,-33,-36,-39,-42,-45,-46,-47,-48,70,71,-41,-40,85,-20,-22,-24,-26,-27,-29,-30,-31,-32,-34,-35,-37,-38,-43,90,]),'NUMERO':([23,24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[31,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'NOT':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'REAL':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TRUE':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FALSE':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque':([0,6,18,70,71,89,],[2,20,20,20,20,20,]),'decls':([3,],[4,]),'epsilon':([3,4,],[5,8,]),'instrs':([4,],[6,]),'decl':([4,],[7,]),'tipo':([4,],[9,]),'basico':([4,],[10,]),'instr':([6,18,70,71,89,],[14,28,86,87,91,]),'loc':([6,18,24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,89,],[15,15,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,15,15,32,15,]),'bool':([24,25,26,27,43,72,],[33,48,49,50,68,88,]),'comb':([24,25,26,27,43,54,72,],[34,34,34,34,34,73,34,]),'igualdad':([24,25,26,27,43,54,55,72,],[35,35,35,35,35,35,74,35,]),'rel':([24,25,26,27,43,54,55,56,57,72,],[36,36,36,36,36,36,36,75,76,36,]),'expr':([24,25,26,27,43,54,55,56,57,58,59,60,61,72,],[37,37,37,37,37,37,37,37,37,77,78,79,80,37,]),'term':([24,25,26,27,43,54,55,56,57,58,59,60,61,62,63,72,],[38,38,38,38,38,38,38,38,38,38,38,38,38,81,82,38,]),'unario':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[40,40,40,40,66,67,40,40,40,40,40,40,40,40,40,40,40,83,84,40,]),'factor':([24,25,26,27,39,41,43,54,55,56,57,58,59,60,61,62,63,64,65,72,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> bloque','programa',1,'p_programa','Sintactico.py',7),
  ('bloque -> LLLAVE decls instrs RLLAVE','bloque',4,'p_bloque','Sintactico.py',12),
  ('decls -> decls decl','decls',2,'p_decls','Sintactico.py',16),
  ('decls -> epsilon','decls',1,'p_decls','Sintactico.py',17),
  ('epsilon -> <empty>','epsilon',0,'p_empty','Sintactico.py',22),
  ('decl -> tipo ID PUNTOYCOMA','decl',3,'p_decl','Sintactico.py',27),
  ('tipo -> tipo LCORCHETE NUMERO RCORCHETE','tipo',4,'p_tipo','Sintactico.py',33),
  ('tipo -> basico','tipo',1,'p_tipo','Sintactico.py',34),
  ('basico -> INT','basico',1,'p_basico','Sintactico.py',40),
  ('basico -> FLOAT','basico',1,'p_basico','Sintactico.py',41),
  ('instrs -> instrs instr','instrs',2,'p_instrs','Sintactico.py',47),
  ('instrs -> epsilon','instrs',1,'p_instrs','Sintactico.py',48),
  ('instr -> loc IGUAL bool PUNTOYCOMA','instr',4,'p_instr','Sintactico.py',54),
  ('instr -> IF LPAREN bool RPAREN instr','instr',5,'p_instr','Sintactico.py',55),
  ('instr -> IF LPAREN bool RPAREN instr ELSE instr','instr',7,'p_instr','Sintactico.py',56),
  ('instr -> WHILE LPAREN bool RPAREN instr','instr',5,'p_instr','Sintactico.py',57),
  ('instr -> DO instr WHILE LPAREN bool RPAREN PUNTOYCOMA','instr',7,'p_instr','Sintactico.py',58),
  ('instr -> BREAK PUNTOYCOMA','instr',2,'p_instr','Sintactico.py',59),
  ('instr -> bloque','instr',1,'p_instr','Sintactico.py',60),
  ('loc -> loc LCORCHETE bool RCORCHETE','loc',4,'p_loc','Sintactico.py',66),
  ('loc -> ID','loc',1,'p_loc','Sintactico.py',67),
  ('bool -> bool OR comb','bool',3,'p_bool','Sintactico.py',73),
  ('bool -> comb','bool',1,'p_bool','Sintactico.py',74),
  ('comb -> comb AND igualdad','comb',3,'p_comb','Sintactico.py',80),
  ('comb -> igualdad','comb',1,'p_comb','Sintactico.py',81),
  ('igualdad -> igualdad IGUALES rel','igualdad',3,'p_igualdad','Sintactico.py',87),
  ('igualdad -> igualdad NE rel','igualdad',3,'p_igualdad','Sintactico.py',88),
  ('igualdad -> rel','igualdad',1,'p_igualdad','Sintactico.py',89),
  ('rel -> expr LT expr','rel',3,'p_rel','Sintactico.py',95),
  ('rel -> expr LE expr','rel',3,'p_rel','Sintactico.py',96),
  ('rel -> expr GE expr','rel',3,'p_rel','Sintactico.py',97),
  ('rel -> expr GT expr','rel',3,'p_rel','Sintactico.py',98),
  ('rel -> expr','rel',1,'p_rel','Sintactico.py',99),
  ('expr -> expr MAS term','expr',3,'p_expr','Sintactico.py',105),
  ('expr -> expr MENOS term','expr',3,'p_expr','Sintactico.py',106),
  ('expr -> term','expr',1,'p_expr','Sintactico.py',107),
  ('term -> term MULTIPLICACION unario','term',3,'p_term','Sintactico.py',113),
  ('term -> term DIVISION unario','term',3,'p_term','Sintactico.py',114),
  ('term -> unario','term',1,'p_term','Sintactico.py',115),
  ('unario -> NOT unario','unario',2,'p_unario','Sintactico.py',121),
  ('unario -> MENOS unario','unario',2,'p_unario','Sintactico.py',122),
  ('unario -> factor','unario',1,'p_unario','Sintactico.py',123),
  ('factor -> LPAREN bool RPAREN','factor',3,'p_factor','Sintactico.py',129),
  ('factor -> loc','factor',1,'p_factor','Sintactico.py',130),
  ('factor -> NUMERO','factor',1,'p_factor','Sintactico.py',131),
  ('factor -> REAL','factor',1,'p_factor','Sintactico.py',132),
  ('factor -> TRUE','factor',1,'p_factor','Sintactico.py',133),
  ('factor -> FALSE','factor',1,'p_factor','Sintactico.py',134),
]
