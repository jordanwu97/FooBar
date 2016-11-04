#Blossom Algroithm

#UnionFind Data Structure for blossom contractions

#Let G be Graph such that:
#iter(G) => 
#G[v] => list of vertices connected to v

#Find AugmentingPath(G,M)
	#Empty Forest F

	#Set exposed edges from previous matching M as root of tree
		#Add tree to Forest F

	#At odd levels (dist to root % 2 = 0) take vertex v
		#When there exists edge e that connect v and neighbor w
			#If w does not exist in forest F
				#Grab x, the vertex matched with w in previous matching M
				#Edges {v,w} {w,x} added to forest
			
			#If w is already in forest F
				#If distance to root of w is even:
					#If root(v) != root(w):
						#found an augmented path root(v)-=-=v-w=-=-root(w)
						#return the augmented path
					#If root(v) == root(w):
						#B = blossom formed by e
						#G' , M' contract G and M
						#P' <- recusively find augmenting path AugmentingPath(G',M')
						#P <- whatever augmenting path returned by P'

	#