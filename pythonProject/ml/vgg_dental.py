from keras.applications import VGG16
from keras import Sequential
from keras.layers import Flatten, Dense, Dropout
from keras.src.preprocessing.image import ImageDataGenerator


#데이터 로드 및 전처리
train_dir = './dental_image/train'
test_dir = './dental_image/test'

train_datagen = ImageDataGenerator(
    rotation_range=180  #  회전
    ,width_shift_range = 0.2 #좌우 이동
    ,height_shift_range=0.2 #상하 이동
    ,horizontal_flip=True  #좌우 반전
    ,vertical_flip=True #상하 반전
    ,brightness_range=[0.5, 1.5]    #명암 증감
)
test_datagen = ImageDataGenerator()
train_generator = train_datagen.flow_from_directory(
    train_dir, target_size=(224, 224), batch_size=32
    , class_mode='categorical', shuffle=True
)
test_generator = test_datagen.flow_from_directory(
    test_dir, target_size=(224, 224), batch_size=32
    , class_mode='categorical', shuffle=True)

class_num = len(train_generator.class_indices)
labels = list(train_generator.class_indices.keys())
print(f'분류 수 : {class_num}, 라벨: {labels}')

# tensorflow의 pre-trained model 가져오기
conv_layer = VGG16(weights='imagenet', include_top=False
                   , input_shape=(224, 224, 3))
conv_layer.summary()
# VGG16모델의 잘 학습된 부분이 학습되지 않도록 고정
for layer in conv_layer.layers:
    layer.trainable = False
model = Sequential()
model.add(conv_layer)
model.add(Flatten())    # 치아 분류를 위한 fine tuning 부분
model.add(Dense(3, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam'
              ,metrics=['acc'])
model.fit_generator(train_generator
                    , steps_per_epoch=train_generator.samples/train_generator.batch_size
                    , epochs=30
                    , validation_data=test_generator
                    , validation_steps= test_generator.samples/test_generator.batch_size
                    ,verbose=1)
model.save('dental_model.h5')

