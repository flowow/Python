#시각화 연습
import matplotlib as mpl
import matplotlib.pylab as plt
#선(라인 플롯):시계열 데이터의 변화

# plt.title("Plot")
# plt.plot([1,2,4,8])
# plt.show()

# plt.title("Plot")
# plt.plot([10,20,30,40],[1,2,4,8])
# plt.show()

plt.title("Plot")
plt.plot([10,20,30,40],[1,2,4,8], 'y^:') #r:색상,s:마커, --:선종류
plt.show()

#https://matplotlib.org/examples/color/named_colors.html

#
# plt.plot([1,2,3], [10,30,90], c='r', lw=5,ls='--',
#          marker='o',ms=15,mec="b", mfc="g",mew=5)
# plt.xlim(0,10)
# plt.ylim(-10, 100)
# plt.show()








