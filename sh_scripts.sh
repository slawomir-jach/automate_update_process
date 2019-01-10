(for i in {1..30}; do echo y; sleep 1; done) | echo "y" | /opt/android/android-sdk-linux/tools/android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-23

(for i in {1..30}; do echo y; sleep 1; done) | echo "y" | /opt/android/android-sdk-linux/tools/android update sdk --no-ui --all --filter NAME_OF_THE_COMPONENT_I_NEED

