#-*-coding:utf-8 -*-

import os

class OrdrDict :
	""" a special type of dict , it's an ordred dict :
	so the ordre of given the keys is imporant , ze can also sort the dict
	"""

	def __init__(self , d = {} , **par) :
		if not d : #not dict given in cons (d is empty)
			if not par : #no arg given (par is empty)
				self._ky = []
				self._vl = []
			else :
				self._ky = list(par.keys())
				if len(set(self._ky)) < len(self._ky) : #double keys
					raise ValueError('keys most be different')
				else : 
					self._vl = list(par.values())
		elif not par : #no arg given (par is empty)
			self._ky = list(d.keys())
			self._vl = list(d.values())
		else :
			raise TypeError("give one of the arg : a dict or a couples of keys and values")
			

	def __repr__(self) :
		ln = len(self._ky)
		i = 0
		dc = {}
		ch = '{'

		while i < ln :
			ch += ' {} : {} ,'.format(self._ky[i] , self._vl[i])
			dc[ self._ky[i] ] = self._vl[i]
			i += 1

		ch = ch.strip(',')
		ch += '}'
		#print (dc)
		return (ch)

	def exists(self , val) :
		""" check if the val given exists in keys list
		return the index of the key in the keys list if it exists
		return -1 if not
		"""
		try :
			nx = self._ky.index(val)
		except ValueError :
			return -1
		else :
			return nx

	def __getitem__(self , indx) :
		"""try :
			nx = self._ky.index(indx)
		except ValueError :
			print('THE KEY "{}"" DOESN\'T EXIST IN THE DICT'.format(indx))
			return ''
		"""
		nx = self.exists(indx)
		if nx == -1 :
			raise ValueError('THE KEY "{}"" DOESN\'T EXIST IN THE DICT'.format(indx))
		else :
			return self._vl[nx]

	def __setitem__(self , indx , val) :
		nx = self.exists(indx)
		if nx == -1 :
			self._ky.append(indx)
			self._vl.append(val)
		else :
			self._vl[nx] = val

	def __delitem__(self , indx) :
		nx = self.exists(indx)
		if nx == -1 :
			raise ValueError('THE KEY "{}"" DOESN\'T EXIST IN THE DICT'.format(indx))
		else :
			del self._ky[nx]
			del self._vl[nx]

	def __len__(self) :
		return len(self._ky)

	def __contains__(self , indx) :
		nx = self.exists(indx)
		if nx == -1 :
			return False
		else :
			return True

	""" ******************************************************************************** """
	def __add__(self , obj) :
		cls = OrdrDict
		if isinstance(obj , cls) :
			self._ky.extend(obj._ky)
			self._vl.extend(obj._vl)
		else :
			raise TypeError('UNSUPPORTED OPERAND ! YOU SHOULD GIVE A {} OBJECT AS OPERAND'.format(cls))

	def __iter__(self) :
		self.posIter = 0
		return self

	def __next__(self) :
		if self.posIter < len(self._ky) :
			self.posIter += 1
			return self._ky[self.posIter - 1]
		else :
			raise StopIteration

	""" ***************************************************************************** """
	'''def _generator() :
		n = 0
		ln = len(self._ky)
		while n < ln :
			yield self._ky[n]
	'''
	def keys(self) :
		return self._ky

	def values(self) :
		return self._vl

	def items(self) :
		ln = len(self._ky)
		lst = []
		for i in range(ln) :
			lst.append( ( self._ky[i] , self._vl[i] ) )

		return lst

	def sort(self) :
		itemsLst = self.items()
		#we sort the list of couple (key , value)
		itemsLst.sort(key = lambda x : x[1] ) 
		#then we create the new OrdrDict from the sorted list 
		kyLst = []
		vlLst = []
		for i in itemsLst :
			kyLst.append(i[0])
			vlLst.append(i[1])

		self._ky = kyLst
		self._vl = vlLst

	def reverse(self) :
		i = len(self._ky)
		kyLst = []
		vlLst = []
		
		while i > 0 :
			kyLst.append(self._ky[i - 1])
			vlLst.append(self._vl[i - 1])
			i -= 1

		self._ky = kyLst
		self._vl = vlLst