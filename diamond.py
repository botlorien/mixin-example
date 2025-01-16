#%%
class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


#%%
class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


#%%
class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


#%%
class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


#%%
class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()

#%%
u = U()
u.ping()

#%%
class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        return super().ping()

#%%
leaf2 = LeafUA()
leaf2.ping()

#%%
LeafUA.__mro__
# %%
leaf1 = Leaf()

# %%
leaf1

# %%
leaf1.ping()

# %%
leaf1.pong()

# %%
Leaf.__mro__


