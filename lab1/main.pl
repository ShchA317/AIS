/* 
Библейская родословная от Адама и Евы до Ноя и его сыновей

*/
  
% rules
married(Husband, Wife) :- Husband @< Wife, married(Wife, Husband). 
husband(Husband, Wife) :- male(Husband), married(Husband, Wife).
wife(Wife, Husband) :- female(Wife), married(Wife, Husband). 
father(Father, Child) :- male(Father), parent(Father, Child). 
mother(Mother, Child) :- female(Mother), parent(Mother, Child).
child(Child, Parent) :- parent(Parent, Child). 
son(Child, Parent) :- male(Child), child(Child, Parent). 
daughter(Child, Parent) :- female(Child), child(Child, Parent). 
sibling(Child1, Child2) :- 
                            father(Father, Child1), father(Parent, Child2),
                            mother(Mother, Child1), mother(Mother, Child2),
                            Child1 \= Child2. 
brother(Brother, Child) :- male(Brother), sibling(Brother, Child). 
sister(Sister, Child) :- female(Sister), sibling(Sister, Child). 
grandparent(Grandp, Child) :- parent(Grandp, Parent),  parent(Parent, Child).
grandfather(Grandf, Child) :- male(Grandf), grandparent(Grandf, Child).  
grandmother(Grandm, Child) :- female(Grandm), grandparent(Grandm, Child). 
grandchild(Child, Grandp) :- grandparent(Grandp, Child). 
grandson(Child, Grandp) :- male(Child), grandchild(Child, Grandp). 
granddaughter(Child, Grandp) :- female(Child), grandchild(Child, Grandp). 
uncle(Uncle, Child) :- male(Uncle), auntoruncle(Uncle, Child). 
predecessor(X,Y) :- parent(X,Y).
predecessor(X,Y) :- parent(X,Z), predecessor(Z,Y).

%facts
male('Адам').
female('Ева').
married('Адам','Ева').

male('Авель').
parent('Адам','Авель').
parent('Ева','Авель').

% Ветвь со стороны Сифа
male('Сиф').
parent('Адам','Сиф').
parent('Ева','Сиф').
female('Азура').
married('Сиф','Азура').

male('Енос').
parent('Сиф','Енос').
parent('Азура','Енос').

male('Каинан').
parent('Енос','Каинан').

male('Малелеил').
parent('Каинан','Малелеил').

male('Иаред').
parent('Малелеил','Иаред').

male('Енох').
parent('Иаред','Енох').

male('Мафусаил').
parent('Енох','Мафусаил').

male('Ламех').
parent('Мафусаил','Ламех').

male('Ной').
parent('Ламех','Ной').

male('Сим').
parent('Ной','Сим').

male('Хам').
parent('Ной','Хам').

male('Иафет').
parent('Ной','Иафет').

% Ветвь со стороны Каина
male('Каин').
parent('Адам','Каин').
parent('Ева','Каин').

male('Энох').
parent('Каин','Энох').

male('Ирад').
parent('Энох','Ирад').

male('Мехиаэль').
parent('Ирад','Мехиаэль').

male('Мафусал').
parent('Мехиаэль','Мафусал').

male('Лемех').
parent('Мафусал','Лемех').
female('Ада').
married('Лемех','Ада').
female('Цилла').
married('Лемех','Цилла').

male('Иувал').
parent('Лемех','Иувал').
parent('Ада','Иувал').

male('Иавал').
parent('Лемех','Иавал').
parent('Ада','Иавал').

male('Тубал-Каин').
parent('Лемех','Тубал-Каин').
parent('Цилла','Тубал-Каин').

female('Ноема').
parent('Лемех','Ноема').
parent('Цилла','Ноема').
