
# coding: utf-8

# In[90]:

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 

from matplotlib.ticker import NullFormatter

m3032,m5032,m7032,mbcg32 = np.loadtxt('032_BH2015_DirectProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)
m3041,m5041,m7041,mbcg41 = np.loadtxt('041_BH2015_DirectProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)
m3091,m5091,m7091,mbcg91 = np.loadtxt('091_BH2015_BiasedProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)

_m3032,_m5032,_m7032,_mbcg32 = np.loadtxt('032_BH2015_BiasedProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)
_m3041,_m5041,_m7041,_mbcg41 = np.loadtxt('041_BH2015_BiasedProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)
_m3091,_m5091,_m7091,_mbcg91 = np.loadtxt('091_BH2015_BiasedProgenitor_Masses.txt',usecols=[8,9,10,11], unpack=True)


# In[26]:

#m(r<0.1r500)
median032mbcg=np.median(mbcg32)
median041mbcg=np.median(mbcg41)
median091mbcg=np.median(mbcg91)
max032mbcg=np.max(mbcg32)
max041mbcg=np.max(mbcg41)
max091mbcg=np.max(mbcg91)
min032mbcg=np.min(mbcg32)
min041mbcg=np.min(mbcg41)
min091mbcg=np.min(mbcg91)
#m(r<30)
median032m30=np.median(m3032)
median041m30=np.median(m3041)
median091m30=np.median(m3091)
max032m30=np.max(m3032)
max041m30=np.max(m3041)
max091m30=np.max(m3091)
min032m30=np.min(m3032)
min041m30=np.min(m3041)
min091m30=np.min(m3091)
#m(r<50)
median032m50=np.median(m5032)
median041m50=np.median(m5041)
median091m50=np.median(m5091)
max032m50=np.max(m5032)
max041m50=np.max(m5041)
max091m50=np.max(m5091)
min032m50=np.min(m5032)
min041m50=np.min(m5041)
min091m50=np.min(m5091)
#m(r<70)
median032m70=np.median(m7032)
median041m70=np.median(m7041)
median091m70=np.median(m7091)
max032m70=np.max(m7032)
max041m70=np.max(m7041)
max091m70=np.max(m7091)
min032m70=np.min(m7032)
min041m70=np.min(m7041)
min091m70=np.min(m7091)
#m(r<50_proj)
#median032m50pro=np.median(m50proj32)
#median041m50pro=np.median(m50proj41)
#median091m50pro=np.median(m50proj91)
#max032m50pro=np.max(m50proj32)
#max041m50pro=np.max(m50proj41)
#max091m50pro=np.max(m50proj91)
#min032m50pro=np.min(m50proj32)
#min041m50pro=np.min(m50proj41)
#min091m50pro=np.min(m50proj91)

redshifts = np.array([2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
mbcgs    = np.array([mbcg32,mbcg41,mbcg91])
m30s     = np.array([m3032,m3041,m3091])
m50s     = np.array([m5032,m5041,m5091])
m70s     = np.array([m7032,m7041,m7091])
#m50sproj = np.array([m50proj32,m50proj41,m50proj91])


# In[27]:

#m(r<0.1r500)
_median032mbcg=np.median(_mbcg32)
_median041mbcg=np.median(_mbcg41)
_median091mbcg=np.median(_mbcg91)
_max032mbcg=np.max(_mbcg32)
_max041mbcg=np.max(_mbcg41)
_max091mbcg=np.max(_mbcg91)
_min032mbcg=np.min(_mbcg32)
_min041mbcg=np.min(_mbcg41)
_min091mbcg=np.min(_mbcg91)
#m(r<30)
_median032m30=np.median(_m3032)
_median041m30=np.median(_m3041)
_median091m30=np.median(_m3091)
_max032m30=np.max(_m3032)
_max041m30=np.max(_m3041)
_max091m30=np.max(_m3091)
_min032m30=np.min(_m3032)
_min041m30=np.min(_m3041)
_min091m30=np.min(_m3091)
#m(r<50)
_median032m50=np.median(_m5032)
_median041m50=np.median(_m5041)
_median091m50=np.median(_m5091)
_max032m50=np.max(_m5032)
_max041m50=np.max(_m5041)
_max091m50=np.max(_m5091)
_min032m50=np.min(_m5032)
_min041m50=np.min(_m5041)
_min091m50=np.min(_m5091)
#m(r<70)
_median032m70=np.median(_m7032)
_median041m70=np.median(_m7041)
_median091m70=np.median(_m7091)
_max032m70=np.max(_m7032)
_max041m70=np.max(_m7041)
_max091m70=np.max(_m7091)
_min032m70=np.min(_m7032)
_min041m70=np.min(_m7041)
_min091m70=np.min(_m7091)
#m(r<50_proj)
#_median032m50pro=np.median(_m50proj32)
#_median041m50pro=np.median(_m50proj41)
#_median091m50pro=np.median(_m50proj91)
#_max032m50pro=np.max(_m50proj32)
#_max041m50pro=np.max(_m50proj41)
#_max091m50pro=np.max(_m50proj91)
#_min032m50pro=np.min(_m50proj32)
#_min041m50pro=np.min(_m50proj41)
#_min091m50pro=np.min(_m50proj91)

_mbcgs    = np.array([_mbcg32,_mbcg41,_mbcg91])
_m30s     = np.array([_m3032,_m3041,_m3091])
_m50s     = np.array([_m5032,_m5041,_m5091])
_m70s     = np.array([_m7032,_m7041,_m7091])


# In[98]:

from matplotlib.offsetbox import AnchoredText

plt.rc('text', usetex=True)
font = {'family': 'serif', 'size': 35, 'serif': ['computer modern roman']}
plt.rc('font', **font)
plt.rc('legend', **{'fontsize': 27}) 
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['ytick.major.size'] = 6
plt.rcParams['ytick.minor.size'] = 3
mpl.rc('lines', linewidth=3)


# In[99]:

fig = plt.figure(figsize=(15,15))

#plot 1--------------------------------------------------------------------------------------------------------------------------------
ax1 = fig.add_subplot(221)
ax1.scatter([2.,1., 0.],[np.log10(median032mbcg),np.log10(median041mbcg),np.log10(median091mbcg)],marker='o',s=90, color='#810090', hatch="X", linewidth='1',alpha=0.7 )
ax1.plot([2.,1., 0.],[np.log10(median032mbcg),np.log10(median041mbcg),np.log10(median091mbcg)],color='#810090')
ax1.scatter([2.,1., 0.],[np.log10(_median032mbcg),np.log10(_median041mbcg),np.log10(_median091mbcg)],marker='o',s=90, color='#028957',linewidth='1',alpha=0.7 )
ax1.plot([2.,1., 0.],[np.log10(_median032mbcg),np.log10(_median041mbcg),np.log10(_median091mbcg)],color='#028957')

ax1.fill_between([2.,1., 0.], [np.log10(min032mbcg),np.log10(min041mbcg),np.log10(min091mbcg)], 
                 [np.log10(max032mbcg),np.log10(max041mbcg),np.log10(max091mbcg)],edgecolor='#810090',
                 hatch="/////", color='none', facecolor='none')
ax1.fill_between([2.,1., 0.], [np.log10(_min032mbcg),np.log10(_min041mbcg),np.log10(_min091mbcg)],
                 [np.log10(_max032mbcg),np.log10(_max041mbcg),np.log10(_max091mbcg)],alpha=0.4,edgecolor='#028957',
                 facecolor='#028957')

plt.text(0.2,11,'M$_{R<0.1R_{500}}$',horizontalalignment='left', verticalalignment='top',fontsize=50)
ax1.legend(loc='upper right', frameon=False, scatterpoints=1,borderpad=0.6, labelspacing=0.7)
ax1.set_xlabel('z')
ax1.set_ylabel('log M/M$_{\odot}$')
ax1.set_ylim(10.6,12.7)
ax1.set_xlim(-0.1,2.1)
ax1.xaxis.set_major_formatter(NullFormatter())
ax1.minorticks_on()

#plot 2--------------------------------------------------------------------------------------------------------------------------------
ax2 = fig.add_subplot(222)
ax2.scatter([2.,1., 0.],[np.log10(median032m30),np.log10(median041m30),np.log10(median091m30)],marker='o',s=90, color='#810090',linewidth='1',alpha=0.7 )
ax2.plot([2.,1., 0.],[np.log10(median032m30),np.log10(median041m30),np.log10(median091m30)],label='Progenitor Directo' ,color='#810090')
ax2.scatter([2.,1., 0.],[np.log10(_median032m30),np.log10(_median041m30),np.log10(_median091m30)],marker='o',s=90, color='#028957',linewidth='1',alpha=0.7 )
ax2.plot([2.,1., 0.],[np.log10(_median032m30),np.log10(_median041m30),np.log10(_median091m30)],label='Progenitor Sesgado',color='#028957')

ax2.fill_between([2.,1., 0.], [np.log10(min032m30),np.log10(min041m30),np.log10(min091m30)], 
                 [np.log10(max032m30),np.log10(max041m30),np.log10(max091m30)],edgecolor='#810090',
                 hatch="/////", color='none', facecolor='none')
ax2.fill_between([2.,1., 0.], [np.log10(_min032m30),np.log10(_min041m30),np.log10(_min091m30)],
                 [np.log10(_max032m30),np.log10(_max041m30),np.log10(_max091m30)],alpha=0.4,edgecolor='#028957', facecolor='#028957')

plt.text(0.2,11,'M$_{R<30Kpc}$',horizontalalignment='left', verticalalignment='top',fontsize=50)
ax2.legend(loc='upper right', frameon=False, scatterpoints=1,borderpad=0.6, labelspacing=0.7)
ax2.set_xlabel('z')
ax2.set_ylim(10.6,12.7)
ax2.set_xlim(-0.1,2.1)
ax2.yaxis.set_major_formatter(NullFormatter())
ax2.xaxis.set_major_formatter(NullFormatter())
ax2.minorticks_on()

#plot 3--------------------------------------------------------------------------------------------------------------------------------
ax3 = fig.add_subplot(223)
ax3.scatter([2.,1., 0.],[np.log10(median032m50),np.log10(median041m50),np.log10(median091m50)],marker='o',s=90, color='#810090',linewidth='1',alpha=0.7 )
ax3.plot([2.,1., 0.],[np.log10(median032m50),np.log10(median041m50),np.log10(median091m50)], color='#810090')

ax3.scatter([2.,1., 0.],[np.log10(_median032m50),np.log10(_median041m50),np.log10(_median091m50)],marker='o',s=90, color='#028957',linewidth='1',alpha=0.7 )
ax3.plot([2.,1., 0.],[np.log10(_median032m50),np.log10(_median041m50),np.log10(_median091m50)],color='#028957')

ax3.fill_between([2.,1., 0.], [np.log10(min032m50),np.log10(min041m50),np.log10(min091m50)],
                 [np.log10(max032m50),np.log10(max041m50),np.log10(max091m50)], edgecolor='#810090',
                 hatch="/////", color='none', facecolor='none')
ax3.fill_between([2.,1., 0.], [np.log10(_min032m50),np.log10(_min041m50),np.log10(_min091m50)],
                 [np.log10(_max032m50),np.log10(_max041m50),np.log10(_max091m50)],alpha=0.4,edgecolor='#028957', facecolor='#028957')

plt.text(0.2,11,'M$_{R<50Kpc}$',horizontalalignment='left', verticalalignment='top',fontsize=50)
ax3.legend(loc='upper right', frameon=False, scatterpoints=1,borderpad=0.6, labelspacing=0.7)
ax3.set_xlabel('z')
ax3.set_ylabel('log M/M$_{\odot}$')
ax3.set_ylim(10.6,12.7)
ax3.set_xlim(-0.1,2.1)
xticks3 = ax3.xaxis.get_major_ticks()
xticks3[1].label1.set_visible(False)
xticks3[-2].label1.set_visible(False)
ax3.minorticks_on()

#plot 4--------------------------------------------------------------------------------------------------------------------------------
ax4 = fig.add_subplot(224)
ax4.scatter([2.,1., 0.],[np.log10(median032m70),np.log10(median041m70),np.log10(median091m70)],marker='o',s=90, color='#810090',linewidth='1',alpha=0.7 )
ax4.plot([2.,1., 0.],[np.log10(median032m70),np.log10(median041m70),np.log10(median091m70)], color='#810090')

ax4.scatter([2.,1., 0.],[np.log10(_median032m70),np.log10(_median041m70),np.log10(_median091m70)],marker='o',s=90, color='#028957',linewidth='1',alpha=0.7 )
ax4.plot([2.,1., 0.],[np.log10(_median032m70),np.log10(_median041m70),np.log10(_median091m70)], color='#028957')

ax4.fill_between([2.,1., 0.], [np.log10(min032m70),np.log10(min041m70),np.log10(min091m70)],
                 [np.log10(max032m70),np.log10(max041m70),np.log10(max091m70)], edgecolor='#810090',
                 hatch="/////", color='none', facecolor='none')
ax4.fill_between([2.,1., 0.], [np.log10(_min032m70),np.log10(_min041m70),np.log10(_min091m70)], 
                 [np.log10(_max032m70),np.log10(_max041m70),np.log10(_max091m70)],alpha=0.4,edgecolor='#028957', facecolor='#028957')

plt.text(0.2,11,'M$_{R<70Kpc}$',horizontalalignment='left', verticalalignment='top',fontsize=50)
ax4.legend(loc='upper right', frameon=False, scatterpoints=1,borderpad=0.6, labelspacing=0.7)
ax4.set_xlabel('z')
ax4.set_ylim(10.6,12.7)
ax4.set_xlim(-0.1,2.1)
ax4.yaxis.set_major_formatter(NullFormatter())
xticks4 = ax4.xaxis.get_major_ticks()
xticks4[1].label1.set_visible(False)
xticks4[-2].label1.set_visible(False)
ax4.minorticks_on()
#------------------------------------------------------------------------------------------------------------------------------------

plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig('evolucion.pdf', format='pdf', dpi=1500,bbox_inches='tight')
plt.show()

