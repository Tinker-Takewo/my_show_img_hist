# メイン
import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread

# title
st.title('Show Picture shuffled color')

# download the image
img_url = 'https://pbs.twimg.com/media/Fmr9BAtagAAZUvN?format=jpg&name=900x900'

im = imread(img_url)

st.image(im, caption='image from Twitter',
         use_column_width=True)


# show histgram of all colors
#hist_red, _ = np.histogram(im[:, :, 0], bins=64)
#ist_green, _ = np.histogram(im[:, :, 1], bins=64)
#hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
#hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

#df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
#st.bar_chart(df_hist)


# choose one color
#color = st.radio(
#    "choose R, G, or B",
#    ('R', 'G', 'B'))
#if color == 'R':
#    df_hist = pd.DataFrame(hist_red)
#    st.bar_chart(df_hist)
#if color == 'G':
#    df_hist = pd.DataFrame(hist_green)
#    st.bar_chart(df_hist)
#if color == 'B':
#    df_hist = pd.DataFrame(hist_blue)
#    st.bar_chart(df_hist)

# change color

im_change=im

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        t = im_change[i,j,0]
        im_change[i,j,0]= im_change[i,j,1]
        im_change[i,j,1]= im_change[i,j,2]
        im_change[i,j,2]= t

st.image(im_change, caption='image from Twitter',
        use_column_width=True)

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        t = im_change[i,j,0]
        im_change[i,j,0]= im_change[i,j,1]
        im_change[i,j,1]= im_change[i,j,2]
        im_change[i,j,2]= t

st.image(im_change, caption='image from Twitter',
        use_column_width=True)

# 単一の色だけ表示
im_change=im

color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))

c = 0

if color == 'R':
    c = 0
if color == 'G':
    c = 1
if color == 'B':
    c = 2

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        im_change[i,j,(c+1)/3]= 0
        im_change[i,j,(c+2)/3]= 0

st.image(im_change, caption='image from Twitter',
        use_column_width=True)