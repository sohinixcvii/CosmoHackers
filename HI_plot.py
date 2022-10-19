import numpy as np
import matplotlib.pyplot as plt

for i in range(0,1):
    filename='HI_map_'+str(i)
    f = open('ionz_out/'+filename) #path to map
    N = np.fromfile(f, count=3,dtype='int32')
    N1,N2,N3 = N
    print(N1,N2,N3)
    l = np.fromfile(f, count=1, dtype='float32')
    print(l)
    data = np.fromfile(f,dtype='float32',count=N1*N2*N3)

#--------------------binarizing--------------------------------------------
    for n in range(len(data)):
        if data[n]>0.01:
            data[n]=0.5
        else:
            data[n]=0
#----------------------end of binarizing----------------------------------

    f.close()
    data = np.reshape(data, (N1,N2,N3), order='C')


    index = np.random.randint(low=0,high=N1,count=5)
    image = data[index,:,:]
    im_i=0
    for im in image:
        fig, ax = plt.subplots(figsize=(5,5))
        #levels = [0,5,10,15,20,25,30,35,40,45,50]
        im = ax.imshow(im,cmap='turbo',interpolation='gaussian',origin='lower')
        #, interpolation='gaussian', origin='lower', levels=levels
        # yloc=[0,8,16,24,32,40,48,56,64]
        # ylab=[el*2.24 for el in yloc]
        # y=['{:.2f}'.format(el) for el in ylab]
        # xloc=[0,8,16,24,32,40,48,56,64]
        # xlab=[el*2.24 for el in xloc]
        # x=['{:.2f}'.format(el) for el in xlab]
        # for el in ylab:
        #     el=int(el)
        #     y.append(str(el))
        # for el in xlab:
        #     el=int(el)
        #     x.append(str(el))
        # plt.colorbar(im, location='top', label='mK')
        # plt.format(grid=False, xlabel='Mpc', ylabel='Mpc',yticklabels=y,xticklabels=x,title="HI map at redshift 7.0"
        #           ,xlocator=xloc,ylocator=yloc)
        #ax.set_xticks(xloc)
        # ax.set_xticklabels(x)
        #ax.set_yticks(yloc)
        # ax.set_yticklabels(y)
        # ax.set_xlabel('Mpc')
        # ax.set_ylabel('Mpc')
        filename= filename+'_'+str(index[im_i])+'.png'
        im_i=im_i+1
        plt.Figure.savefig(fig,filename,bbox_inches='tight')
