import Card


class Hand:
  def __init__(self, cards):
      self.cards = cards


  def __repr__(self):
    return self.cards


  def __len__(self):
      return len(self.cards)


  def add(self, card: Card):
      """ Добавить карту в КОНЕЦ списка. """
      self.cards += ' ' + repr(card)


  def counts(self):
    self.count_tem = self.cards.count('темпура')
    self.count_sas = self.cards.count('сасими')
    self.count_kl = self.cards.count('клёцки')
    self.count_ln = self.cards.count('лосось_нигири')
    self.count_kn = self.cards.count('кальмар_нигири')
    self.count_yn = self.cards.count('яйцо_нигири')
    self.count_pu = self.cards.count('пудинг')
    self.count_sr = self.cards.count('суси_ролл')
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