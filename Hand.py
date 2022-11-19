import Card


class Hand:
  def __init__(self, cards):
      self.cards = cards
  def __repr__(self):
      return ' '.join([str(card) for card in self.cards])


  def __len__(self):
      return len(self.cards)


  def add(self, card: Card):
      """ Добавить карту в КОНЕЦ списка. """
      self.cards.append(card)


  def counts(self):
    self.count_tem = 0
    self.count_sas = 0
    self.count_kl = 0
    self.count_ln = 0
    self.count_kn = 0
    self.count_yn = 0
    self.count_pu = 0
    self.count_sr = 0
    for s in self.cards:
      if repr(s) == 'темпура':
        self.count_tem += 1
      if repr(s) == 'сасими':
        self.count_sas += 1
      if repr(s) == 'клёцки':
        self.count_kl += 1
      if repr(s) == 'лосось нигири':
        self.count_ln += 1
      if repr(s) == 'кальмар нигири':
        self.count_kn += 1
      if repr(s) == 'яйцо нигири':
        self.count_yn += 1
      if repr(s) == 'пудинг':
        self.count_pu += 1
      if repr(s) == 'суси ролл':
        self.count_sr += 1
    return self.count_tem, self.count_sas, self.count_kl, self.count_ln, self.count_kn, self.count_yn, self.count_pu, self.count_sr


  def points(self):
    self.counts()
    self.point = 0
    self.point += (self.count_tem // 2) * 5
    self.point += (self.count_sas // 3) * 10
    if self.count_kl == 1:
      self.point += 1
    if self.count_kl == 2:
      self.point += 3
    if self.count_kl == 3:
      self.point += 6
    if self.count_kl == 4:
      self.point += 10
    if self.count_kl >= 5:
      self.point += 15
    self.point += self.count_ln * 2
    self.point += self.count_kn * 3
    self.point += self.count_yn * 1
    return  self.point